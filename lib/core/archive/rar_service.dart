import 'dart:io';

import 'package:flutter/services.dart';
import 'package:path/path.dart' as p;
import 'package:path_provider/path_provider.dart';

// Handles legacy RAR archives created by the old Nuitka binaries.
// Requires unrar.exe bundled at assets/bin/unrar.exe.
// New files encoded by this app use ZIP; this service is decode-only.
class RarService {
  static String? _unrarPath;

  /// Extracts a RAR archive to [outputDir] using the bundled unrar.exe.
  static Future<void> extractRar({
    required String archivePath,
    required String outputDir,
    required String password,
  }) async {
    final unrar = await _ensureUnrar();
    await Directory(outputDir).create(recursive: true);
    final result = await Process.run(unrar, [
      'x',
      '-y',
      '-p$password',
      archivePath,
      '$outputDir${p.separator}',
    ]);
    if (result.exitCode != 0) {
      throw Exception(
        'Legacy RAR extraction failed (exit ${result.exitCode}): ${result.stderr}',
      );
    }
  }

  /// Extracts unrar.exe from Flutter assets to the system temp directory
  /// on first call, then caches the path for the session.
  static Future<String> _ensureUnrar() async {
    if (_unrarPath != null) return _unrarPath!;
    final tempDir = await getTemporaryDirectory();
    final dest = File(p.join(tempDir.path, 'mstorage_unrar.exe'));
    if (!await dest.exists()) {
      final ByteData data;
      try {
        data = await rootBundle.load('assets/bin/unrar.exe');
      } catch (_) {
        throw StateError(
          'unrar.exe not found in assets/bin/. '
          'Add it to assets/bin/ to enable legacy RAR file decoding.',
        );
      }
      await dest.writeAsBytes(data.buffer.asUint8List());
    }
    _unrarPath = dest.path;
    return _unrarPath!;
  }
}
