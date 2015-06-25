# -*- mode: python -*-

block_cipher = None


a = Analysis(['smash.py'],
             pathex=['C:\\Users\\Fabian\\Dropbox (MIT)\\Smash Up PT'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)
pyz = PYZ(a.pure,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='smash.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
