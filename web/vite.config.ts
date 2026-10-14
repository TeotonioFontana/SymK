import { resolve } from 'node:path';
import { defineConfig } from 'vite';

export default defineConfig({
  base: '/symk/',
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        roles: resolve(__dirname, 'roles.html'),
        authority: resolve(__dirname, 'authority.html')
      }
    }
  }
});
