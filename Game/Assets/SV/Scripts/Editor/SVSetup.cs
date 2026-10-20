using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;

namespace SV.Editor
{
    /// One-click scene: StrikeVector > Build Race Scene. Then press Play, or StrikeVector > Build Mac App.
    public static class SVSetup
    {
        const string ScenePath = "Assets/SV/Scenes/Race.unity";

        [MenuItem("StrikeVector/Build Race Scene")]
        public static void BuildRaceScene()
        {
            var scene = EditorSceneManager.NewScene(NewSceneSetup.DefaultGameObjects, NewSceneMode.Single);

            var track = new GameObject("Track").AddComponent<TrackSpline>();
            track.Build();

            var inputs = new GameObject("Input");
            var kb = inputs.AddComponent<KeyboardInput>();
            var phone = inputs.AddComponent<PhoneInput>();
            var router = inputs.AddComponent<InputRouter>();
            router.keyboard = kb; router.phone = phone;

            var craft = new GameObject("Kestrel").AddComponent<CraftMover>();
            craft.track = track; craft.inputSource = router;
            BuildPlaceholderBody(craft.transform);

            var cam = Camera.main;
            if (cam == null) cam = new GameObject("Main Camera", typeof(Camera), typeof(AudioListener)).GetComponent<Camera>();
            cam.farClipPlane = 3000f;
            var chase = cam.gameObject.AddComponent<ChaseCamera>(); chase.craft = craft;
            var hud = cam.gameObject.AddComponent<RaceHud>(); hud.craft = craft; hud.input = router;
            var tel = cam.gameObject.AddComponent<Telemetry>(); tel.craft = craft; tel.input = router;

            var light = Object.FindAnyObjectByType<Light>();
            if (light) light.transform.rotation = Quaternion.Euler(45f, 35f, 0f);

            System.IO.Directory.CreateDirectory("Assets/SV/Scenes");
            EditorSceneManager.SaveScene(scene, ScenePath);
            EditorBuildSettings.scenes = new[] { new EditorBuildSettingsScene(ScenePath, true) };
            Debug.Log("StrikeVector: race scene built at " + ScenePath + ". Press Play. Phone relay: node Tools/controller/server.js");
        }

        /// Three boxes read as the forked Kestrel silhouette until the real blockout GLB lands.
        static void BuildPlaceholderBody(Transform root)
        {
            var bone = SVMaterials.Flat(new Color(0.72f, 0.69f, 0.60f));
            var charcoal = SVMaterials.Flat(new Color(0.15f, 0.17f, 0.19f));
            Box(root, "Body", new Vector3(0f, 0.55f, -0.8f), new Vector3(2.2f, 1.1f, 4.0f), charcoal);
            Box(root, "ProngL", new Vector3(-1.1f, 0.5f, 1.4f), new Vector3(1.0f, 0.9f, 2.8f), bone);
            Box(root, "ProngR", new Vector3(1.1f, 0.5f, 1.4f), new Vector3(1.0f, 0.9f, 2.8f), bone);
            Box(root, "PodL", new Vector3(-1.3f, 0.7f, -2.5f), new Vector3(0.8f, 0.8f, 1.0f), charcoal);
            Box(root, "PodR", new Vector3(1.3f, 0.7f, -2.5f), new Vector3(0.8f, 0.8f, 1.0f), charcoal);
        }

        static void Box(Transform parent, string name, Vector3 pos, Vector3 size, Material m)
        {
            var g = GameObject.CreatePrimitive(PrimitiveType.Cube);
            Object.DestroyImmediate(g.GetComponent<Collider>());
            g.name = name; g.transform.SetParent(parent, false);
            g.transform.localPosition = pos; g.transform.localScale = size;
            g.GetComponent<MeshRenderer>().sharedMaterial = m;
        }

        [MenuItem("StrikeVector/Build Mac App")]
        public static void BuildMac()
        {
            var opts = new BuildPlayerOptions
            {
                scenes = new[] { ScenePath },
                locationPathName = "Builds/StrikeVector.app",
                target = BuildTarget.StandaloneOSX,
                options = BuildOptions.None
            };
            var report = BuildPipeline.BuildPlayer(opts);
            Debug.Log("StrikeVector build: " + report.summary.result + " -> Game/Builds/StrikeVector.app");
        }
    }
}
