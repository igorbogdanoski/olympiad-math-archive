# 🚀 Deployment & Authentication План

**Креирано**: 2 февруари 2026, 01:35 AM  
**Цел**: Да можат колеги да пристапат до платформата + логирање и колаборација

---

## 📊 ТЕКОВЕН СТАТУС

**Сега**: Локален dev server на твојот компјутер
- URL: http://localhost:4321/
- Пристап: Само ти (од твојот компјутер)
- Колеги: **НЕ можат да пристапат** (треба deployment)

---

## 🎯 ЦЕЛ: Јавна платформа со логирање

### Што треба да постигнеме:

1. **Deployment** → Колегите да можат да пристапат (јавен URL)
2. **Authentication** → Логирање со email/password
3. **User roles** → Наставници, администратори, ученици
4. **Collaboration** → Споделување worksheets, коментари
5. **Data persistence** → Зачувување на напредок, worksheets

---

## 🚀 ОПЦИЈА 1: БРЗО DEPLOYMENT (1-2 часа) - ПРЕПОРАКА

### Користење на **Vercel** (бесплатно за MVP)

**Предности**:
- ✅ Бесплатно за почеток
- ✅ Automatic HTTPS
- ✅ Global CDN (брзо од секаде)
- ✅ Automatic deploys од GitHub
- ✅ Нема потреба од сервер

**Чекори**:

#### 1. Креирај Vercel акаунт (5 минути)
```
1. Оди на: https://vercel.com/signup
2. Signup со GitHub акаунт
3. Авторизирај Vercel да пристапи до твоите repos
```

#### 2. Deploy платформата (10 минути)
```bash
# Install Vercel CLI
npm install -g vercel

# Navigate to project
cd C:\Users\pc4all\Documents\matholimpiad\olympiad-math-archive\web

# Deploy
vercel --prod
```

**Што ќе добиеш**:
- Јавен URL: `https://olympiad-math-archive.vercel.app`
- Automatic SSL (HTTPS)
- Automatic updates (секој push на GitHub = нов deploy)

#### 3. Сподели со колегите (1 минута)
```
Пример URL: https://olympiad-math-archive.vercel.app

Колегите ќе можат да пристапат од:
- Македонија: ✅
- Било каде во светот: ✅
- Мобилен телефон: ✅
- Таблет: ✅
```

**Цена**: 🆓 **БЕСПЛАТНО** (до 100GB bandwidth/месец)

---

## 🔐 ОПЦИЈА 2: AUTHENTICATION СИСТЕМ (1 недела развој)

### Што треба да се имплементира:

#### **Phase 5A: Basic Authentication** (3-4 дена)

**Технологија**: Supabase (PostgreSQL + Auth built-in)

**Features**:
```
✓ User registration (email + password)
✓ User login/logout
✓ Password reset
✓ Email verification
✓ Profile management
```

**User roles**:
```typescript
enum UserRole {
  STUDENT = 'student',      // Ученици (browse problems, track progress)
  TEACHER = 'teacher',      // Наставници (+ create worksheets, view tips)
  ADMIN = 'admin'           // Администратори (+ manage users, content)
}
```

**Implementation stack**:
```
Frontend: Astro + Svelte components
Backend: Supabase (PostgreSQL + Row Level Security)
Auth: Supabase Auth (email/password, OAuth)
Session: JWT tokens (secure, stateless)
```

**Database schema** (додаток на постоечка):
```sql
-- Users table (managed by Supabase)
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  email TEXT UNIQUE NOT NULL,
  full_name TEXT,
  role TEXT DEFAULT 'student',
  school TEXT,
  grade INTEGER,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  last_login TIMESTAMPTZ
);

-- User progress (track solved problems)
CREATE TABLE user_progress (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id),
  problem_id TEXT NOT NULL,
  status TEXT DEFAULT 'in_progress', -- in_progress, solved, abandoned
  attempts INTEGER DEFAULT 0,
  hints_used INTEGER DEFAULT 0,
  time_spent_minutes INTEGER,
  solved_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Worksheets ownership (connect worksheets to teachers)
ALTER TABLE worksheets 
ADD COLUMN created_by_user_id UUID REFERENCES users(id);

-- Shared worksheets (collaboration)
CREATE TABLE worksheet_shares (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  worksheet_id UUID REFERENCES worksheets(id),
  shared_by UUID REFERENCES users(id),
  shared_with UUID REFERENCES users(id),
  permission TEXT DEFAULT 'view', -- view, edit
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

**Чекори за имплементација**:

##### День 1: Supabase Setup (4 часа)
```bash
# 1. Create Supabase project
https://supabase.com/dashboard → New Project

