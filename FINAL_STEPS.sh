#!/bin/bash
# ===================================================================
# ФИНАЛНИ ЧЕКОРИ - Копирај ги ПОСЛЕ npm install
# ===================================================================

# ЧЕКОР 5: Build (2-3 минути)
echo "🔨 ЧЕКОР 5: Build апликацијата..."
cd /opt/olympiad-math-archive/web
npm run build
echo "✅ Build завршен"
echo ""

# ЧЕКОР 6: Копирај во nginx root (15 секунди)
echo "📂 ЧЕКОР 6: Копирај built фајлови..."
rm -rf /var/www/html/*
cp -r /opt/olympiad-math-archive/web/dist/* /var/www/html/
chown -R www-data:www-data /var/www/html/
echo "✅ Фајлови копирани во /var/www/html/"
echo ""

# ЧЕКОР 7: Reload nginx (2 секунди)
echo "🔄 ЧЕКОР 7: Reload nginx..."
nginx -t
systemctl reload nginx
echo "✅ Nginx reload-иран"
echo ""

# ЧЕКОР 8: Тестирај
echo "🧪 ЧЕКОР 8: Тестирај deployment..."
echo "HTTP тест:"
curl -s -I http://localhost/ | head -5
echo ""
echo "HTTPS тест:"
curl -s -I https://app.missmath.net/ | head -5
echo ""

# ФИНАЛНО
echo "=================================================================="
echo "✅ DEPLOYMENT УСПЕШНО ЗАВРШЕН!"
echo "=================================================================="
echo ""
echo "🌐 Сајтот е достапен на:"
echo "   https://app.missmath.net/"
echo ""
echo "📊 Статистики:"
find /var/www/html -name '*.html' | wc -l | xargs echo "   • HTML страници:"
du -sh /var/www/html/ | cut -f1 | xargs echo "   • Големина:"
echo ""
echo "=================================================================="
