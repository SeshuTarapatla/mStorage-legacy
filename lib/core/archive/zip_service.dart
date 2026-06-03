import 'dart:io';

import 'package:archive/archive_io.dart';

// Note: the archive package uses ZipCrypto (traditional ZIP password protection),
// not AES-256. Both ZipFileEncoder (create) and ZipDecoder (extract) stream
// file content via InputFileStream/OutputFileStream, so large video files
// never need to fit in memory.
class ZipService {
  /// Creates a password-protected ZIP at [outputPath] containing [filePaths].
  /// Uses STORE compression (no deflate) since video files are pre-compressed.
  static Future<void> createEncryptedZip({
    required List<String> filePaths,
    required String outputPath,
    required String password,
  }) async {
    final encoder = ZipFileEncoder(password: password);
    encoder.create(outputPath, level: ZipFileEncoder.STORE);
    for (final filePath in filePaths) {
      await encoder.addFile(File(filePath), null, ZipFileEncoder.STORE);
    }
    await encoder.close();
  }

  /// Extracts a ZIP archive to [outputDir].
  static Future<void> extractZip({
    required String archivePath,
    required String outputDir,
    required String password,
  }) async {
    final input = InputFileStream(archivePath);
    final archive = ZipDecoder().decodeBuffer(input, password: password);
    await extractArchiveToDiskAsync(archive, outputDir);
    await input.close();
    await archive.clear();
  }
}
