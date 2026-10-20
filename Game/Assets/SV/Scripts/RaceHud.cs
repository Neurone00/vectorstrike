using UnityEngine;

namespace SV
{
    /// Minimal debug HUD. ponytail: OnGUI until the real HUD art exists.
    public class RaceHud : MonoBehaviour
    {
        public CraftMover craft;
        public InputRouter input;
        GUIStyle big, small;

        void OnGUI()
        {
            if (big == null)
            {
                big = new GUIStyle(GUI.skin.label) { fontSize = 36, fontStyle = FontStyle.Bold };
                small = new GUIStyle(GUI.skin.label) { fontSize = 18 };
            }
            if (!craft) return;
            GUI.Label(new Rect(20, 20, 400, 50), Mathf.RoundToInt(craft.Speed * 3.6f) + " km/h", big);
            GUI.Label(new Rect(20, 70, 400, 30), "Lap " + (craft.Lap + 1) + "   " + Mathf.RoundToInt(craft.S) + " / " + Mathf.RoundToInt(craft.track.Length) + " m", small);
            if (input) GUI.Label(new Rect(20, 100, 600, 30), input.Status + "   (keyboard: arrows/WASD, Q/E airbrakes, Shift boost)", small);
            if (GUI.Button(new Rect(20, 140, 120, 30), "Reset")) craft.ResetToStart();
        }
    }
}
