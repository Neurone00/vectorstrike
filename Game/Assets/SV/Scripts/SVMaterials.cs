using UnityEngine;
using UnityEngine.Rendering;

namespace SV
{
    /// Flat-colour material that works whether URP is assigned or the project is still on the built-in pipeline.
    public static class SVMaterials
    {
        public static Material Flat(Color c)
        {
            bool urp = GraphicsSettings.currentRenderPipeline != null;
            var sh = Shader.Find(urp ? "Universal Render Pipeline/Lit" : "Standard");
            var m = new Material(sh);
            m.SetColor(urp ? "_BaseColor" : "_Color", c);
            return m;
        }
    }
}
