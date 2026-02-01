<script lang="ts">
  export let tip: any;
  export let compact: boolean = false;
  export let showFeedback: boolean = false;

  let isExpanded = false;
  let helpfulClicked = false;
  let notHelpfulClicked = false;

  function toggleExpand() {
    isExpanded = !isExpanded;
  }

  function markHelpful() {
    helpfulClicked = true;
    notHelpfulClicked = false;
    // TODO: Send feedback to backend
    console.log('Marked helpful:', tip.tip_id);
  }

  function markNotHelpful() {
    notHelpfulClicked = true;
    helpfulClicked = false;
    // TODO: Send feedback to backend
    console.log('Marked not helpful:', tip.tip_id);
  }

  function getDifficultyColor(difficulty: string) {
    switch (difficulty) {
      case 'easy':
        return 'bg-green-100 text-green-800';
      case 'medium':
        return 'bg-yellow-100 text-yellow-800';
      case 'hard':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  }

  function getDifficultyLabel(difficulty: string) {
    switch (difficulty) {
      case 'easy':
        return 'Лесно';
      case 'medium':
        return 'Средно';
      case 'hard':
        return 'Тешко';
      default:
        return difficulty;
    }
  }
</script>

<div class="expert-tip-card bg-gradient-to-r from-blue-50 to-indigo-50 rounded-lg shadow-md p-4 mb-4 border-l-4 border-blue-500">
  <!-- Header -->
  <div class="flex items-start justify-between mb-2">
    <div class="flex items-center gap-2 flex-1">
      <span class="text-2xl">💡</span>
      <h3 class="text-lg font-semibold text-gray-900">{tip.title_mk}</h3>
    </div>
    {#if !compact}
      <button
        on:click={toggleExpand}
        class="text-blue-600 hover:text-blue-800 transition-colors ml-2"
        aria-label={isExpanded ? 'Затвори' : 'Прошири'}
      >
        <svg class="w-5 h-5 transform transition-transform {isExpanded ? 'rotate-180' : ''}" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
        </svg>
      </button>
    {/if}
  </div>

  <!-- Metadata Badges -->
  <div class="flex flex-wrap gap-2 mb-3">
    <span class="px-2 py-1 text-xs rounded-full {getDifficultyColor(tip.difficulty)}">
      {getDifficultyLabel(tip.difficulty)}
    </span>
    <span class="px-2 py-1 text-xs rounded-full bg-purple-100 text-purple-800">
      {tip.grade_range[0]}-{tip.grade_range[1]} одд.
    </span>
    {#if tip.subcategory}
      <span class="px-2 py-1 text-xs rounded-full bg-gray-100 text-gray-700">
        {tip.subcategory}
      </span>
    {/if}
  </div>

  <!-- Content -->
  <div class="text-gray-700 mb-3">
    <p class="leading-relaxed">{tip.content_mk}</p>
  </div>

  <!-- Expanded Content -->
  {#if isExpanded || !compact}
    <div class="space-y-3 mt-4 pt-4 border-t border-blue-200">
      <!-- Common Mistakes -->
      {#if tip.common_mistakes && tip.common_mistakes.length > 0}
        <div class="bg-red-50 rounded-lg p-3">
          <h4 class="text-sm font-semibold text-red-900 mb-2 flex items-center gap-2">
            <span>⚠️</span>
            Чести грешки:
          </h4>
          <ul class="text-sm text-red-800 space-y-1">
            {#each tip.common_mistakes as mistake}
              <li class="flex items-start gap-2">
                <span class="text-red-500 mt-0.5">•</span>
                <span>{mistake}</span>
              </li>
            {/each}
          </ul>
        </div>
      {/if}

      <!-- Pro Tip -->
      {#if tip.pro_tip}
        <div class="bg-green-50 rounded-lg p-3">
          <h4 class="text-sm font-semibold text-green-900 mb-2 flex items-center gap-2">
            <span>🎯</span>
            Про совет:
          </h4>
          <p class="text-sm text-green-800">{tip.pro_tip}</p>
        </div>
      {/if}

      <!-- БРО Standards -->
      {#if tip.bro_standards && tip.bro_standards.length > 0}
        <div class="flex flex-wrap gap-1">
          <span class="text-xs text-gray-600 mr-2">БРО:</span>
          {#each tip.bro_standards as standard}
            <span class="px-2 py-0.5 text-xs bg-blue-100 text-blue-700 rounded">
              {standard}
            </span>
          {/each}
        </div>
      {/if}

      <!-- Tags -->
      {#if tip.tags && tip.tags.length > 0}
        <div class="flex flex-wrap gap-1">
          {#each tip.tags as tag}
            <span class="px-2 py-0.5 text-xs bg-gray-200 text-gray-700 rounded">
              #{tag}
            </span>
          {/each}
        </div>
      {/if}
    </div>
  {/if}

  <!-- Feedback Buttons -->
  {#if showFeedback}
    <div class="flex items-center gap-3 mt-4 pt-3 border-t border-blue-200">
      <span class="text-sm text-gray-600">Дали ти помогна овој совет?</span>
      <button
        on:click={markHelpful}
        class="px-3 py-1 text-sm rounded-lg transition-colors {helpfulClicked ? 'bg-green-600 text-white' : 'bg-green-100 text-green-700 hover:bg-green-200'}"
      >
        👍 Да
      </button>
      <button
        on:click={markNotHelpful}
        class="px-3 py-1 text-sm rounded-lg transition-colors {notHelpfulClicked ? 'bg-red-600 text-white' : 'bg-red-100 text-red-700 hover:bg-red-200'}"
      >
        👎 Не
      </button>
      {#if helpfulClicked}
        <span class="text-sm text-green-600 ml-2">✓ Ви благодариме!</span>
      {/if}
    </div>
  {/if}
</div>

<style>
  .expert-tip-card {
    animation: slideIn 0.3s ease-out;
  }

  @keyframes slideIn {
    from {
      opacity: 0;
      transform: translateY(-10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
</style>
