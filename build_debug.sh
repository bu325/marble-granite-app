#!/bin/bash

# Build Debug APK Script for Marble Granite Manager

echo "Building Debug APK for Marble Granite Manager..."

# Check if buildozer is installed
if ! command -v buildozer &> /dev/null; then
    echo "Buildozer not found. Installing..."
    pip install buildozer
fi

# Initialize buildozer if needed
if [ ! -d ".buildozer" ]; then
    echo "Initializing buildozer..."
    buildozer init
fi

# Build debug APK
echo "Building debug APK..."
buildozer -v android debug

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "Debug APK built successfully!"
    echo "APK location: bin/marblegranitemanager-0.1-debug.apk"
else
    echo "Build failed. Check the output above for errors."
    exit 1
fi

