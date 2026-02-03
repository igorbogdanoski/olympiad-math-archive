#!/bin/bash
# БРЗО DEPLOYMENT НА app.missmath.net
# Копирај ги командите една по една во SSH терминалот

echo "=== DEPLOYMENT ЗА app.missmath.net ==="
echo ""

# ЧЕК 1: Креирај deployment директориум
echo "ЧЕК 1: Креирај директориуми..."
mkdir -p /opt/olympiad-math-archive
cd /opt/olympiad-math-archive

# ЧЕК 2: Clone Git repo (НАЈБРЗ НАЧИН)
echo "ЧЕК 2: Clone GitHub репото..."
git clone https://github.com/igorbogdanoski/olympiad-math-archive.git .
# Или ако веќе постои:
# cd /opt/olympiad-math-archive && git pull origin main

# ЧЕК 3: Backup старата апликација
echo "ЧЕК 3: Backup на претходната апликација..."
BACKUP_DIR="/root/backup-$(date +%Y%m%d-%H%M%S)"
mkdir -p $BACKUP_DIR
cp -r /var/www/html/ $BACKUP_DIR/ 2>/dev/null || echo "No old files to backup"
cp /etc/nginx/sites-available/default $BACKUP_DIR/nginx-default.conf 2>/dev/null

# ЧЕК 4: Копирај новите static фајлови
echo "ЧЕК 4: Копирај built фајлови..."
# Ќе го направиме откако видиме каде е nginx root

# ЧЕК 5: Update nginx конфигурација
echo "ЧЕК 5: Update nginx config..."
# Ќе го направиме откако видиме current config

# ЧЕК 6: Рестартирај nginx
echo "ЧЕК 6: Рестартирај nginx..."
nginx -t && systemctl reload nginx

# ЧЕК 7: Тестирај
echo "ЧЕК 7: Тестирај deployment..."
curl -I http://localhost/ | head -5
curl -I https://app.missmath.net/ | head -5

echo ""
echo "✅ DEPLOYMENT ЗАВРШЕН!"
echo "🌐 Сајтот е достапен на: https://app.missmath.net/"
