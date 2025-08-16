[app]
title = Marble & Granite Manager
package.name = MarbleGranite
package.domain = com.marblegranite.app
source.dir = app
version = 1.0.0
requirements = python3,kivy==2.3.0,kivymd,peewee,reportlab,arabic_reshaper,python-bidi,requests,plyer,matplotlib,pillow
orientation = portrait
fullscreen = 0
log_level = 2
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET,CAMERA
android.api = 33
android.minapi = 24
p4a.bootstrap = sdl2
source.include_exts = py,kv,ttf,otf,png,jpg,jpeg,pdf,db,json,txt,md
source.include_patterns = assets/fonts/*,app_data/attachments/*,app_data/pdfs/*
android.archs = armeabi-v7a, arm64-v8a
android.enable_androidx = 1
# android.allow_backup = 0


# (Optional) Signing config for release – will be injected by CI if not set locally
# android.release_keystore = release.keystore
# android.release_keystore_password = YOUR_KEYSTORE_PASSWORD
# android.release_keyalias = YOUR_KEY_ALIAS
# android.release_keyalias_password = YOUR_KEY_PASSWORD

[buildozer]
log_level = 2

[app.android]
# Place Android-specific customizations here if needed
