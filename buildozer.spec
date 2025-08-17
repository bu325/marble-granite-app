[app]
title = Marble Granite Manager
package.name = marblegranite
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,xml,db,json
version = 0.1
requirements = python3,kivy==2.2.1,kivymd==1.1.1,arabic_reshaper,python-bidi,peewee,requests,plyer,pillow
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.archs = armeabi-v7a
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[app:source.exclude_patterns]
# استثناء مجلدات/ملفات غير ضرورية
.git
__pycache__
*.pyc
*.pyo
*.md

[app:python]
# خيارات بايثون إضافية (خليها فاضية حالياً)
