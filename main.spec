from kivy_deps import sdl2, glew

# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\users\\tasee\\PycharmProjects\\pythonProject2'],
             binaries=[],
             datas=[],
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
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe, Tree ('C:\\Users\\tasee\\PycharmProjects\\pythonProject2'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in
               (sdl2.dep_bins+
               glew.dep_noms)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
