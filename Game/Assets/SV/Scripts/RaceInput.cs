namespace SV
{
    /// One frame of player intent. Every gameplay system reads this and nothing else.
    public struct RaceInput
    {
        public float steer;      // -1..1, left..right
        public float throttle;   // 0..1
        public bool airbrakeL, airbrakeR, boost, pulse;
        public bool manual;      // true = tilt/slider drive the craft; false = follow planned line (later)
        public int line;         // active planned line index (later)
    }

    public interface IInputProvider
    {
        RaceInput Current { get; }
        bool Connected { get; }
        string Status { get; }
    }
}
