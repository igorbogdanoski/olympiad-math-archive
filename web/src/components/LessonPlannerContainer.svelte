<script>
  import { onMount } from 'svelte';
  import LessonPlanViewer from './LessonPlanViewer.svelte';
  import { API_BASE_URL } from '../utils/config';

  export let curriculumData;

  let selectedGrade = '';
  let selectedThemeIndex = -1;
  let selectedActivityIndex = -1;
  let isLoading = false;
  let generatedPlan = null;
  let error = null;

  $: grades = curriculumData?.subjects?.mathematics ? Object.keys(curriculumData.subjects.mathematics) : [];
  $: themes = selectedGrade ? curriculumData.subjects.mathematics[selectedGrade].themes : [];
  $: activities = selectedThemeIndex !== -1 ? themes[selectedThemeIndex].activities : [];

  async function generatePlan() {
    if (!selectedGrade || selectedThemeIndex === -1 || selectedActivityIndex === -1) {
      alert('Ве молиме изберете одделение, тема и активност.');
      return;
    }

    isLoading = true;
    error = null;
    generatedPlan = null;

    try {
      const response = await fetch(`${API_BASE_URL}/generate-lesson-plan`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          grade: selectedGrade,
          themeIndex: selectedThemeIndex,
          activityIndex: selectedActivityIndex
        }),
      });

      if (!response.ok) {
        throw new Error('Проблем при комуникација со AI сервисот.');
      }

      const data = await response.json();
      if (data.error) {
        throw new Error(data.error);
      }
      generatedPlan = data;
    } catch (err) {
      console.error(err);
      error = err.message;
    } finally {
      isLoading = false;
    }
  }

  function handleGradeChange() {
    selectedThemeIndex = -1;
    selectedActivityIndex = -1;
  }

  function handleThemeChange() {
    selectedActivityIndex = -1;
  }
</script>

<div class="space-y-8">
  <div class="bg-white dark:bg-slate-900 rounded-3xl p-8 border border-slate-200 dark:border-slate-800 shadow-xl">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <!-- Grade Selection -->
      <div class="space-y-2">
        <label class="block text-sm font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider">Одделение</label>
        <select 
          bind:value={selectedGrade} 
          on:change={handleGradeChange}
          class="w-full p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white focus:ring-2 focus:ring-blue-500 outline-none transition-all"
        >
          <option value="">Избери одделение</option>
          {#each grades as grade}
            <option value={grade}>{grade.replace('grade_', '')}. одделение</option>
          {/each}
        </select>
      </div>

      <!-- Theme Selection -->
      <div class="space-y-2">
        <label class="block text-sm font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider">Тема</label>
        <select 
          bind:value={selectedThemeIndex} 
          on:change={handleThemeChange}
          disabled={!selectedGrade}
          class="w-full p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white focus:ring-2 focus:ring-blue-500 outline-none transition-all disabled:opacity-50"
        >
          <option value={-1}>Избери тема</option>
          {#each themes as theme, i}
            <option value={i}>{theme.name}</option>
          {/each}
        </select>
      </div>

      <!-- Activity Selection -->
      <div class="space-y-2">
        <label class="block text-sm font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider">Активност</label>
        <select 
          bind:value={selectedActivityIndex}
          disabled={selectedThemeIndex === -1}
          class="w-full p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white focus:ring-2 focus:ring-blue-500 outline-none transition-all disabled:opacity-50"
        >
          <option value={-1}>Избери активност</option>
          {#each activities as activity, i}
            <option value={i}>{activity}</option>
          {/each}
        </select>
      </div>
    </div>

    <div class="mt-8 flex justify-center">
      <button 
        on:click={generatePlan}
        disabled={isLoading || selectedActivityIndex === -1}
        class="inline-flex items-center gap-3 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-black py-4 px-10 rounded-2xl transition-all shadow-lg shadow-blue-200 dark:shadow-none disabled:opacity-50 disabled:cursor-not-allowed hover:-translate-y-1"
      >
        {#if isLoading}
          <div class="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin"></div>
          <span>Генерирање...</span>
        {:else}
          <span>✨ Создај Сценарио</span>
        {/if}
      </button>
    </div>
  </div>

  {#if error}
    <div class="p-6 bg-red-50 border border-red-100 rounded-2xl text-red-600 font-medium text-center">
      ⚠️ {error}
    </div>
  {/if}

  {#if generatedPlan}
    <div class="mt-12 animate-in fade-in slide-in-from-bottom-8 duration-700">
      <LessonPlanViewer plan={generatedPlan} onClose={() => generatedPlan = null} />
    </div>
  {/if}
</div>
