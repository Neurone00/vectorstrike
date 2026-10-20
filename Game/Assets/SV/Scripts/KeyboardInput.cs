using UnityEngine;

namespace SV
{
    /// Dev fallback: arrows/WASD steer and throttle, Q/E airbrakes, Shift boost, Space pulse.
    public class KeyboardInput : MonoBehaviour, IInputProvider
    {
        RaceInput cur;
        public RaceInput Current => cur;
        public bool Connected => true;
        public string Status => "keyboard";

        void Update()
        {
            cur.steer = Input.GetAxisRaw("Horizontal");
            float v = Input.GetAxisRaw("Vertical");
            cur.throttle = v > 0 ? 1f : (v < 0 ? 0f : 0.6f); // idles at 60% so it drives with no key held
            cur.airbrakeL = Input.GetKey(KeyCode.Q);
            cur.airbrakeR = Input.GetKey(KeyCode.E);
            cur.boost = Input.GetKey(KeyCode.LeftShift);
            cur.pulse = Input.GetKeyDown(KeyCode.Space);
            cur.manual = true;
        }
    }
}
