# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\Asus\\Desktop\\BUT\\S2\\R2-07\\SAE\\Git\\SAE-C2\\App\\Controlleur.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/Asus/Desktop/BUT/S2/R2-07/SAE/Git/SAE-C2/App/modifiers', 'modifiers/'), ('C:/Users/Asus/Desktop/BUT/S2/R2-07/SAE/Git/SAE-C2/App/gradient', 'gradient/'), ('C:/Users/Asus/Desktop/BUT/S2/R2-07/SAE/Git/SAE-C2/App/ImageWidget.py', '.'), ('C:/Users/Asus/Desktop/BUT/S2/R2-07/SAE/Git/SAE-C2/App/SliderWidget.py', '.'), ('C:/Users/Asus/Desktop/BUT/S2/R2-07/SAE/Git/SAE-C2/App/Vue_Traitement.py', '.'), ('C:/Users/Asus/Desktop/BUT/S2/R2-07/SAE/Git/SAE-C2/images', 'images/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Controlleur',
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
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Controlleur',
)
