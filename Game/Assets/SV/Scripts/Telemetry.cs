using System.IO;
using UnityEngine;

namespace SV
{
    /// Logs craft state every 2 s and, when launched with -sv-shots, saves a screenshot alongside each log line.
    /// ponytail: headless verification aid; harmless in normal play.
    public class Telemetry : MonoBehaviour
    {
        public CraftMover craft;
        public InputRouter input;
        public float every = 2f;
        float next; int n; string dir;

        void Start()
        {
            Application.runInBackground = true; // keep driving when the window is not focused (phone tests, demos)
            foreach (var a in System.Environment.GetCommandLineArgs()) if (a == "-sv-shots") dir = Path.Combine(Application.persistentDataPath, "shots");
            if (dir != null) Directory.CreateDirectory(dir);
        }

        void Update()
        {
            if (!craft || Time.time < next) return;
            next = Time.time + every;
            Debug.Log($"SV t={Time.time:F1} s={craft.S:F1} lat={craft.Lateral:F2} speed={craft.Speed:F1} lap={craft.Lap} input={(input ? input.Status : "-")}");
            if (dir != null) ScreenCapture.CaptureScreenshot(Path.Combine(dir, $"shot_{n++:D3}.png"));
        }
    }
}
