/**
 * Worksheet Template Manager
 * Created: February 3, 2026
 * Purpose: Manage worksheet templates and auto-select problems
 */

// API Base URL
const API_BASE = window.location.hostname === 'localhost' 
  ? 'http://localhost:8000/api'
  : '/api';

/**
 * Fetch all available templates from backend
 */
async function fetchTemplates() {
  try {
    const response = await fetch(`${API_BASE}/worksheet/templates`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data.templates;
  } catch (error) {
    console.error('Error fetching templates:', error);
    return null;
  }
}

/**
 * Fetch specific template details
 */
async function fetchTemplateDetails(templateId) {
  try {
    const response = await fetch(`${API_BASE}/worksheet/templates/${templateId}`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching template details:', error);
    return null;
  }
}

/**
 * Auto-select problems based on template
 */
async function selectProblemsFromTemplate(templateId, filters = {}) {
  try {
    const response = await fetch(`${API_BASE}/worksheet/select-problems`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        template_id: templateId,
        ...filters
      })
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Error selecting problems:', error);
    return null;
  }
}

/**
 * Auto-balance problems by difficulty
 * @param {Array} problems - All available problems
 * @param {Object} distribution - Difficulty distribution {easy: 0.3, medium: 0.5, hard: 0.2}
 * @param {Number} count - Total number of problems to select
 */
function autoBalanceProblems(problems, distribution, count) {
  const easyCount = Math.floor(count * distribution.easy);
  const mediumCount = Math.floor(count * distribution.medium);
  const hardCount = count - easyCount - mediumCount;
  
  // Categorize problems by difficulty
  const easy = problems.filter(p => (p.difficulty || 0) <= 2);
  const medium = problems.filter(p => (p.difficulty || 0) === 3);
  const hard = problems.filter(p => (p.difficulty || 0) >= 4);
  
  // Shuffle arrays
  const shuffled = {
    easy: shuffle(easy),
    medium: shuffle(medium),
    hard: shuffle(hard)
  };
  
  // Select problems
  const selected = [
    ...shuffled.easy.slice(0, easyCount),
    ...shuffled.medium.slice(0, mediumCount),
    ...shuffled.hard.slice(0, hardCount)
  ];
  
  return selected;
}

/**
 * Shuffle array (Fisher-Yates algorithm)
 */
function shuffle(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

/**
 * Check БРО coverage
 */
function checkBROCoverage(problems, requiredStandards) {
  const covered = new Set(
    problems
      .map(p => p.bro_standard)
      .filter(Boolean)
  );
  
  const missing = requiredStandards.filter(s => !covered.has(s));
  const coverage = ((requiredStandards.length - missing.length) / requiredStandards.length * 100);
  
  return {
    status: missing.length === 0 ? 'success' : 'warning',
    message: missing.length === 0 
      ? '✓ Сите БРО стандарди покриени'
      : `⚠️ Недостасуваат: ${missing.join(', ')}`,
    coverage: coverage.toFixed(0),
    missing: missing,
    covered: Array.from(covered)
  };
}

/**
 * Filter recently used problems
 */
function filterRecentlyUsed(problems, daysAgo = 30) {
  const recentWorksheets = JSON.parse(localStorage.getItem('recent_worksheets') || '[]');
  const cutoffDate = new Date(Date.now() - daysAgo * 24 * 60 * 60 * 1000);
  
  // Get recently used problem IDs
  const usedIds = new Set();
  recentWorksheets
    .filter(ws => new Date(ws.created_at) > cutoffDate)
    .forEach(ws => ws.problem_ids.forEach(id => usedIds.add(id)));
  
  // Filter out recently used
  const fresh = problems.filter(p => !usedIds.has(p.id));
  
  // If too few fresh problems, include some recent ones
  if (fresh.length < 10) {
    console.warn('Not enough fresh problems, including recently used ones');
    return problems;
  }
  
  return fresh;
}

/**
 * Save worksheet to recent history
 */
function saveToRecentHistory(worksheet) {
  const recent = JSON.parse(localStorage.getItem('recent_worksheets') || '[]');
  recent.unshift({
    id: worksheet.id || `ws_${Date.now()}`,
    title: worksheet.title,
    problem_ids: worksheet.problems.map(p => p.id),
    created_at: new Date().toISOString()
  });
  
  // Keep only last 50 worksheets
  localStorage.setItem('recent_worksheets', JSON.stringify(recent.slice(0, 50)));
}

/**
 * Get difficulty label in Macedonian
 */
function getDifficultyLabel(difficulty) {
  const labels = {
    1: 'Многу лесно',
    2: 'Лесно',
    3: 'Средно',
    4: 'Тешко',
    5: 'Многу тешко'
  };
  return labels[difficulty] || 'Непознато';
}

/**
 * Get difficulty color class
 */
function getDifficultyColor(difficulty) {
  const colors = {
    1: 'difficulty-very-easy',
    2: 'difficulty-easy',
    3: 'difficulty-medium',
    4: 'difficulty-hard',
    5: 'difficulty-very-hard'
  };
  return colors[difficulty] || 'difficulty-medium';
}

/**
 * Auto-assign points based on difficulty
 */
function assignPoints(problem) {
  const pointMap = {
    1: 2,
    2: 3,
    3: 5,
    4: 8,
    5: 12
  };
  return pointMap[problem.difficulty || 3] || 5;
}

/**
 * Calculate total points for worksheet
 */
function calculateTotalPoints(problems) {
  return problems.reduce((sum, p) => sum + (p.points || assignPoints(p)), 0);
}

/**
 * Display template selector UI
 */
async function displayTemplateSelector() {
  const templates = await fetchTemplates();
  if (!templates) {
    console.error('Failed to load templates');
    return;
  }
  
  const container = document.getElementById('template-selector');
  if (!container) return;
  
  container.innerHTML = Object.entries(templates).map(([id, template]) => `
    <div class="template-card" data-template-id="${id}" onclick="selectTemplate('${id}')">
      <div class="template-icon">${template.icon}</div>
      <h3>${template.name}</h3>
      <p class="template-desc">${template.description}</p>
      <div class="template-meta">
        <span class="meta-item">
          <strong>${template.problems}</strong> задачи
        </span>
        ${template.time_limit ? `
          <span class="meta-item">
            <strong>${template.time_limit}</strong> мин
          </span>
        ` : ''}
      </div>
      <div class="template-difficulty">
        <div class="difficulty-bar">
          <div class="bar-segment bar-easy" style="width: ${template.difficulty.easy * 100}%"></div>
          <div class="bar-segment bar-medium" style="width: ${template.difficulty.medium * 100}%"></div>
          <div class="bar-segment bar-hard" style="width: ${template.difficulty.hard * 100}%"></div>
        </div>
        <div class="difficulty-labels">
          <span>${(template.difficulty.easy * 100).toFixed(0)}% лесно</span>
          <span>${(template.difficulty.medium * 100).toFixed(0)}% средно</span>
          <span>${(template.difficulty.hard * 100).toFixed(0)}% тешко</span>
        </div>
      </div>
    </div>
  `).join('');
}

// Export functions for global use
window.worksheetTemplates = {
  fetchTemplates,
  fetchTemplateDetails,
  selectProblemsFromTemplate,
  autoBalanceProblems,
  checkBROCoverage,
  filterRecentlyUsed,
  saveToRecentHistory,
  getDifficultyLabel,
  getDifficultyColor,
  assignPoints,
  calculateTotalPoints,
  displayTemplateSelector
};
