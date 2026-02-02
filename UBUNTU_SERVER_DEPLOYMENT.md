# 🚀 Deployment на Ubuntu Сервер со Docker
**Сервер**: 76.13.129.9 (Ubuntu + Docker)  
**Дата**: 2 февруари 2026

---

## 📋 ТЕКОВНА СОСТОЈБА

**Што имаш**:
- ✅ Ubuntu сервер: 76.13.129.9
- ✅ Docker инсталиран
- ✅ Платформа локално развиена (1318 pages)
- ✅ PostgreSQL schema готова (worksheets табели)

**Што треба да deployираме**:
1. Frontend (Astro static site) → Nginx
2. Backend API (Node.js/Express) → Docker container
3. PostgreSQL database → Docker container
4. Redis Queue → Docker container
5. SSL сертификат → Let's Encrypt (HTTPS)

---

## 🐳 DOCKER COMPOSE АРХИТЕКТУРА

### Сервиси што ќе работат:

```yaml
services:
  1. nginx         - Web server + reverse proxy
  2. frontend      - Astro static files (served by nginx)
  3. backend       - Node.js API (Express)
  4. postgres      - PostgreSQL database
  5. redis         - Redis queue (Manim jobs)
  6. manim-worker  - Background job processor
```

### Мрежна архитектура:

```
Internet (port 80/443)
    ↓
[Nginx] → SSL termination
    ↓
    ├→ /            → Frontend (Astro static files)
    ├→ /api/*       → Backend (Node.js API)
    └→ /ws/*        → WebSocket (real-time updates)
    
Backend
    ↓
    ├→ PostgreSQL (port 5432)
    ├→ Redis (port 6379)
    └→ Manim Worker
```

---

## 📦 DEPLOYMENT ПЛАН (1-2 часа)

### Чекор 1: Креирај Docker Compose конфигурација (30 минути)

**Локација**: `docker-compose.prod.yml`

```yaml
version: '3.8'

services:
  # PostgreSQL Database
  postgres:
    image: postgres:16-alpine
    container_name: math_archive_db
    restart: always
    environment:
      POSTGRES_DB: math_archive
      POSTGRES_USER: mathuser
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./backend/database/worksheets_schema.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"
    networks:
      - app_network

  # Redis Queue
  redis:
    image: redis:7-alpine
    container_name: math_archive_redis
    restart: always
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"
    networks:
      - app_network

  # Backend API
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: math_archive_api
    restart: always
    environment:
      NODE_ENV: production
      PORT: 3000
      DATABASE_URL: postgresql://mathuser:${DB_PASSWORD}@postgres:5432/math_archive
      REDIS_URL: redis://redis:6379
      JWT_SECRET: ${JWT_SECRET}
      GEMINI_API_KEY: ${GEMINI_API_KEY}
    depends_on:
      - postgres
      - redis
    ports:
      - "3000:3000"
    networks:
      - app_network

  # Manim Worker (background jobs)
  manim-worker:
    build:
      context: ./backend/manim-worker
      dockerfile: Dockerfile
    container_name: math_archive_manim
    restart: always
    environment:
      REDIS_URL: redis://redis:6379
    depends_on:
      - redis
    volumes:
      - manim_output:/app/output
    networks:
      - app_network

  # Nginx (web server + reverse proxy)
  nginx:
    image: nginx:alpine
    container_name: math_archive_nginx
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./web/dist:/usr/share/nginx/html:ro
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/ssl:/etc/nginx/ssl:ro
      - manim_output:/usr/share/nginx/html/videos:ro
    depends_on:
      - backend
    networks:
      - app_network

volumes:
  postgres_data:
  redis_data:
  manim_output:

networks:
  app_network:
    driver: bridge
```

---

### Чекор 2: Креирај Nginx конфигурација (15 минути)

**Локација**: `nginx/nginx.conf`

