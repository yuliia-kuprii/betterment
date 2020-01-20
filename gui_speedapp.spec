# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['gui_speedapp.py'],
             pathex=['/Users/yuliiakuprii/PycharmProjects/Betterment'],
             binaries=[],
             datas=[('tortuga_bg.gif', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='gui_speedapp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='tortuga_icon.icns')
app = BUNDLE(exe,
             name='gui_speedapp.app',
             icon='tortuga_icon.icns',
             bundle_identifier=None)
