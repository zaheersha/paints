import { defineConfig } from "vite";
import { resolve } from "path";

export default defineConfig({
  resolve: {
    alias: {
      "@": resolve(__dirname, "src"), // 👈 This fixes "@/...." imports
    },
  },

  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, "index.html"),
        about: resolve(__dirname, "about.html"),
        contact: resolve(__dirname, "contact.html"),
        products: resolve(__dirname, "products.html"),
        cycleDistemper: resolve(__dirname, "cycle-distemper.html"),
        cycleExteriorEmulsion: resolve(__dirname, "cycle-exterior-emulsion.html"),
        cycleExteriorPrimer: resolve(__dirname, "cycle-exterior-primer.html"),
        cycleInteriorEmulsion: resolve(__dirname, "cycle-interior-emulsion.html"),
        cycleInteriorPrimer: resolve(__dirname, "cycle-interior-primer.html"),
        cycleMultiPrimer: resolve(__dirname, "cycle-multi-primer.html"),
        vegamCeilingWhite: resolve(__dirname, "vegam-ceiling-white.html"),
        vegamDampProof: resolve(__dirname, "vegam-dampproof.html"),
        vegamEnamel: resolve(__dirname, "vegam-enamel.html"),
        vegamExteriorEmulsion: resolve(__dirname, "vegam-exterior-emulsion.html"),
        vegamExteriorPrimer: resolve(__dirname, "vegam-exterior-primer.html"),
        vegamInteriorEmulsion: resolve(__dirname, "vegam-interior-emulsion.html"),
        vegamInteriorPrimer: resolve(__dirname, "vegam-interior-primer.html"),
        vegamTextureFine: resolve(__dirname, "vegam-texture-fine.html"),
        vegamTextureRustic: resolve(__dirname, "vegam-texture-rustic.html"),
        vegamWallcarePutty: resolve(__dirname, "vegam-wallcare-putty.html"),
      },
    },
  },
});