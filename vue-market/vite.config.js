import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import EnvironmentPlugin from 'vite-plugin-environment'


// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    EnvironmentPlugin({baseUrl:'http://127.0.0.1:8000/api/v1/'}, { defineOn: 'import.meta.env' })],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    }
  },
})
