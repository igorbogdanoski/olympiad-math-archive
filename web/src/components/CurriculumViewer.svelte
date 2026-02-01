<script>
  import { onMount } from 'svelte';
  import { fade, slide } from 'svelte/transition';

  // State
  let grades = [];
  let activeGrade = "I"; 
  let curriculumData = null;
  let loading = false;
  let generatingActivity = null; 
  let generatedCode = ""; 
  let showCodeModal = false;
  let openThemeIndex = 0; 
  let error = null;

  // API URL (Make sure this matches your backend)
  const API_URL = 'http://127.0.0.1:8000';

  // Fetch available grades on mount
  onMount(async () => {
    try {
      const response = await fetch(`${API_URL}/grades`);
      if (response.ok) {
        const data = await response.json();
        grades = data.grades || [];
        // Sort grades logically if needed, but backend sends them as is for now
      } else {
        console.error("Failed to fetch grades");
      }
    } catch (err) {
      console.error("Backend offline?", err);
      error = "Cannot connect to server.";
    }

    // Load initial grade
    fetchCurriculum(activeGrade);
  });

  // Fetch curriculum for a specific grade
  async function fetchCurriculum(grade) {
    loading = true;
    activeGrade = grade;
    curriculumData = null;
    openThemeIndex = 0;
    
    try {
      const response = await fetch(`${API_URL}/curriculum/${grade}`);
      if (response.ok) {
        curriculumData = await response.json();
      } else {
        console.error("Error fetching curriculum:", await response.text());
        curriculumData = null;
      }
    } catch (error) {
      console.error("Server unavailable:", error);
    } finally {
      loading = false;
    }
  }

  // Generate Lesson with AI
  async function generateLesson(themeIndex, activityIndex) {
    generatingActivity = `${themeIndex}-${activityIndex}`;
    
    const payload = {
      grade: activeGrade,
      themeIndex: themeIndex,
      activityIndex: activityIndex
    };

    try {
      const response = await fetch(`${API_URL}/generate-lesson`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (response.ok) {
        const data = await response.json();
        generatedCode = data.code;
        showCodeModal = true;
      } else {
        alert("Generation Error! Check Backend Console.");
      }
    } catch (error) {
      alert("Server error. Ensure Python backend is running.");
    } finally {
      generatingActivity = null;
    }
  }

  function toggleTheme(index) {
    openThemeIndex = openThemeIndex === index ? null : index;
  }
</script>

<div class="max-w-6xl mx-auto p-4 font-sans text-slate-800">
  
  <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6 mb-8 text-center">
    <h1 class="text-3xl font-extrabold text-slate-800 mb-6 tracking-tight">
      🧬 Наставна Програма & AI Генератор
    </h1>

    {#if error}
      <div class="p-4 bg-red-50 text-red-600 rounded-lg mb-4">
        {error}
      </div>
    {/if}
    
    <div class="space-y-6">
      <div>
        <div class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3">Избери Одделение</div>
        
        {#if grades.length > 0}
          <div class="flex flex-wrap justify-center gap-2">
            {#each grades as grade}
              <button 
                class="px-4 py-2 rounded-lg font-bold text-sm transition-all duration-200 border-2 
                {activeGrade === grade 
                  ? 'bg-blue-600 text-white border-blue-600 scale-105 shadow-md' 
                  : 'bg-white text-gray-600 border-gray-200 hover:border-blue-300 hover:bg-blue-50'}"
                on:click={() => fetchCurriculum(grade)}
              >
                {grade.replace('HighSchool_', 'Средно ')}
              </button>
            {/each}
          </div>
        {:else}
           <p class="text-gray-400 text-sm">Се вчитуваат одделенијата...</p>
        {/if}
      </div>
    </div>
  </div>

  {#if loading}
    <div class="flex flex-col items-center justify-center h-64 opacity-75">
      <div class="w-12 h-12 border-4 border-blue-200 border-t-blue-600 rounded-full animate-spin"></div>
      <p class="mt-4 text-gray-500 font-medium animate-pulse">Вчитување...</p>
    </div>
  
  {:else if curriculumData}
    <div in:fade={{ duration: 300 }} class="space-y-4">
      
      <div class="flex justify-between items-end mb-6 px-2 border-b pb-2">
        <h2 class="text-2xl font-bold text-slate-700">
          Програма за <span class="text-blue-600">
            {activeGrade.startsWith('High') 
              ? activeGrade.replace('HighSchool_', '') + ' година' 
              : activeGrade + ' одделение'}
          </span>
        </h2>
        <span class="text-sm text-gray-400 font-mono hidden md:block">Извор: {curriculumData.source || 'База'}</span>
      </div>

      {#each curriculumData.themes as theme, tIndex}
        <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden transition-all duration-300 hover:shadow-md">
          
          <button 
            class="w-full flex justify-between items-center p-5 text-left bg-gray-50 hover:bg-white transition-colors focus:outline-none"
            on:click={() => toggleTheme(tIndex)}
          >
            <div class="flex items-center gap-4">
              <span class="flex items-center justify-center w-8 h-8 rounded-full bg-blue-100 text-blue-600 font-bold text-sm shrink-0">
                {tIndex + 1}
              </span>
              <h3 class="text-lg font-bold text-slate-800">{theme.title}</h3>
            </div>
            <span class="text-gray-400 text-xl transform transition-transform duration-300 {openThemeIndex === tIndex ? 'rotate-180' : ''}">
              ▼
            </span>
          </button>

          {#if openThemeIndex === tIndex}
            <div transition:slide={{ duration: 300 }} class="p-6 border-t border-gray-100 bg-white">
              <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                
                <div class="space-y-6">
                  {#if theme.objectives && theme.objectives.length > 0}
                    <div class="bg-blue-50 p-4 rounded-lg border border-blue-100">
                      <h4 class="text-xs font-bold text-blue-600 uppercase mb-3">🎯 Цели на учење</h4>
                      <ul class="space-y-2">
                        {#each theme.objectives as obj}
                          <li class="text-sm text-gray-700 flex items-start gap-2"><span class="text-blue-400 mt-1">•</span> {obj}</li>
                        {/each}
                      </ul>
                    </div>
                  {/if}

                  {#if theme.standards && theme.standards.length > 0}
                    <div>
                      <h4 class="text-xs font-bold text-green-600 uppercase mb-3">📏 Стандарди</h4>
                      <ul class="space-y-2 pl-2">
                        {#each theme.standards as std}
                          <li class="text-sm text-gray-600 flex items-start gap-2"><span class="text-green-500 mt-1">✓</span> {std}</li>
                        {/each}
                      </ul>
                    </div>
                  {/if}
                </div>

                <div>
                  <div class="flex items-center justify-between mb-3">
                    <h4 class="text-xs font-bold text-purple-600 uppercase">🎬 Активности</h4>
                    <span class="text-xs text-gray-400 bg-gray-100 px-2 py-1 rounded">AI Генератор</span>
                  </div>
                  <div class="space-y-2 max-h-[500px] overflow-y-auto pr-2 custom-scrollbar">
                    {#each theme.activities as activity, aIndex}
                      <div class="group flex flex-col sm:flex-row sm:items-center justify-between p-3 rounded-lg border border-gray-100 hover:border-purple-300 hover:bg-purple-50 transition-all bg-white gap-3">
                        <p class="text-sm text-gray-700 font-medium leading-snug">{activity}</p>
                        <button 
                          class="shrink-0 flex items-center justify-center gap-2 bg-white text-purple-600 border border-purple-200 hover:bg-purple-600 hover:text-white px-4 py-2 rounded-md text-xs font-bold shadow-sm transition-all w-full sm:w-auto"
                          disabled={generatingActivity !== null}
                          on:click|stopPropagation={() => generateLesson(tIndex, aIndex)}
                        >
                          {#if generatingActivity === `${tIndex}-${aIndex}`}
                            <span>⏳...</span>
                          {:else}
                            <span>▶️ Video</span>
                          {/if}
                        </button>
                      </div>
                    {/each}
                  </div>
                </div>

              </div>
            </div>
          {/if}
        </div>
      {/each}
    </div>
  {:else}
    <div class="text-center py-12 bg-gray-50 rounded-xl border border-dashed border-gray-300">
      <p class="text-gray-500 text-lg">Нема пронајдено податоци за {activeGrade}.</p>
    </div>
  {/if}

  {#if showCodeModal}
    <div class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-sm" transition:fade={{ duration: 200 }}>
      <div class="bg-gray-900 rounded-2xl shadow-2xl w-full max-w-5xl h-[85vh] flex flex-col border border-gray-700 overflow-hidden">
        <div class="flex justify-between items-center p-4 border-b border-gray-700 bg-gray-800">
          <div class="flex items-center gap-3">
            <span class="text-green-400 font-mono text-xl">🐍</span>
            <h3 class="font-bold text-white text-lg">Python / Manim Code</h3>
          </div>
          <button class="text-gray-400 hover:text-white text-2xl" on:click={() => showCodeModal = false}>&times;</button>
        </div>
        <div class="flex-1 overflow-auto p-0 bg-[#1e1e1e]">
          <pre class="text-sm font-mono text-gray-300 p-6 outline-none">{generatedCode}</pre>
        </div>
        <div class="p-4 border-t border-gray-700 bg-gray-800 flex justify-end gap-3">
          <button class="px-5 py-2.5 bg-gray-700 text-gray-200 rounded-lg hover:bg-gray-600 font-medium transition-colors" on:click={() => { navigator.clipboard.writeText(generatedCode); alert('Code copied!'); }}>📋 Копирај</button>
          <button class="px-5 py-2.5 bg-blue-600 hover:bg-blue-500 text-white rounded-lg font-bold shadow-lg" on:click={() => showCodeModal = false}>Затвори</button>
        </div>
      </div>
    </div>
  {/if}
</div>

<style>
  .custom-scrollbar::-webkit-scrollbar { width: 6px; }
  .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
  .custom-scrollbar::-webkit-scrollbar-thumb { background-color: #cbd5e1; border-radius: 20px; }
  .custom-scrollbar::-webkit-scrollbar-thumb:hover { background-color: #94a3b8; }
</style>
