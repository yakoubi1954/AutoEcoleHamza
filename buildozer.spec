[app]
title = AutoEcole Hamza
package.name = AutoEcoleHamza
package.domain = org.hamza

source.dir = .
source.include_exts = py,png,jpg,kv
source.include_patterns = assets/*
source.exclude_dirs = venv,.venv,bin

requirements = python3,kivy,android
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

version = 0.1
version.code = 1
version.name = 0.1

icon.filename = assets/icon.png
presplash.filename = assets/splash.png
android.extra_args = --lang=fr

android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_path = /home/yakoubi/.buildozer/android/platform/android-ndk-r25b

[buildozer]
log_level = 2
warn_on_root = 1
android.archs = arm64-v8a
