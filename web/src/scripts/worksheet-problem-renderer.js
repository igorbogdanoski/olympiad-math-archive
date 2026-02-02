/**
 * Worksheet Problem Renderer
 * Handles fetching and displaying problems in the worksheet builder
 */

class WorksheetProblemRenderer {
  constructor(apiBase = '') {
    this.apiBase = apiBase;
    this.selectedProblems = [];
  }

  /**
   * Fetch problems from API by IDs
   * @param {Array<number>} problemIds - Array of problem IDs
   * @returns {Promise<Array>} Array of problem objects
   */
  async fetchProblems(problemIds) {
    if (!problemIds || problemIds.length === 0) {
      return [];
    }

    try {
      const idsString = problemIds.join(',');
      const response = await fetch(`${this.apiBase}/api/problems?ids=${idsString}`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      return data.problems || [];
    } catch (error) {
      console.error('Error fetching problems:', error);
      throw error;
    }
  }

  /**
   * Fetch a single problem by ID
   * @param {number} problemId - Problem ID
   * @returns {Promise<Object>} Problem object
   */
  async fetchProblem(problemId) {
    try {
      const response = await fetch(`${this.apiBase}/api/problems/${problemId}`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      return await response.json();
    } catch (error) {
      console.error(`Error fetching problem ${problemId}:`, error);
      throw error;
    }
  }

  /**
   * Search problems by query
   * @param {string} query - Search query
   * @param {number} limit - Maximum results
   * @returns {Promise<Array>} Array of problem objects
   */
  async searchProblems(query, limit = 50) {
    try {
      const response = await fetch(
        `${this.apiBase}/api/problems/search?q=${encodeURIComponent(query)}&limit=${limit}`
      );
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      return data.problems || [];
    } catch (error) {
      console.error('Error searching problems:', error);
      throw error;
    }
  }

  /**
   * Render a problem card
   * @param {Object} problem - Problem object
   * @param {number} index - Problem number in worksheet
   * @returns {string} HTML string
   */
  renderProblemCard(problem, index) {
    const difficultyColors = {
      'easy': 'bg-green-100 text-green-800',
      'medium': 'bg-yellow-100 text-yellow-800',
      'hard': 'bg-red-100 text-red-800'
    };

    const difficultyClass = difficultyColors[problem.difficulty] || 'bg-gray-100 text-gray-800';
    const points = problem.points || this.getDefaultPoints(problem.difficulty);

    return `
      <div class="problem-card border border-gray-200 rounded-lg p-4 mb-3 bg-white shadow-sm hover:shadow-md transition-shadow" data-problem-id="${problem.id}">
        <div class="flex items-start gap-3">
          <!-- Drag Handle -->
          <div class="drag-handle cursor-move text-gray-400 hover:text-gray-600 pt-1">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8h16M4 16h16"/>
            </svg>
          </div>

          <!-- Problem Number Badge -->
          <div class="flex-shrink-0">
            <div class="w-8 h-8 rounded-full bg-purple-600 text-white flex items-center justify-center font-bold text-sm">
              ${index}
            </div>
          </div>

          <!-- Problem Content -->
          <div class="flex-1 min-w-0">
            <!-- Problem Title/Header -->
            <div class="flex items-center gap-2 mb-2 flex-wrap">
              <span class="text-xs px-2 py-1 rounded ${difficultyClass}">
                ${this.translateDifficulty(problem.difficulty)}
              </span>
              <span class="text-xs px-2 py-1 rounded bg-blue-100 text-blue-800">
                ${problem.grade || 'N/A'} одделение
              </span>
              <span class="text-xs px-2 py-1 rounded bg-purple-100 text-purple-800">
                ${points} поени
              </span>
            </div>

            <!-- Problem Content (with math rendering) -->
            <div class="problem-content text-sm text-gray-700 mb-2">
              ${this.renderContent(problem.content || problem.title || 'Нема содржина')}
            </div>

            <!-- БРО Standard Tag (if available) -->
            ${problem.primary_skill ? `
              <div class="text-xs text-gray-500 mt-2">
                <span class="font-semibold">БРО:</span> ${problem.primary_skill}
              </div>
            ` : ''}

            <!-- Image (if available) -->
            ${problem.image_url ? `
              <div class="mt-2">
                <img src="${problem.image_url}" alt="Problem illustration" class="max-w-xs rounded border">
              </div>
            ` : ''}
          </div>

          <!-- Remove Button -->
          <button class="remove-problem flex-shrink-0 text-red-500 hover:text-red-700 p-1" 
                  onclick="removeProblem(${problem.id})"
                  title="Отстрани задача">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>
        </div>
      </div>
    `;
  }

  /**
   * Render problem content with math formulas
   * @param {string} content - Raw content with potential LaTeX
   * @returns {string} HTML with rendered math
   */
  renderContent(content) {
    // Replace LaTeX delimiters with KaTeX spans
    // Inline math: $...$
    content = content.replace(/\$([^\$]+)\$/g, (match, formula) => {
      return `<span class="math-inline">${formula}</span>`;
    });

    // Display math: $$...$$
    content = content.replace(/\$\$([^\$]+)\$\$/g, (match, formula) => {
      return `<div class="math-display">${formula}</div>`;
    });

    return content;
  }

  /**
   * Translate difficulty to Macedonian
   * @param {string} difficulty - Difficulty level
   * @returns {string} Translated difficulty
   */
  translateDifficulty(difficulty) {
    const translations = {
      'easy': 'Лесна',
      'medium': 'Средна',
      'hard': 'Тешка'
    };
    return translations[difficulty] || difficulty;
  }

  /**
   * Get default points based on difficulty
   * @param {string} difficulty - Difficulty level
   * @returns {number} Point value
   */
  getDefaultPoints(difficulty) {
    const pointMap = {
      'easy': 2,
      'medium': 3,
      'hard': 5
    };
    return pointMap[difficulty] || 3;
  }

  /**
   * Render all selected problems to a container
   * @param {string} containerId - ID of container element
   * @param {Array} problems - Array of problem objects
   */
  renderProblems(containerId, problems) {
    const container = document.getElementById(containerId);
    if (!container) {
      console.error(`Container #${containerId} not found`);
      return;
    }

    if (!problems || problems.length === 0) {
      container.innerHTML = `
        <div class="text-center py-12 text-gray-500">
          <svg class="w-16 h-16 mx-auto mb-4 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
          </svg>
          <p class="text-lg">Нема избрани задачи</p>
          <p class="text-sm mt-2">Изберете задачи од листата погоре</p>
        </div>
      `;
      return;
    }

    // Render each problem card
    const html = problems.map((problem, idx) => 
      this.renderProblemCard(problem, idx + 1)
    ).join('');

    container.innerHTML = html;

    // Initialize KaTeX rendering after DOM update
    this.renderMathFormulas(container);
  }

  /**
   * Render mathematical formulas using KaTeX
   * @param {HTMLElement} container - Container element with math content
   */
  renderMathFormulas(container) {
    if (typeof renderMathInElement === 'undefined') {
      console.warn('KaTeX auto-render not loaded');
      return;
    }

    try {
      renderMathInElement(container, {
        delimiters: [
          {left: '$$', right: '$$', display: true},
          {left: '$', right: '$', display: false},
          {left: '\\[', right: '\\]', display: true},
          {left: '\\(', right: '\\)', display: false}
        ],
        throwOnError: false
      });
    } catch (error) {
      console.error('KaTeX rendering error:', error);
    }
  }

  /**
   * Calculate statistics for selected problems
   * @param {Array} problems - Array of problem objects
   * @returns {Object} Statistics object
   */
  calculateStats(problems) {
    if (!problems || problems.length === 0) {
      return {
        count: 0,
        totalPoints: 0,
        difficulty: { easy: 0, medium: 0, hard: 0 },
        grades: {},
        broStandards: new Set()
      };
    }

    const stats = {
      count: problems.length,
      totalPoints: 0,
      difficulty: { easy: 0, medium: 0, hard: 0 },
      grades: {},
      broStandards: new Set()
    };

    problems.forEach(problem => {
      // Count points
      stats.totalPoints += problem.points || this.getDefaultPoints(problem.difficulty);

      // Count difficulty
      if (problem.difficulty) {
        stats.difficulty[problem.difficulty] = (stats.difficulty[problem.difficulty] || 0) + 1;
      }

      // Count grades
      if (problem.grade) {
        stats.grades[problem.grade] = (stats.grades[problem.grade] || 0) + 1;
      }

      // Collect БРО standards
      if (problem.primary_skill) {
        stats.broStandards.add(problem.primary_skill);
      }
      if (problem.secondary_skills && Array.isArray(problem.secondary_skills)) {
        problem.secondary_skills.forEach(skill => stats.broStandards.add(skill));
      }
    });

    return stats;
  }
}

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
  module.exports = WorksheetProblemRenderer;
}
