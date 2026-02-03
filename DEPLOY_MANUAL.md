# 🚀 MANUAL DEPLOYMENT - app.mismath.net

## Брзи Чекори (5 минути)

### 1️⃣ SSH Login
```bash
ssh root@76.13.129.9
# Password: H0mer!Simpson
```

### 2️⃣ Update Code
```bash
cd /root/olympiad-math-archive
git pull origin production-clean-v2
```

### 3️⃣ Update Backend (копирај нови фајлови)
```bash
cp -r /root/olympiad-math-archive/backend/* /root/backend_build/
```

### 4️⃣ Restart Backend
```bash
pkill -f uvicorn
cd /root/backend_build
nohup /root/backend_build/venv/bin/python3.12 -m uvicorn app.main:app --host 0.0.0.0 --port 8000 > /tmp/backend.log 2>&1 &
```

### 5️⃣ Check Backend
```bash
sleep 2
curl http://localhost:8000/health
# Треба да врати: {"status":"healthy"}
```

### 6️⃣ Build Frontend (ако треба)
```bash
cd /root/olympiad-math-archive/web
npm run build
```

---

## ✅ Што Ќе Добиеш

**NEW FEATURES на app.mismath.net:**
- 🔊 Sound effects (click, success, streak)
- 🎮 Floating points animation
- 🔥 Live streak indicator
- ⚡ Speed bonus system
- 🛡️ Anti-cheat (server timestamps)
- ⚙️ Database optimized (7 indexes)

---

## 🧪 ТЕСТ

1. **Отвори:** https://app.mismath.net/students/quiz
2. **Влез со код:** TEST123 (или креирај нов quiz)
3. **Тест features:**
   - Кликни одговор → чуј звук 🔊
   - Одговори брзо → види "+950 поени" 💰
   - 3+ правилни → види 🔥 streak

---

## 📊 Logs (ако има проблем)

```bash
# Backend log
tail -f /tmp/backend.log

# Check if running
ps aux | grep uvicorn

# Check port 8000
netstat -tuln | grep 8000
```
