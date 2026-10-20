using UnityEngine;

namespace SV
{
    /// Spline-constrained craft. State is (s, lateral, speed); manual mode maps tilt to lateral rate and slider to target speed.
    /// Auto mode (planned lines) comes later; until then auto behaves like manual with the input it has.
    public class CraftMover : MonoBehaviour
    {
        public TrackSpline track;
        public MonoBehaviour inputSource;   // anything implementing IInputProvider (InputRouter)

        [Header("Stats (per vehicle later)")]
        public float maxSpeed = 70f;        // m/s
        public float accel = 22f;
        public float brake = 45f;
        public float lateralRate = 16f;     // m/s across the deck at full tilt
        public float airbrakeDecel = 25f;
        public float airbrakeKick = 6f;     // extra lateral m/s toward the braking side
        public float boostMul = 1.35f;
        public float hoverHeight = 0.45f;
        public float leanDeg = 22f;
        public float edgeMargin = 1.2f;

        public float S { get; private set; }
        public float Lateral { get; private set; }
        public float Speed { get; private set; }
        public int Lap { get; private set; }

        IInputProvider input;

        void Start() { input = inputSource as IInputProvider; Place(); }

        void Update()
        {
            if (track == null || input == null) return;
            var i = input.Current;
            float dt = Time.deltaTime;

            float target = i.throttle * maxSpeed * (i.boost ? boostMul : 1f);
            float rate = target > Speed ? accel : brake;
            Speed = Mathf.MoveTowards(Speed, target, rate * dt);

            float lat = i.steer * lateralRate;
            if (i.airbrakeL) { Speed = Mathf.MoveTowards(Speed, 0f, airbrakeDecel * dt); lat -= airbrakeKick; }
            if (i.airbrakeR) { Speed = Mathf.MoveTowards(Speed, 0f, airbrakeDecel * dt); lat += airbrakeKick; }
            float half = track.width * 0.5f - edgeMargin;
            float next = Mathf.Clamp(Lateral + lat * dt, -half, half);
            if (Mathf.Abs(next) >= half - 0.01f && Mathf.Abs(Lateral) < half - 0.01f) Speed *= 0.85f; // wall scrape
            Lateral = next;

            S += Speed * dt;
            if (S >= track.Length) { S -= track.Length; Lap++; }
            Place(i.steer);
        }

        void Place(float steer = 0f)
        {
            if (track == null) return;
            track.Sample(S, out var p, out var f, out var r);
            transform.position = p + Vector3.up * hoverHeight + r * Lateral;
            transform.rotation = Quaternion.LookRotation(f, Vector3.up) * Quaternion.Euler(0f, 0f, -steer * leanDeg);
        }

        public void ResetToStart() { S = 0f; Lateral = 0f; Speed = 0f; Lap = 0; Place(); }
    }
}
