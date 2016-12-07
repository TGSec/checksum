@echo off

cmd /c "nuitka checksum.py"
rmdir /s /q "checksum.build"
del "win32 compiled\checksum.exe"
move checksum.exe "win32 compiled\"