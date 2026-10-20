using UnityEngine;

namespace SV
{
    /// Uses the phone while it is streaming, otherwise the keyboard. The craft reads from here.
    public class InputRouter : MonoBehaviour, IInputProvider
    {
        public PhoneInput phone;
        public KeyboardInput keyboard;
        IInputProvider Active => phone != null && phone.Connected ? phone : (IInputProvider)keyboard;
        public RaceInput Current => Active.Current;
        public bool Connected => true;
        public string Status => Active.Status;
    }
}
