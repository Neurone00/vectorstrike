using System;
using System.Net.WebSockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using UnityEngine;

namespace SV
{
    /// Reads the phone controller through the local Node relay (Tools/controller/server.js).
    /// Uses the .NET ClientWebSocket, so no package is needed. Reconnects every 2 s while disconnected.
    public class PhoneInput : MonoBehaviour, IInputProvider
    {
        [Serializable]
        class Msg { public float steer, throttle; public bool abL, abR, boost, pulse; public string mode; public int line; }

        public string url = "ws://127.0.0.1:8081";  // relay's plain local game port (phones use the TLS port 8080)
        public float staleAfter = 0.5f; // seconds without a message before we fall back to keyboard

        volatile string latest;
        float lastAt = -10f;
        bool pulseHeld;
        RaceInput cur;
        ClientWebSocket ws;
        CancellationTokenSource cts;

        public RaceInput Current => cur;
        public bool Connected => ws != null && ws.State == WebSocketState.Open && Time.unscaledTime - lastAt < staleAfter;
        public string Status => ws == null ? "phone: connecting" : "phone: " + ws.State + (Connected ? "" : " (no data)");

        void OnEnable()
        {
            cts = new CancellationTokenSource(); _ = Loop(cts.Token);
        }
        void OnDisable() { cts.Cancel(); try { ws?.Dispose(); } catch { } ws = null; }

        async Task Loop(CancellationToken ct)
        {
            var buf = new byte[4096];
            while (!ct.IsCancellationRequested)
            {
                try
                {
                    ws = new ClientWebSocket();
                    await ws.ConnectAsync(new Uri(url), ct);
                    var hello = Encoding.UTF8.GetBytes("{\"role\":\"game\"}");
                    await ws.SendAsync(new ArraySegment<byte>(hello), WebSocketMessageType.Text, true, ct);
                    while (ws.State == WebSocketState.Open && !ct.IsCancellationRequested)
                    {
                        var r = await ws.ReceiveAsync(new ArraySegment<byte>(buf), ct);
                        if (r.MessageType == WebSocketMessageType.Close) break;
                        latest = Encoding.UTF8.GetString(buf, 0, r.Count); // ponytail: one JSON per frame, < 4 KB
                    }
                }
                catch (Exception e) { Debug.LogWarning("PhoneInput " + url + " failed: " + e.GetBaseException().Message); }
                try { ws?.Dispose(); } catch { }
                ws = null;
                try { await Task.Delay(2000, ct); } catch (Exception) { }
            }
        }

        void Update()
        {
            var s = latest;
            if (s == null) return;
            latest = null;
            Msg m;
            try { m = JsonUtility.FromJson<Msg>(s); } catch (Exception) { return; }
            if (m == null) return;
            lastAt = Time.unscaledTime;
            cur.steer = Mathf.Clamp(m.steer, -1f, 1f);
            cur.throttle = Mathf.Clamp01(m.throttle);
            cur.airbrakeL = m.abL; cur.airbrakeR = m.abR; cur.boost = m.boost;
            cur.pulse = m.pulse && !pulseHeld; pulseHeld = m.pulse; // rising edge only
            cur.manual = m.mode != "auto";
            cur.line = m.line;
        }
    }
}
