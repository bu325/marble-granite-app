#!/usr/bin/env bash
set -e
buildozer android clean
buildozer -v android debug