```nginx
user nginx;
worker_processes auto;

events {
    worker_connections 1024;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # Logging
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    # Performance
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;

    # Rate limiting (prevent abuse)
    limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;
    limit_req_zone $binary_remote_addr zone=general_limit:10m rate=100r/s;

    # Upstream backend
    upstream backend_api {
        server backend:3000;
    }

    # HTTP → HTTPS redirect
    server {
        listen 80;
        server_name 76.13.129.9 olympiad-math.mk www.olympiad-math.mk;

        # Let's Encrypt challenge
        location /.well-known/acme-challenge/ {
            root /var/www/certbot;
        }

        # Redirect to HTTPS
        location / {
            return 301 https://$host$request_uri;
        }
    }

    # HTTPS server
    server {
        listen 443 ssl http2;
        server_name 76.13.129.9 olympiad-math.mk www.olympiad-math.mk;

        # SSL configuration
        ssl_certificate /etc/nginx/ssl/fullchain.pem;
        ssl_certificate_key /etc/nginx/ssl/privkey.pem;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers HIGH:!aNULL:!MD5;

        # Security headers
        add_header X-Frame-Options "SAMEORIGIN" always;
        add_header X-Content-Type-Options "nosniff" always;
        add_header X-XSS-Protection "1; mode=block" always;
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

        # Frontend (Astro static files)
        location / {
            root /usr/share/nginx/html;
            try_files $uri $uri/ /index.html;
            limit_req zone=general_limit burst=20;

            # Cache static assets
            location ~* \.(jpg|jpeg|png|gif|ico|css|js|svg|woff|woff2|ttf)$ {
                expires 1y;
                add_header Cache-Control "public, immutable";
            }
        }

        # Backend API
        location /api/ {
            proxy_pass http://backend_api/;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_cache_bypass $http_upgrade;
            
            # Rate limiting for API
            limit_req zone=api_limit burst=20 nodelay;
        }

        # WebSocket (for Redis Queue real-time updates)
        location /ws/ {
            proxy_pass http://backend_api/ws/;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "Upgrade";
            proxy_set_header Host $host;
            proxy_read_timeout 86400;
        }

        # Manim videos
        location /videos/ {
            alias /usr/share/nginx/html/videos/;
            expires 1y;
            add_header Cache-Control "public, immutable";
        }
    }
}
```

---

### Чекор 3: Креирај Backend Dockerfile (10 минути)

**Локација**: `backend/Dockerfile`

```dockerfile
FROM node:20-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --only=production

# Copy application code
COPY . .

# Build TypeScript (if using TS)
# RUN npm run build

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node -e "require('http').get('http://localhost:3000/health', (r) => {process.exit(r.statusCode === 200 ? 0 : 1)})"

# Start server
CMD ["node", "index.js"]
```

---

### Чекор 4: Креирај .env фајл (5 минути)

**Локација**: `.env.production`

```bash
# Database
DB_PASSWORD=your_secure_password_here_change_this_123

# JWT Secret (for authentication)
JWT_SECRET=your_jwt_secret_key_change_this_456

# Gemini API (for GeoGebra matcher)
GEMINI_API_KEY=your_gemini_api_key

# Server
SERVER_URL=https://76.13.129.9
# or
# SERVER_URL=https://olympiad-math.mk (if you have domain)

# Email (for notifications - optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_app_password
```

**⚠️ ВАЖНО**: Промени ги сите `your_*` вредности!

---

### Чекор 5: Build Frontend (10 минути)

```bash
cd C:\Users\pc4all\Documents\matholimpiad\olympiad-math-archive\web

# Build production site
npm run build

# Резултат: web/dist/ (1318 pages)
```

---

### Чекор 6: Copy фајлови на сервер (15 минути)

**Од твојот Windows компјутер**:

```powershell
# Use SCP to copy files to server
scp -r web/dist root@76.13.129.9:/opt/math-archive/web/
scp docker-compose.prod.yml root@76.13.129.9:/opt/math-archive/
scp -r nginx root@76.13.129.9:/opt/math-archive/
scp -r backend root@76.13.129.9:/opt/math-archive/
scp .env.production root@76.13.129.9:/opt/math-archive/.env
```

**Или со rsync** (побрзо):

```powershell
rsync -avz --progress web/dist/ root@76.13.129.9:/opt/math-archive/web/dist/
rsync -avz --progress docker-compose.prod.yml root@76.13.129.9:/opt/math-archive/
rsync -avz --progress nginx/ root@76.13.129.9:/opt/math-archive/nginx/
rsync -avz --progress backend/ root@76.13.129.9:/opt/math-archive/backend/
```

---

### Чекор 7: SSH на сервер и deploy (20 минути)

```bash
# SSH to server
ssh root@76.13.129.9

# Navigate to project
cd /opt/math-archive

# Pull latest code (if using Git)
git pull origin production-clean-v2

# Start services
docker-compose -f docker-compose.prod.yml up -d

# Check status
docker-compose -f docker-compose.prod.yml ps

# View logs
docker-compose -f docker-compose.prod.yml logs -f

# Initialize database (first time only)
docker-compose -f docker-compose.prod.yml exec postgres psql -U mathuser -d math_archive -f /docker-entrypoint-initdb.d/init.sql
```

---

### Чекор 8: SSL сертификат - Let's Encrypt (15 минути)

