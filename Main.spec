# -*- mode: python -*-

block_cipher = None


a = Analysis(['Main.py'],
             pathex=['D:\\Soft\\Python36-32\\Lib', 'D:\\Soft\\Python36-32\\Lib\\site-packages', '', 'E:\\Python Life\\FuleiTools'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Main',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='E:\\Python Life\\FuleiTools\\Resouces\\flkjlogo.ico')
