#!/bin/bash
# DEPLOYMENT COMMANDS - Копирај ги една по една во SSH терминалот

echo "=== ЧЕК 1: Најди каде е претходната апликација ==="
docker inspect math_api | grep -A 10 Mounts
ls -la /root/
ls -la /var/www/
find /var/www/ -name "index.html" 2>/dev/null
find /home/ -type d -name "app" 2>/dev/null

echo ""
echo "=== ЧЕК 2: Провери nginx и портови ==="
docker ps -a | grep nginx
netstat -tulpn | grep :80
netstat -tulpn | grep :443
which nginx
nginx -v 2>&1 || echo "Nginx not installed on host"

echo ""
echo "=== ЧЕК 3: Провери app.missmath.net DNS ==="
cat /etc/nginx/sites-available/default 2>/dev/null || echo "No nginx config"
cat /etc/nginx/nginx.conf 2>/dev/null | head -20

echo ""
echo "=== ЧЕК 4: Провери дали има Git repo ==="
find /root/ -name ".git" -type d 2>/dev/null
find /home/ -name ".git" -type d 2>/dev/null
find /var/www/ -name ".git" -type d 2>/dev/null

echo ""
echo "=== ЧЕК 5: Инсталирај docker-compose (брзо) ==="
# Избери една од овие опции:
echo "ОПЦИЈА 1 (препорачана): apt install docker-compose"
echo "ОПЦИЈА 2 (најнова): sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose"
