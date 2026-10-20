using System.Collections.Generic;
using UnityEngine;

namespace SV
{
    /// Closed Catmull-Rom centerline. Every racer lives in (s, lateral) on it.
    /// Also generates a flat deck ribbon and two walls so there is something to see.
    [ExecuteAlways]
    public class TrackSpline : MonoBehaviour
    {
        public List<Vector3> points = new List<Vector3>();
        public float width = 16f;
        public float wallHeight = 1.2f;
        public int samplesPerSegment = 12;

        Vector3[] pos;      // sampled positions
        float[] cum;        // cumulative length at each sample
        public float Length { get; private set; }

        void OnEnable() { Build(); }

        public void Build()
        {
            if (points.Count < 4) points = DefaultLoop();
            int n = points.Count;
            var list = new List<Vector3>();
            for (int i = 0; i < n; i++)
            {
                Vector3 p0 = points[(i - 1 + n) % n], p1 = points[i], p2 = points[(i + 1) % n], p3 = points[(i + 2) % n];
                for (int k = 0; k < samplesPerSegment; k++)
                    list.Add(CatmullRom(p0, p1, p2, p3, k / (float)samplesPerSegment));
            }
            pos = list.ToArray();
            cum = new float[pos.Length + 1];
            for (int i = 0; i < pos.Length; i++)
                cum[i + 1] = cum[i] + Vector3.Distance(pos[i], pos[(i + 1) % pos.Length]);
            Length = cum[pos.Length];
            BuildMesh();
        }

        static Vector3 CatmullRom(Vector3 p0, Vector3 p1, Vector3 p2, Vector3 p3, float t)
        {
            float t2 = t * t, t3 = t2 * t;
            return 0.5f * ((2f * p1) + (-p0 + p2) * t + (2f * p0 - 5f * p1 + 4f * p2 - p3) * t2 + (-p0 + 3f * p1 - 3f * p2 + p3) * t3);
        }

        /// Position and frame at arc length s (wraps). right = cross(up, forward).
        public void Sample(float s, out Vector3 p, out Vector3 forward, out Vector3 right)
        {
            s = Mathf.Repeat(s, Length);
            int lo = 0, hi = pos.Length;
            while (hi - lo > 1) { int mid = (lo + hi) / 2; if (cum[mid] <= s) lo = mid; else hi = mid; }
            Vector3 a = pos[lo], b = pos[(lo + 1) % pos.Length];
            float seg = cum[lo + 1] - cum[lo];
            float t = seg > 1e-5f ? (s - cum[lo]) / seg : 0f;
            p = Vector3.Lerp(a, b, t);
            forward = (b - a).normalized;
            right = Vector3.Cross(Vector3.up, forward).normalized;
        }

        void BuildMesh()
        {
            var mf = GetComponent<MeshFilter>(); if (!mf) mf = gameObject.AddComponent<MeshFilter>();
            var mr = GetComponent<MeshRenderer>(); if (!mr) mr = gameObject.AddComponent<MeshRenderer>();
            int n = pos.Length;
            var v = new Vector3[n * 6];
            var tri = new List<int>();
            float h = width * 0.5f;
            for (int i = 0; i < n; i++)
            {
                Sample(cum[i], out var p, out _, out var r);
                v[i * 6 + 0] = p - r * h;                       // deck left
                v[i * 6 + 1] = p + r * h;                       // deck right
                v[i * 6 + 2] = p - r * h;                       // wall left bottom
                v[i * 6 + 3] = p - r * h + Vector3.up * wallHeight;
                v[i * 6 + 4] = p + r * h;                       // wall right bottom
                v[i * 6 + 5] = p + r * h + Vector3.up * wallHeight;
                int j = (i + 1) % n;
                Quad(tri, i * 6 + 0, i * 6 + 1, j * 6 + 1, j * 6 + 0);   // deck, up-facing
                Quad(tri, i * 6 + 3, i * 6 + 2, j * 6 + 2, j * 6 + 3);   // left wall, faces inward
                Quad(tri, i * 6 + 4, i * 6 + 5, j * 6 + 5, j * 6 + 4);   // right wall, faces inward
            }
            var mesh = new Mesh { name = "Track" };
            mesh.indexFormat = UnityEngine.Rendering.IndexFormat.UInt32;
            mesh.vertices = v; mesh.triangles = tri.ToArray();
            mesh.RecalculateNormals(); mesh.RecalculateBounds();
            mf.sharedMesh = mesh;
            if (mr.sharedMaterial == null) mr.sharedMaterial = SVMaterials.Flat(new Color(0.16f, 0.17f, 0.19f));
        }

        static void Quad(List<int> t, int a, int b, int c, int d) { t.Add(a); t.Add(c); t.Add(b); t.Add(a); t.Add(d); t.Add(c); } // clockwise = front face in Unity

        /// ~1.4 km loop with varied bends, flat. ponytail: parametric placeholder until the circuit layout reference arrives.
        static List<Vector3> DefaultLoop()
        {
            var l = new List<Vector3>();
            for (int i = 0; i < 24; i++)
            {
                float a = i / 24f * Mathf.PI * 2f;
                float r = 1f + 0.18f * Mathf.Sin(3f * a) + 0.08f * Mathf.Cos(5f * a);
                l.Add(new Vector3(Mathf.Cos(a) * 240f * r, 0f, Mathf.Sin(a) * 150f * r));
            }
            return l;
        }
    }
}
