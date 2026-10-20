#!/bin/bash
# Starts the phone relay and the built Mac app together. Ctrl-C stops both.
# ponytail: dev convenience; the two commands in the READMEs do the same thing by hand.
cd "$(dirname "$0")/.." || exit 1
APP=Game/Builds/StrikeVector.app
[ -d "$APP" ] || { echo "No build at $APP. In Unity: StrikeVector > Build Mac App."; exit 1; }
[ -d Tools/controller/node_modules ] || (cd Tools/controller && npm install)
(cd Tools/controller && node server.js) &
RELAY=$!
sleep 1
open -n "$APP" --args -screen-width 1280 -screen-height 720 -screen-fullscreen 0
echo "Phone app: type this Mac's IP shown above with :8080, tap Start, Calibrate, tilt."
trap 'kill $RELAY 2>/dev/null; pkill -f StrikeVector.app; exit 0' INT TERM
wait $RELAY
