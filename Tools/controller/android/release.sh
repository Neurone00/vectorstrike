#!/bin/bash
# Build and publish a controller release: ./release.sh 0.3 ["notes"]
# Bumps versionName/versionCode (installer refuses updates otherwise), builds the debug APK,
# creates GitHub release controller-v<version> with the APK attached. Installed apps pick it up
# on next launch (Updater.java).
set -euo pipefail
cd "$(dirname "$0")"
V="${1:?version like 0.3}"; NOTES="${2:-Controller v$V}"
CODE=$(( $(echo "$V" | cut -d. -f1) * 100 + $(echo "$V" | cut -d. -f2) ))   # 0.3 -> 3, 1.2 -> 102
sed -i '' -E "s/versionCode = [0-9]+; versionName = \"[^\"]*\"/versionCode = $CODE; versionName = \"$V\"/" app/build.gradle.kts
export JAVA_HOME="${JAVA_HOME:-/opt/homebrew/opt/openjdk@21}" ANDROID_HOME="${ANDROID_HOME:-$HOME/Library/Android/sdk}"
./gradlew assembleDebug --no-daemon -q
OUT="$(mktemp -d)/SVController-v$V.apk"; cp app/build/outputs/apk/debug/app-debug.apk "$OUT"
gh release create "controller-v$V" "$OUT" --repo Neurone00/vectorstrike --target main --title "SV Controller v$V" --notes "$NOTES"
echo "released controller-v$V (versionCode $CODE)"
