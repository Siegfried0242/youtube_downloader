# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['F:/Python/Beginning/finished_project/youtube_downloader/youtube_create.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/kujon/AppData/Local/Programs/Python/Python310/Lib/site-packages/customtkinter', 'customtkinter/'), ('F:/Python/Beginning/finished_project/youtube_downloader/fgfdfdfdf.png', '.'), ('F:/Python/Beginning/finished_project/youtube_downloader/icon_.png', '.'), ('F:/Python/Beginning/finished_project/youtube_downloader/yt_icon.ico', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='youtube_create',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='yt_icon.ico',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='youtube_create',
)