# 2. Get credentials
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_ANON_KEY=eyJxxxxx...

# 3. Install Supabase client
cd web
npm install @supabase/supabase-js

# 4. Create Supabase client
# web/src/lib/supabase.ts
import { createClient } from '@supabase/supabase-js'

export const supabase = createClient(
  import.meta.env.PUBLIC_SUPABASE_URL,
  import.meta.env.PUBLIC_SUPABASE_ANON_KEY
)
```

##### День 2-3: Authentication UI (8-10 часа)
```astro
<!-- web/src/pages/login.astro -->
---
import Layout from '../layouts/Layout.astro';
import LoginForm from '../components/auth/LoginForm.svelte';
---
<Layout title="Најави се">
  <LoginForm client:load />
</Layout>

<!-- web/src/components/auth/LoginForm.svelte -->
<script lang="ts">
  import { supabase } from '../../lib/supabase';
  
  let email = '';
  let password = '';
  let error = '';
  
  async function handleLogin() {
    const { data, error: authError } = await supabase.auth.signInWithPassword({
      email,
      password
    });
    
    if (authError) {
      error = authError.message;
    } else {
      window.location.href = '/';
    }
  }
</script>

<form on:submit|preventDefault={handleLogin}>
  <input type="email" bind:value={email} placeholder="Email" />
  <input type="password" bind:value={password} placeholder="Password" />
  <button type="submit">Најави се</button>
  {#if error}<p class="error">{error}</p>{/if}
</form>
```

##### День 4: Protected Routes + Session Management (4 часа)
```typescript
// web/src/middleware/auth.ts
import { supabase } from '../lib/supabase';

export async function requireAuth() {
  const { data: { session } } = await supabase.auth.getSession();
  
  if (!session) {
    return Response.redirect('/login');
  }
  
  return session.user;
}

// Protect worksheet builder
// web/src/pages/teachers/worksheet-builder.astro
---
import { requireAuth } from '../../middleware/auth';
const user = await requireAuth();
if (!user) return; // Redirect handled in middleware
---
```

##### День 5: Testing + Polish (4 часа)
- Test registration flow
- Test login/logout
- Test password reset
- Test protected routes
- UI polish (error messages, loading states)

**ROI**:
- 1 недела развој = трајна infrastructure
- Supabase бесплатен до 50,000 users
- Automatic backup, scaling, security

---

## 🤝 ОПЦИЈА 3: COLLABORATION FEATURES (2 недели развој)

### Phase 5B: Worksheet Sharing & Collaboration

**Features**:

#### 1. Share Worksheets (3 дена)
```typescript
// Teacher creates worksheet
POST /api/worksheets
{
  title: "Геометрија 7 клас - Тест 1",
  template: "test",
  problems: [...],
  created_by: user_id
}

// Teacher shares with colleague
POST /api/worksheets/:id/share
{
  email: "colleague@school.mk",
  permission: "edit" // or "view"
}

// Email notification sent
Subject: "Igor ти сподели worksheet: Геометрија 7 клас - Тест 1"
```

#### 2. Comments & Feedback (3 дена)
```sql
CREATE TABLE worksheet_comments (
  id UUID PRIMARY KEY,
  worksheet_id UUID REFERENCES worksheets(id),
  user_id UUID REFERENCES users(id),
  comment TEXT NOT NULL,
  parent_comment_id UUID REFERENCES worksheet_comments(id), -- for replies
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

**UI**:
```svelte
<!-- Comments section on worksheet page -->
<div class="comments">
  <h3>Коментари (5)</h3>
  
  <div class="comment">
    <img src="avatar.jpg" />
    <div>
      <strong>Марија Петровска</strong>
      <p>Одличен worksheet! Можеби да додадеме уште 2 потешки проблеми?</p>
      <button>Одговори</button>
    </div>
  </div>
  
  <textarea placeholder="Додај коментар..."></textarea>
  <button>Објави</button>
</div>
```

#### 3. Version History (2 дена)
```sql
CREATE TABLE worksheet_versions (
  id UUID PRIMARY KEY,
  worksheet_id UUID REFERENCES worksheets(id),
  version_number INTEGER,
  content JSONB, -- full snapshot
  changed_by UUID REFERENCES users(id),
  change_description TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

**UI**: "See history" button → Timeline view

#### 4. Templates Library (2 дена)
```typescript
// Teacher publishes worksheet as template
POST /api/templates/publish
{
  worksheet_id: "xxx",
  category: "geometry",
  grade_level: 7,
  public: true
}

// Other teachers can use template
GET /api/templates
[
  {
    id: "xxx",
    title: "Геометрија 7 - Триаголници",
    author: "Igor Bogdanoski",
    uses: 23,
    rating: 4.8
  }
]
```

#### 5. Real-time Collaboration (5 дена) - OPTIONAL
```typescript
// WebSocket for live editing (like Google Docs)
import { io } from 'socket.io-client';

const socket = io('wss://api.olympiad-math.mk');

socket.on('worksheet:update', (data) => {
  // Update UI in real-time
  updateWorksheet(data);
});

// When user makes change
socket.emit('worksheet:edit', {
  worksheet_id: 'xxx',
  changes: { ... }
});
```

---

## 💾 ОПЦИЈА 4: DATA PERSISTENCE & PROGRESS TRACKING (1 недела)

### Phase 5C: Student Progress & Analytics

#### 1. Track Solved Problems (2 дена)
```typescript
// Student solves problem
POST /api/progress/solve
{
  problem_id: "2025_mun_g7_3",
  time_spent: 15, // minutes
  hints_used: 2,
  attempts: 3
}

// Get student progress
GET /api/progress/me
{
  total_solved: 45,
  by_subject: {
    geometry: 20,
    algebra: 15,
    number_theory: 7,
    combinatorics: 3
  },
  by_difficulty: {
    easy: 15,
    medium: 25,
    hard: 5
  },
  streak_days: 7, // 7 days in a row
  achievements: [
    { name: "First Problem", icon: "🎯", earned_at: "2026-01-15" },
    { name: "Geometry Master", icon: "📐", earned_at: "2026-01-28" }
  ]
}
```

#### 2. Progress Dashboard (2 дена)
```astro
<!-- web/src/pages/dashboard.astro -->
---
const progress = await fetchUserProgress(user.id);
---

<Layout title="Мој прогрес">
  <div class="stats-grid">
    <div class="stat-card">
      <h3>Решени задачи</h3>
      <div class="value">45</div>
      <div class="change">+5 оваа недела</div>
    </div>
    
    <div class="stat-card">
      <h3>Тековен streak</h3>
      <div class="value">🔥 7 дена</div>
    </div>
    
    <div class="stat-card">
      <h3>БРО покриеност</h3>
      <div class="value">68%</div>
      <div class="progress-bar"></div>
    </div>
  </div>
  
  <div class="chart">
    <h3>Активност низ време</h3>
    <LineChart data={progress.activity} />
  </div>
</Layout>
```

#### 3. Recommendations Engine (3 дена)
```typescript
// AI-powered problem recommendations
GET /api/recommendations
{
  recommended_problems: [
    {
      problem_id: "xxx",
      reason: "Based on your recent geometry progress",
      difficulty: "medium",
      estimated_time: 20
    },
    {
      problem_id: "yyy",
      reason: "You haven't practiced quadratic equations lately",
      difficulty: "easy",
      estimated_time: 10
    }
  ],
  next_bro_standard: {
    code: "MAT-O-G7-T3-S2",
    title: "Квадратни равенки",
    mastery: 0.45, // 45% mastered
    recommended_problems: ["xxx", "yyy", "zzz"]
  }
}
```

---

## 📅 TIMELINE & ROADMAP

### **Неделата 1 (Feb 2-9): DEPLOYMENT + MVP AUTH**

**Ден 1-2 (Feb 2-3)**: 
- ✅ Worksheet Generator Day 2 (finish JavaScript + PDF)
- ✅ GeoGebra Matcher (batch processing)

**Ден 3 (Feb 4)**:
- 🔵 Deploy на Vercel (production URL)
- 🔵 Share со 5 teachers за testing

**Ден 4-7 (Feb 5-9)**:
- 🔵 Supabase setup
- 🔵 Authentication UI (login, register, logout)
- 🔵 Protected routes
- 🔵 Basic user profiles

### **Неделата 2 (Feb 10-16): USER ROLES + PROGRESS TRACKING**

**Ден 1-3 (Feb 10-12)**:
- 🟡 User roles (student, teacher, admin)
- 🟡 Progress tracking (solved problems)
- 🟡 Basic analytics dashboard

**Ден 4-7 (Feb 13-16)**:
- 🟡 Worksheet ownership (created_by)
- 🟡 Save worksheets to database
- 🟡 My Worksheets page (for teachers)

### **Неделата 3 (Feb 17-23): COLLABORATION**

**Ден 1-3 (Feb 17-19)**:
- 🟡 Share worksheets with colleagues
- 🟡 Email notifications
- 🟡 View shared worksheets

**Ден 4-7 (Feb 20-23)**:
- 🟡 Comments on worksheets
- 🟡 Version history
- 🟡 Templates library (publish/use)

### **Неделата 4 (Feb 24-29): POLISH + LAUNCH**

**Ден 1-3 (Feb 24-26)**:
- 🟡 Testing with 20 teachers
- 🟡 Bug fixes
- 🟡 UI polish

**Ден 4-7 (Feb 27-29)**:
- 🟢 Public beta launch
- 🟢 Marketing (social media, teacher groups)
- 🟢 Onboarding materials (video tutorials)

---

## 💰 COSTS & RESOURCES

### **Бесплатни опции (за почеток)**:

| Service | Free Tier | Cost After |
|---------|-----------|------------|
| **Vercel** | Unlimited sites, 100GB bandwidth | $20/месец (Pro) |
| **Supabase** | 50,000 users, 500MB database | $25/месец (Pro) |
| **Cloudflare** | Unlimited bandwidth | Бесплатно |
| **GitHub** | Unlimited repos | Бесплатно |

**Total monthly cost**: 🆓 **$0** (до 50k users) → **$45/месец** (growth)

### **Потребни ресурси**:

**Развој**:
- 1 Full-stack developer (тебе): 40 часа/недела × 4 недели = 160 часа
- (Optional) 1 Designer: 10 часа за UI/UX polish

**Content**:
- Existing: 1100+ problems ✅
- Existing: 391 BRO standards ✅
- Existing: 50 expert tips ✅

---

## 🚀 БРЗО DEPLOYMENT (ДЕНЕС!)

### Да го направиме ова СЕГА (30 минути):

#### Чекор 1: Signup на Vercel (5 минути)
```
1. Оди на: https://vercel.com/signup
2. Click "Continue with GitHub"
3. Авторизирај Vercel
```

#### Чекор 2: Install Vercel CLI (5 минути)
```powershell
npm install -g vercel
```

#### Чекор 3: Deploy (10 минути)
```powershell
cd C:\Users\pc4all\Documents\matholimpiad\olympiad-math-archive\web
vercel login
vercel --prod
```

#### Чекор 4: Share URL (1 минута)
```
Vercel ќе ти даде URL:
https://olympiad-math-archive-xxxx.vercel.app

Сподели со колегите:
"Одете на: https://olympiad-math-archive-xxxx.vercel.app
Кликнете на Math Editor, Curriculum Planner, итн"
```

### Што ќе можат колегите:

✅ **Веднаш (без логирање)**:
- Browse 1100+ problems
- Use Math Editor
- View Curriculum Planner (391 BRO standards)
- View Expert Tips (50)
- Browse Skills, Theorems

❌ **Не можат (треба auth - 1 недела)**:
- Save progress
- Create worksheets
- Share with others
- Track solved problems

---

## 🎯 RECOMMENDATION

### **IMMEDIATE (Денес)**:
1. ✅ Deploy на Vercel (30 мин)
2. ✅ Share URL со 5-10 колеги
3. ✅ Collect feedback (survey)

### **Week 1 (Feb 2-9)**:
4. 🔵 Finish Worksheet Generator + GeoGebra Matcher
5. 🔵 Setup Supabase + Basic Auth
6. 🔵 Protected routes

### **Week 2 (Feb 10-16)**:
7. 🟡 User roles + Progress tracking
8. 🟡 Worksheet ownership
9. 🟡 Analytics dashboard

### **Week 3-4 (Feb 17-29)**:
10. 🟡 Collaboration features
11. 🟡 Polish + Testing
12. 🟢 Public beta launch

---

## 📞 NEXT STEPS

### Дали сакаш да:

**A) Deployираме ДЕНЕС?** (30 минути)
- Install Vercel CLI
- Deploy production site
- Share URL со колегите

**B) Направиме детален план за Auth?** (1 недела)
- Supabase setup
- Login/Register UI
- Protected routes

**C) И двете?** (препорака)
- Прво: Deploy (колегите можат да browsеат)
- Потоа: Auth (follow-up за collaboration)

**Кажи ми што сакаш прво и ќе започнеме!** 🚀

---

**Креирано**: 2 февруари 2026, 01:35 AM  
**Status**: Ready for deployment  
**Blocker**: None (сè е готово)
