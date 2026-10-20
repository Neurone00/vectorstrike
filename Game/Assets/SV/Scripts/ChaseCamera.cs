using UnityEngine;

namespace SV
{
    /// Chase camera: sits behind and above the craft, looks ahead, widens FOV with speed. No Cinemachine needed yet.
    public class ChaseCamera : MonoBehaviour
    {
        public CraftMover craft;
        public float back = 11f, up = 4.5f, lookAhead = 12f;
        public float smooth = 8f;
        public float fovMin = 60f, fovMax = 82f;

        Camera cam;
        void Start() { cam = GetComponent<Camera>(); if (craft) transform.position = Goal(); }

        void LateUpdate()
        {
            if (!craft) return;
            transform.position = Vector3.Lerp(transform.position, Goal(), 1f - Mathf.Exp(-smooth * Time.deltaTime));
            var t = craft.transform;
            transform.rotation = Quaternion.LookRotation(t.position + t.forward * lookAhead - transform.position, Vector3.up);
            if (cam) cam.fieldOfView = Mathf.Lerp(fovMin, fovMax, craft.Speed / craft.maxSpeed);
        }

        Vector3 Goal()
        {
            var t = craft.transform;
            var flatFwd = Vector3.ProjectOnPlane(t.forward, Vector3.up).normalized;
            return t.position - flatFwd * back + Vector3.up * up;
        }
    }
}
