// Logs what the game would receive. Run: node test_client.js
const WebSocket = require('ws');
// wss when the server has key.pem/cert.pem (self-signed, so skip verification)
const wss = require('fs').existsSync(__dirname + '/key.pem');
const ws = new WebSocket(`${wss ? 'wss' : 'ws'}://127.0.0.1:${process.env.PORT || (wss ? 8443 : 8080)}`, { rejectUnauthorized: false });
ws.on('open', () => { ws.send(JSON.stringify({ role: 'game' })); console.log('connected as game'); });
ws.on('message', d => console.log(d.toString()));
ws.on('close', () => console.log('closed'));
