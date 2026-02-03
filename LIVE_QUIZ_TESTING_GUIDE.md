# 🚀 LIVE QUIZ СИСТЕМ - Упатство за Тестирање

## 📋 Што е имплементирано?

### Backend API (quiz_generator.py)
✅ **6 нови endpoints**:
- `POST /api/quiz-generator/live/create` - Креира live quiz со access code
- `POST /api/quiz-generator/live/join` - Ученик се приклучува во лоби
- `GET /api/quiz-generator/live/access/{code}` - Земи quiz (БЕЗ одговори!)
- `POST /api/quiz-generator/live/submit` - Автоматско оценување
- `GET /api/quiz-generator/live/{quiz_id}/stats` - Real-time статистика

### Frontend Pages
✅ **Student Portal**: `/student/quiz`
- Mobile-first дизајн
- Внес на код → Име → Квиз → Резултати
- Timer со auto-submit
- Конфети анимација

✅ **Teacher Dashboard**: `/teachers/live-quiz?id=QUIZ_ID`
- Live мониторинг (polling на 3 sec)
- QR код за лесен пристап
- Картички со статуси (работи/завршил)
- Автоматски update кога ученик предава

---

## 🧪 E2E Тест (Чекор по Чекор)

### Подготовка

**1. Стартувај Backend:**
```powershell
cd backend
uvicorn main:app --reload
```
Очекувано: `INFO: Uvicorn running on http://127.0.0.1:8000`

**2. Стартувај Frontend:**
```powershell
cd web
npm run dev
```
Очекувано: `Local: http://localhost:4321`

---

### Автоматски Тест

**3. Пушти ја скриптата:**
```powershell
.\test_live_quiz.ps1
```

**Што прави скриптата:**
- ✅ Креира live quiz преку API
- ✅ Генерира 6-значен код (пр. `XK92A7`)
- ✅ Ги копира Quiz ID и Access Code
- ✅ Отвора Teacher Dashboard и Student Portal

---

### Рачно Тестирање

**4. Teacher Dashboard:**
- Отвори: `http://localhost:4321/teachers/live-quiz?id=QUIZ_ID`
- Требаш да го видиш:
  - Access кодот (голем, син текст)
  - QR код
  - Статистика: 0 Приклучени, 0 Завршени

**5. Student Portal (Телефон или друг Tab):**
- Отвори: `http://localhost:4321/student/quiz`
- Внеси код: `XK92A7` (или твојот код)
- Внеси име: `Тест Ученик`
- Кликни **"✍️ ЗАПОЧНИ КВИЗ"**

**6. Гледај го Teacher Dashboard:**
- На секои 3 секунди се освежува
- Требаш да видиш картичка:
  ```
  📛 Тест Ученик
  ✍️ РАБОТИ...
  ```

**7. Реши го квизот:**
- Селектирај одговори (1 по 1)
- Кликни **"🏁 Предај Тест"**

**8. Резултати:**
- **Student Portal**: Ќе видиш score + конфети 🎉
- **Teacher Dashboard**: Картичката станува ЗЕЛЕНА со поени!

---

## 🔐 Безбедност

### Што е заштитено?

1. **API Response Sanitization**
   - `/live/access/{code}` НЕ ги враќа `correct_answer` полињата
   - Дури и со DevTools → Network tab, не може да се видат решенијата

2. **Timer Enforcement**
   - Ако времето истече → автоматски submit
   - Backend не верува на client-side време

3. **Access Code Validation**
   - 6-значен код (букви + броеви)
   - Проверка за колизии при генерирање

---

## 🐛 Debugging

### Проблем: "Невалиден код"
**Причина**: Quiz не постои во база  
**Решение**: Провери дали `test_live_quiz.ps1` успешно креираше quiz

### Проблем: "Нема пронајдено задачи"
**Причина**: Базата нема problems за тие БРО кодови  
**Решение**: Промени ги `bro_codes` во скриптата на валидни вредности од твојата база

### Проблем: Student картичката не се појавува
**Причина**: Polling не работи (CORS грешка?)  
**Решение**: 
- Провери Browser Console за грешки
- Осигурај се дека backend има CORS middleware

### Проблем: Submission не работи
**Причина**: Auto-grading алгоритам не ги препознава одговорите  
**Решение**: Провери дали `correct_answer` во problems е валиден стринг

---

## 📊 Следни Чекори (Post-MVP)

### Фичери за додавање:
- [ ] Close quiz функција (status = "closed")
- [ ] Export резултати (PDF/Excel)
- [ ] Анти-чит детекција (tab switching tracking)
- [ ] Persistent state (Redis за live sessions)
- [ ] Push notifications (WebSocket наместо polling)
- [ ] Retake механизам (дозволи ученик да го повтори)

### Performance оптимизации:
- [ ] Cache quiz data (не повторувај DB query за секој student)
- [ ] Batch updates (collect submissions, update на 1 sec)
- [ ] CDN за QR кодови

---

## 📝 Напомени

### За Production Deploy:
1. Смени `API_BASE` во frontend кодот на production URL
2. Додај rate limiting (не повеќе од 10 requests/sec per IP)
3. Зачувај submissions во archive collection (не ги бриши!)
4. Додај teacher authentication (middleware check)

### За Mobile Testing:
- На иста Wi-Fi мрежа, користи IP адреса:
  - Backend: `http://192.168.1.X:8000`
  - Frontend: `http://192.168.1.X:4321`
- Алтернатива: Користи ngrok за tunneling

---

## ✅ Checklist

Пред да го прогласиш за "COMPLETE":

- [ ] Backend imports work (no errors)
- [ ] Student може да влезе со код
- [ ] Teacher dashboard го гледа студентот во лоби
- [ ] Timer одбројува правилно
- [ ] Submit работи и враќа резултати
- [ ] Teacher dashboard се update-ува со score
- [ ] QR код се генерира
- [ ] Confetti animation работи

---

🎉 **Готово! Имаш функционален Live Quiz систем.**

За прашања: провери ги `console.log` во browser или API response во Network tab.