```bash
# On server
ssh root@76.13.129.9

# Install certbot
apt update
apt install -y certbot python3-certbot-nginx

# Get SSL certificate (if you have domain)
certbot --nginx -d olympiad-math.mk -d www.olympiad-math.mk

# Or for IP only (self-signed)
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /opt/math-archive/nginx/ssl/privkey.pem \
  -out /opt/math-archive/nginx/ssl/fullchain.pem \
  -subj "/CN=76.13.129.9"

# Restart nginx
docker-compose -f docker-compose.prod.yml restart nginx
```

---

## 🔥 БРЗО DEPLOYMENT (15 минути) - Тест верзија

Ако сакаш **брзо да тестираш**, без Docker Compose:

```bash
# SSH to server
ssh root@76.13.129.9

# Install Nginx (if not installed)
apt update && apt install -y nginx

# Copy built files
mkdir -p /var/www/math-archive
# (upload web/dist/ content here via SCP)

# Create simple Nginx config
cat > /etc/nginx/sites-available/math-archive << 'EOF'
server {
    listen 80;
    server_name 76.13.129.9;
    
    root /var/www/math-archive;
    index index.html;
    
    location / {
        try_files $uri $uri/ /index.html;
    }
}
EOF

# Enable site
ln -s /etc/nginx/sites-available/math-archive /etc/nginx/sites-enabled/
nginx -t
systemctl reload nginx

# Open firewall
ufw allow 80/tcp
ufw allow 443/tcp
```

**Резултат**: http://76.13.129.9/ (достапно за колегите)

---

## 📊 DEPLOYMENT CHECKLIST

### Pre-deployment:
- [ ] Build frontend (`npm run build` → web/dist/)
- [ ] Test locally (`npm run preview`)
- [ ] Update `.env.production` (DB password, JWT secret)
- [ ] Review nginx config (ports, domains)

### Deployment:
- [ ] Copy files to server (SCP/rsync)
- [ ] SSH to server
- [ ] Run `docker-compose up -d`
- [ ] Check logs (`docker-compose logs`)
- [ ] Initialize database (worksheets schema)
- [ ] Get SSL certificate (Let's Encrypt)

### Post-deployment:
- [ ] Test homepage: http://76.13.129.9/
- [ ] Test Math Editor: http://76.13.129.9/math-editor-demo
- [ ] Test Curriculum: http://76.13.129.9/curriculum-planner
- [ ] Test API: http://76.13.129.9/api/health
- [ ] Monitor logs: `docker-compose logs -f`
- [ ] Setup backups (PostgreSQL, Redis)

### Security:
- [ ] Change default passwords
- [ ] Setup firewall (ufw)
- [ ] Enable SSL (HTTPS)
- [ ] Configure rate limiting
- [ ] Setup fail2ban (prevent brute force)
- [ ] Regular security updates (`apt update && apt upgrade`)

---

## 🌐 ПОСЛЕ DEPLOYMENT

### Колегите ќе можат да пристапат:

**URL (IP адреса)**:
```
http://76.13.129.9/
```

**Или со domain** (ако имаш):
```
https://olympiad-math.mk/
```

### Што ќе можат да прават (без auth):
- ✅ Browse 1100+ задачи
- ✅ Use Math Editor
- ✅ View Curriculum Planner
- ✅ View Expert Tips
- ✅ Browse Skills, Theorems

### Што треба за логирање (следна фаза):
- 🔵 Supabase setup (или PostgreSQL auth)
- 🔵 Login/Register UI
- 🔵 JWT tokens
- 🔵 Protected routes

---

## 🚀 IMMEDIATE ACTION PLAN

### Опција A: Docker Compose (Full Production) - 1-2 часа
1. Креирај `docker-compose.prod.yml`
2. Креирај `nginx/nginx.conf`
3. Креирај `backend/Dockerfile`
4. Build frontend (`npm run build`)
5. Copy на сервер (SCP)
6. SSH + `docker-compose up -d`
7. Test http://76.13.129.9/

### Опција B: Simple Nginx (Quick Test) - 15 минути
1. Build frontend (`npm run build`)
2. SCP web/dist/ на сервер
3. Configure Nginx
4. Test http://76.13.129.9/

**Која опција сакаш да ја направиме прво?**

---

## 📝 СЛЕДНИ ЧЕКОРИ

Кажи ми:

1. **Дали имаш SSH пристап до серверот?** (root@76.13.129.9)
2. **Дали е веќе инсталиран Docker?** (`docker --version`)
3. **Дали имаш domain** (olympiad-math.mk) или користиме IP (76.13.129.9)?
4. **Дали сакаш Full Production (Docker Compose) или Quick Test (Nginx only)?**

Ќе ти помогнам чекор-по-чекор! 🚀
