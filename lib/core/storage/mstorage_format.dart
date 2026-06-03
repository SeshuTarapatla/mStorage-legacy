import 'dart:io';
import 'dart:typed_data';

enum ArchiveType { zip, rar, unknown }

// Handles reading and writing the mStorage container format:
//   [ mask video (MP4) ] + [ \nbreakpoint\n ] + [ archive (ZIP or RAR) ]
class MStorageFormat {
  static final _breakpointBytes =
      Uint8List.fromList('\nbreakpoint\n'.codeUnits);

  /// Extracts the archive portion of an encoded MP4 into a temp file.
  /// Returns the temp file path and the detected archive type.
  static Future<({String archivePath, ArchiveType type})> extractToTempFile(
    String inputPath,
  ) async {
    final tempDir = await Directory.systemTemp.createTemp('mstorage_');
    final tempArchivePath = '${tempDir.path}/archive';

    final raf = await File(inputPath).open();
    try {
      // Mask video is <5s so the breakpoint always falls within the first 10MB.
      final header = await raf.read(10 * 1024 * 1024);
      final bpIndex = _findBreakpoint(header);
      if (bpIndex == -1) {
        throw const FormatException(
          'Not a valid mStorage file: breakpoint marker not found',
        );
      }

      final archiveStart = bpIndex + _breakpointBytes.length;
      final sink = File(tempArchivePath).openWrite();
      try {
        sink.add(header.sublist(archiveStart));
        const chunkSize = 1024 * 1024;
        while (true) {
          final chunk = await raf.read(chunkSize);
          if (chunk.isEmpty) break;
          sink.add(chunk);
        }
      } finally {
        await sink.close();
      }
    } finally {
      await raf.close();
    }

    final typeBytes = await _readFirstBytes(File(tempArchivePath), 4);
    return (archivePath: tempArchivePath, type: _detectType(typeBytes));
  }

  /// Assembles a mask video and an archive file into a single output MP4.
  static Future<void> assemble({
    required String maskVideoPath,
    required String archivePath,
    required String outputPath,
  }) async {
    final sink = File(outputPath).openWrite();
    try {
      await sink.addStream(File(maskVideoPath).openRead());
      sink.add(_breakpointBytes);
      await sink.addStream(File(archivePath).openRead());
    } finally {
      await sink.close();
    }
  }

  static int _findBreakpoint(Uint8List bytes) {
    final m = _breakpointBytes;
    outer:
    for (var i = 0; i <= bytes.length - m.length; i++) {
      for (var j = 0; j < m.length; j++) {
        if (bytes[i + j] != m[j]) continue outer;
      }
      return i;
    }
    return -1;
  }

  static ArchiveType _detectType(Uint8List bytes) {
    if (bytes.length < 4) return ArchiveType.unknown;
    // ZIP magic: PK\x03\x04
    if (bytes[0] == 0x50 && bytes[1] == 0x4B &&
        bytes[2] == 0x03 && bytes[3] == 0x04) {
      return ArchiveType.zip;
    }
    // RAR magic: Rar!
    if (bytes[0] == 0x52 && bytes[1] == 0x61 &&
        bytes[2] == 0x72 && bytes[3] == 0x21) {
      return ArchiveType.rar;
    }
    return ArchiveType.unknown;
  }

  static Future<Uint8List> _readFirstBytes(File file, int count) async {
    final raf = await file.open();
    try {
      return await raf.read(count);
    } finally {
      await raf.close();
    }
  }
}
