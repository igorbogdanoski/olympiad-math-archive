# PWA Icons

Ова папка треба да содржи икони за PWA (Progressive Web App).

## Потребни икони:

- `icon-72x72.png` - iOS Safari
- `icon-96x96.png` - Android Chrome
- `icon-128x128.png` - Desktop
- `icon-144x144.png` - Windows Tiles
- `icon-152x152.png` - iOS Safari
- `icon-192x192.png` - Android Chrome (standard)
- `icon-384x384.png` - Android Chrome (splash)
- `icon-512x512.png` - Android Chrome (maskable)

## Како да генерираш:

1. Направи master icon (512x512px) со логото на платформата
2. Користи алатка како https://realfavicongenerator.net/ за автоматско генерирање
3. Или користи ImageMagick:
   ```bash
   magick convert icon-512x512.png -resize 144x144 icon-144x144.png
   ```

**ЗАБЕЛЕШКА**: Додади ги вистинските икони пред production deployment!
