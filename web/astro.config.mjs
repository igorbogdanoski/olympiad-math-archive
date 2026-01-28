import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  output: 'static',
  integrations: [tailwind()],
  vite: {
    preview: {
      allowedHosts: ['app.mismath.net', 'localhost']
    },
    server: {
      allowedHosts: ['app.mismath.net', 'localhost']
    }
  }
});
