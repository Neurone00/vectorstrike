'use strict';
// STRIKE VECTOR phone controller relay.
// HTTP: serves this folder's static files. WS: phones <-> game relay.
const http = require('http');
const https = require('https');
const fs = require('fs');
const os = require('os');
const path = require('path');
const { WebSocketServer } = require('ws');
const qr = require('qrcode-terminal');

const PORT = 8080;        // plain HTTP: serves the page, or redirects to HTTPS when certs exist
const TLS_PORT = 8443;    // HTTPS + wss when key.pem/cert.pem exist
const ROOT = __dirname;
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.png': 'image/png', '.svg': 'image/svg+xml', '.apk': 'application/vnd.android.package-archive' };

// HTTPS if key.pem + cert.pem exist (Android Chrome only fires deviceorientation on secure origins).
// Make them with: openssl req -x509 -newkey rsa:2048 -nodes -keyout key.pem -out cert.pem -days 3650 -subj /CN=sv -addext subjectAltName=IP:<lan-ip>
const tls = fs.existsSync(path.join(ROOT, 'key.pem')) && { key: fs.readFileSync(path.join(ROOT, 'key.pem')), cert: fs.readFileSync(path.join(ROOT, 'cert.pem')) };
const handler = (req, res) => {
  console.log(`GET ${req.url} from ${req.socket.remoteAddress}`);
  let p = decodeURIComponent(req.url.split('?')[0]);
  if (p === '/') p = '/race.html';
  if (p === '/app.apk') p = '/android/app/build/outputs/apk/debug/app-debug.apk';   // phone downloads the controller app from here
  const file = path.join(ROOT, path.normalize(p));
  if (!file.startsWith(ROOT)) { res.writeHead(403); return res.end(); }
  fs.readFile(file, (err, data) => {
    if (err) { res.writeHead(404); return res.end('not found'); }
    res.writeHead(200, { 'Content-Type': MIME[path.extname(file)] || 'application/octet-stream', 'Cache-Control': 'no-store' });
    res.end(data);
  });
};
const server = tls ? https.createServer(tls, handler) : http.createServer(handler);

// Relay: role is set by the first {role:"phone"|"game"} message.
const wss = new WebSocketServer({ server });
// Plain ws on localhost only, for the game process (Unity's TLS stack rejects the self-signed cert).
const local = http.createServer((_, res) => { res.writeHead(404); res.end(); });
const wssLocal = new WebSocketServer({ server: local });
wssLocal.on('connection', onConnection);
wss.on('connection', onConnection);
function allClients() { return [...wss.clients, ...wssLocal.clients]; }
function onConnection(ws, req) {
  ws.role = null;
  ws.on('message', (buf) => {
    const text = buf.toString();
    if (!ws.role) {
      try { ws.role = JSON.parse(text).role === 'game' ? 'game' : 'phone'; } catch { ws.role = 'phone'; }
      console.log(`+ ${ws.role} ${req.socket.remoteAddress}`);
      return;
    }
    if (text.startsWith('{"diag"')) return console.log(`diag ${req.socket.remoteAddress} ${JSON.parse(text).diag}`);
    const target = ws.role === 'phone' ? 'game' : 'phone';
    for (const c of allClients()) if (c !== ws && c.role === target && c.readyState === 1) c.send(text);
  });
  ws.on('close', () => ws.role && console.log(`- ${ws.role} ${req.socket.remoteAddress}`));
}

function lanIp() {
  for (const ifs of Object.values(os.networkInterfaces()))
    for (const i of ifs) if (i.family === 'IPv4' && !i.internal) return i.address;
  return '127.0.0.1';
}

local.listen(PORT + 1, '127.0.0.1');
// With TLS, port 8080 stays plain HTTP and redirects, so typing "ip:8080" without https:// still works.
if (tls) http.createServer((req, res) => {
  console.log(`redirect ${req.url} from ${req.socket.remoteAddress}`);
  res.writeHead(302, { Location: `https://${(req.headers.host || lanIp()).split(':')[0]}:${TLS_PORT}${req.url}` }); res.end();
}).listen(PORT);
const port = tls ? TLS_PORT : PORT;
server.listen(port, () => {
  const url = `${tls ? 'https' : 'http'}://${lanIp()}:${port}/race.html`;
  console.log(`STRIKE VECTOR controller\n  app  : ${tls ? 'https' : 'http'}://${lanIp()}:${port}/app.apk\n  phone: ${url}${tls ? `  (or type ${lanIp()}:${PORT})` : ''}\n  game : ${tls ? 'wss' : 'ws'}://${lanIp()}:${port}  (send {"role":"game"} first)\n  local: ws://127.0.0.1:${PORT + 1}  (plain, for the game on this Mac)\n`);
  qr.generate(url, { small: true });
});
