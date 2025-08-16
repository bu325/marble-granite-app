#!/bin/bash

# Build Release APK Script for Marble Granite Manager

echo "Building Release APK for Marble Granite Manager..."

# Check if buildozer is installed
if ! command -v buildozer &> /dev/null; then
    echo "Buildozer not found. Installing..."
    pip install buildozer
fi

# Check if keystore exists
KEYSTORE_FILE="my-release-key.keystore"
if [ ! -f "$KEYSTORE_FILE" ]; then
    echo "Keystore not found. Creating new keystore..."
    echo "Please provide the following information for the keystore:"
    
    keytool -genkey -v -keystore $KEYSTORE_FILE -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000
    
    if [ $? -ne 0 ]; then
        echo "Failed to create keystore. Exiting."
        exit 1
    fi
    
    echo "Keystore created successfully: $KEYSTORE_FILE"
    echo "Please update buildozer.spec with the keystore information:"
    echo "  [app]"
    echo "  android.keystore = $KEYSTORE_FILE"
    echo "  android.keyalias = my-key-alias"
    echo "  android.keystore_passwd = <your_keystore_password>"
    echo "  android.keyalias_passwd = <your_key_password>"
    echo ""
    echo "Then run this script again."
    exit 0
fi

# Build release APK
echo "Building release APK..."
buildozer android release

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "Release APK built successfully!"
    echo "APK location: bin/marblegranitemanager-0.1-release.apk"
else
    echo "Build failed. Check the output above for errors."
    exit 1
fi

