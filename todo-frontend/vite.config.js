import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  // When deploying to GitHub Pages under https://<user>.github.io/mss_final_todo/
  // set the base to the repository name with leading and trailing slashes.
  base: '/mss_final_todo/',
  plugins: [
    vue(),
    vueDevTools(),
    tailwindcss(),
  ],
  server:{
    watch:{
      usePolling:true
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})