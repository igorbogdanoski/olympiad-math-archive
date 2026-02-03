# 🎮 Gamification System - Speed Bonus

## Overview

Имплементиран **Kahoot-стил Speed Bonus** систем кој награди брзи одговори и consecutive точни одговори (streak).

## 🚀 Феатури

### 1. ⚡ Speed Tracking

**Frontend** (`web/src/pages/student/quiz.astro`):
- Секое прашање добива `questionStartTime` (timestamp)
- При селекција на одговор, се пресметува `time_spent` во секунди
- Максимален капа: 60 секунди по прашање

**Структура на одговор**:
```javascript
answers[question_id] = {
    option: "A",
    time: 3  // секунди
}
```

### 2. 🎯 Speed Badge (Визуелен Фидбек)

Ако ученик одговори **под 5 секунди**:
- Се појавува "⚡ БРЗО!" badge
- Жолта анимација (`popUp`)
- Се исчезнува по 1 секунда

**CSS**: `.speed-badge` со `@keyframes popUp`

### 3. 🏆 Speed Bonus Formula (Backend)

**Scoring Logic** (`backend/routers/quiz_generator.py`):

```python
# Max points = base_points × 2 (instant answer)
# Min points = base_points × 1 (slow answer)

time_limit_per_q = 30  # Slow threshold
time_factor = 1 - (time_taken / (2 * time_limit_per_q))

earned_points = int(base_points * 2 * time_factor)
```

**Примери**:
- **0 sec** → factor 1.0 → **200% поени**
- **15 sec** → factor 0.75 → **150% поени**
- **30 sec** → factor 0.5 → **100% поени**

### 4. 🔥 Streak System

**Consecutive правила**:
- Секој точен одговор → `current_streak++`
- Погрешен одговор → `streak = 0` (reset)
- Се чува `max_streak` за квизот

**Награди**:
```python
if max_streak >= 5:
    feedback = "🔥 Невероватен Streak: 5!"
    # 300 confetti particles (frontend)

elif max_streak >= 3:
    feedback = "⚡ Одличен Streak: 3!"
    # 200 confetti particles
```

### 5. 🎊 Enhanced Confetti

**Frontend** (`handleSuccess`):
```javascript
if (result.streak >= 5) {
    confetti({ particleCount: 300, spread: 100, startVelocity: 40 });
} else if (result.score > 1000) {
    confetti({ particleCount: 200, spread: 80 });
} else {
    confetti({ particleCount: 150, spread: 70 });
}
```

## 📊 Database Schema

**Submission Document**:
```json
{
    "quiz_id": "...",
    "student_name": "Марко",
    "answers": [
        {
            "problem_id": "abc123",
            "student_answer": "A",
            "is_correct": true,
            "points_earned": 180,
            "time_spent": 3
        }
    ],
    "total_score": 950,
    "max_score": 1000,
    "streak": 5,
    "submitted_at": "2026-02-03T..."
}
```

## 🧪 Testing

**Тест Сценарија**:

### Test 1: Speed Badge Visibility
1. Одговори прво прашање **под 5 секунди**
2. Очекувано: "⚡ БРЗО!" badge се појавува

### Test 2: Score Comparison
1. **Round 1**: Одговори споро (30 sec по прашање)
2. **Round 2**: Одговори брзо (3 sec по прашање)
3. Очекувано: Round 2 има **~2x повисок скор**

### Test 3: Streak Reward
1. Одговори **5 прашања точно** подред
2. Очекувано: "🔥 Невероватен Streak: 5!" + 300 confetti

## 📝 Implementation Details

### Frontend Changes (`quiz.astro`)
- **Lines ~680**: Add `questionStartTime` to data object
- **Lines ~757**: Reset timer in `renderQuestion()`
- **Lines ~790**: Calculate `time_spent` in option click handler
- **Lines ~795**: Show speed badge for fast answers
- **Lines ~870**: Send `time` with each answer in payload
- **Lines ~925**: Enhanced confetti based on streak
- **Lines ~935**: Add `showFloatingBadge()` helper
- **Lines ~615**: Add `.speed-badge` CSS with `popUp` animation

### Backend Changes (`quiz_generator.py`)
- **Lines ~630**: Speed bonus formula implementation
- **Lines ~635**: Streak tracking (`current_streak`, `max_streak`)
- **Lines ~645**: Dynamic `max_possible_score` calculation
- **Lines ~670**: Save `streak` in submission document
- **Lines ~675**: Dynamic feedback with streak info
- **Lines ~680**: Return `streak` in response

## 🎯 Impact

**User Experience**:
- ✅ Immediate visual feedback (badge)
- ✅ Competitive element (speed matters)
- ✅ Streak rewards encourage focus
- ✅ Dynamic scoring (not binary)

**Pedagogical Value**:
- ⏱️ Rewards quick recall (fluency)
- 🧠 Encourages sustained attention (streak)
- 📈 Differentiated scoring (nuanced performance)

**Technical Benefits**:
- 🔌 Works offline (time tracked locally)
- 📱 Lightweight (no extra API calls)
- 🚀 Scalable (no real-time sync needed)

## 🔗 Related Files

- Frontend: `web/src/pages/student/quiz.astro` (+80 lines)
- Backend: `backend/routers/quiz_generator.py` (+60 lines)
- Test Script: `test_gamification.ps1` (new)

## 🚀 Next Steps (Future)

**V2.0 Features** (Not in MVP):
- Live leaderboard (requires WebSockets)
- Combo multipliers (3x, 5x, 10x streaks)
- Power-ups (skip, 50/50, time freeze)
- Badges/Achievements system
- Sound effects for speed/streak

**Current Status**: ✅ Complete (Phase 2 of 3)

---

**Git Commit**:
```bash
git add .
git commit -m "feat: Speed Bonus gamification (Phase 2) - Time tracking, speed badges, streak rewards"
```
