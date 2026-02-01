<script>
  import { API_BASE_URL } from '../utils/config';
  import PresentationViewer from './PresentationViewer.svelte';

  export let plan = null;
  export let onClose = () => {};

  let isGeneratingPresentation = false;
  let presentationHtml = null;
  let isGeneratingVideo = false;
  let videoUrl = null;
  let isGeneratingWorksheet = false;
  let worksheetHtml = null;

  async function generatePresentation() {
    isGeneratingPresentation = true;
    try {
      const response = await fetch(`${API_BASE_URL}/generate-presentation`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ plan })
      });
      const data = await response.json();
      presentationHtml = data.html;
    } catch (err) {
      console.error('Error generating presentation:', err);
      alert('Грешка при генерирање на презентацијата.');
    } finally {
      isGeneratingPresentation = false;
    }
  }

  async function generateVideo() {
    isGeneratingVideo = true;
    videoUrl = null;
    try {
      const response = await fetch(`${API_BASE_URL}/generate-manim`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          grade: plan.grade || 'Unknown', 
          topic: plan.title,
          activity: plan.core_activity.description
        })
      });
      const data = await response.json();
      if (data.video_url) {
        videoUrl = data.video_url;
      }
    } catch (err) {
      console.error('Error generating video:', err);
      alert('Грешка при генерирање на видеото. Проверете дали Manim е инсталиран на серверот.');
    } finally {
      isGeneratingVideo = false;
    }
  }

  async function generateWorksheet(teacherMode = false) {
    if (!plan.standard_code) {
      alert('Овој дел нема специфичен код за стандард. Проверете ја наставната програма.');
      return;
    }
    isGeneratingWorksheet = true;
    try {
      const response = await fetch(`${API_BASE_URL}/generate-worksheet`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          standardCode: plan.standard_code,
          teacherMode: teacherMode
        })
      });
      const data = await response.json();
      worksheetHtml = data.html;
      
      const blob = new Blob([worksheetHtml], { type: 'text/html' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `Worksheet_${teacherMode ? 'Teacher' : 'Student'}_${plan.standard_code}.html`;
      a.click();
      URL.revokeObjectURL(url);
      
    } catch (err) {
      console.error('Error generating worksheet:', err);
      alert('Грешка при генерирање на работниот лист.');
    } finally {
      isGeneratingWorksheet = false;
    }
  }

  function printPlan() {
    window.print();
  }
</script>

{#if presentationHtml}
  <PresentationViewer html={presentationHtml} onClose={() => presentationHtml = null} />
{/if}

<div class="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-slate-900/90 backdrop-blur-md no-print">
  <div class="bg-white rounded-[2.5rem] shadow-2xl w-full max-w-4xl h-[90vh] flex flex-col overflow-hidden border border-slate-200">
    
    <!-- Header -->
    <div class="flex justify-between items-center p-8 border-b border-slate-100 bg-slate-50">
      <div class="flex items-center gap-4">
        <div class="w-12 h-12 bg-indigo-600 rounded-2xl flex items-center justify-center text-2xl shadow-lg shadow-indigo-200">
          📋
        </div>
        <div>
          <h3 class="font-black text-slate-900 text-2xl">{plan?.title || 'Сценарио за час'}</h3>
          <p class="text-slate-500 text-xs font-bold uppercase tracking-widest">Генерирано со AI Асистент</p>
        </div>
      </div>
      <div class="flex items-center gap-3">
        <button 
          on:click={generatePresentation}
          disabled={isGeneratingPresentation}
          class="px-6 py-3 bg-orange-500 text-white rounded-xl font-bold text-sm hover:bg-orange-600 transition-all flex items-center gap-2 shadow-lg shadow-orange-200 disabled:opacity-50"
        >
          <span>{isGeneratingPresentation ? 'Се генерира...' : 'Креирај Презентација'}</span> 📊
        </button>
        <div class="flex items-center bg-emerald-600 rounded-xl shadow-lg shadow-emerald-200 overflow-hidden">
          <button 
            on:click={() => generateWorksheet(false)}
            disabled={isGeneratingWorksheet}
            class="px-5 py-3 text-white font-bold text-sm hover:bg-emerald-700 transition-all flex items-center gap-2 border-r border-emerald-500/50 disabled:opacity-50"
          >
            <span>{isGeneratingWorksheet ? '...' : 'Наставен Лист'}</span> 📝
          </button>
          <button 
            on:click={() => generateWorksheet(true)}
            disabled={isGeneratingWorksheet}
            title="Верзија со решенија"
            class="px-4 py-3 text-white font-bold text-sm hover:bg-emerald-700 transition-all disabled:opacity-50"
          >
            🔑
          </button>
        </div>
        <button 
          on:click={printPlan}
          class="px-6 py-3 bg-slate-900 text-white rounded-xl font-bold text-sm hover:bg-slate-800 transition-all flex items-center gap-2"
        >
          <span>Print</span> 🖨️
        </button>
        <button 
          class="w-12 h-12 flex items-center justify-center rounded-xl hover:bg-slate-200 text-slate-400 hover:text-slate-900 transition-all text-2xl" 
          on:click={onClose}
        >
          &times;
        </button>
      </div>
    </div>

    <!-- Content -->
    <div class="flex-1 overflow-y-auto p-10 space-y-12 printable-area">
      
      <!-- Introduction Section -->
      <section class="space-y-4">
        <div class="flex items-center gap-3 text-indigo-600">
          <span class="text-xl font-black">01</span>
          <h4 class="font-black uppercase tracking-widest text-sm">Вовед и Мотивација ({plan?.intro?.duration})</h4>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="p-6 rounded-3xl bg-indigo-50 border border-indigo-100">
            <h5 class="font-bold text-indigo-900 mb-2">Кука (Hook)</h5>
            <p class="text-slate-700 leading-relaxed italic">"{plan?.intro?.hook}"</p>
          </div>
          <div class="p-6 rounded-3xl bg-slate-50 border border-slate-100">
            <h5 class="font-bold text-slate-900 mb-2">Контекст</h5>
            <p class="text-slate-600 leading-relaxed">{plan?.intro?.context}</p>
          </div>
        </div>
      </section>

      <!-- Macedonian ERR Scenario Section -->
      {#if plan?.macedonianScenario}
      <section class="space-y-4">
        <div class="flex items-center gap-3 text-orange-600">
          <span class="text-xl font-black">02</span>
          <h4 class="font-black uppercase tracking-widest text-sm">Сценарио за час (ERR Рамка)</h4>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="p-6 rounded-3xl bg-orange-50 border border-orange-100">
            <h5 class="font-bold text-orange-900 mb-3 flex items-center gap-2">
              <span>🌟</span> Евокација
            </h5>
            <ul class="space-y-2">
              {#each plan.macedonianScenario.evokacija || [] as item}
                <li class="text-slate-700 text-sm flex gap-2">
                  <span class="text-orange-400">•</span> {item}
                </li>
              {/each}
            </ul>
          </div>
          <div class="p-6 rounded-3xl bg-blue-50 border border-blue-100">
            <h5 class="font-bold text-blue-900 mb-3 flex items-center gap-2">
              <span>📖</span> Разбирање
            </h5>
            <ul class="space-y-2">
              {#each plan.macedonianScenario.razbiranje || [] as item}
                <li class="text-slate-700 text-sm flex gap-2">
                  <span class="text-blue-400">•</span> {item}
                </li>
              {/each}
            </ul>
          </div>
          <div class="p-6 rounded-3xl bg-emerald-50 border border-emerald-100">
            <h5 class="font-bold text-emerald-900 mb-3 flex items-center gap-2">
              <span>💡</span> Рефлексија
            </h5>
            <ul class="space-y-2">
              {#each plan.macedonianScenario.refleksija || [] as item}
                <li class="text-slate-700 text-sm flex gap-2">
                  <span class="text-emerald-400">•</span> {item}
                </li>
              {/each}
            </ul>
          </div>
        </div>
      </section>
      {/if}

      <!-- Core Activity Section -->
      <section class="space-y-4">
        <div class="flex items-center gap-3 text-blue-600">
          <span class="text-xl font-black">03</span>
          <h4 class="font-black uppercase tracking-widest text-sm">Главна Активност ({plan?.core_activity?.duration})</h4>
        </div>
        <div class="p-8 rounded-[2rem] border-2 border-blue-100 space-y-6">
          <div>
            <h5 class="font-bold text-blue-900 mb-3 flex items-center gap-2">
              <span>📝</span> Инструкции за наставникот
            </h5>
            <p class="text-slate-700 leading-relaxed whitespace-pre-wrap">{plan?.core_activity?.description}</p>
          </div>
          
          <div class="bg-blue-600 text-white p-6 rounded-2xl shadow-xl shadow-blue-200">
            <h5 class="font-bold mb-2 flex items-center gap-2">
              <span>🎬</span> Визуелен Фокус (Manim)
            </h5>
            <p class="text-blue-50 text-sm leading-relaxed mb-4">{plan?.core_activity?.visual_focus}</p>
            
            {#if videoUrl}
              <div class="mt-4 rounded-xl overflow-hidden border border-white/20">
                <video controls class="w-full">
                  <source src={videoUrl} type="video/mp4">
                  Вашиот прелистувач не поддржува видео.
                </video>
              </div>
            {:else}
              <button 
                on:click={generateVideo}
                disabled={isGeneratingVideo}
                class="w-full py-3 bg-white text-blue-600 rounded-xl font-bold text-sm hover:bg-blue-50 transition-all flex items-center justify-center gap-2 disabled:opacity-50"
              >
                {#if isGeneratingVideo}
                   <span class="animate-pulse">Се рендерира (околу 30 сек)...</span>
                {:else}
                   <span>Генерирај Анимација</span> 🎥
                {/if}
              </button>
            {/if}
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
             {#each plan?.core_activity?.key_questions || [] as question}
                <div class="flex items-start gap-3 p-4 bg-slate-50 rounded-xl border border-slate-100">
                  <span class="text-blue-500 font-bold">?</span>
                  <p class="text-slate-700 text-sm font-medium">{question}</p>
                </div>
             {/each}
          </div>
        </div>
      </section>

      <!-- Olympiad Bridge -->
      <section class="space-y-4">
        <div class="flex items-center gap-3 text-purple-600">
          <span class="text-xl font-black">04</span>
          <h4 class="font-black uppercase tracking-widest text-sm">Олимписки Мост ({plan?.olympiad_bridge?.duration || plan?.olympiadBridge?.duration || '15м'})</h4>
        </div>
        <div class="p-8 rounded-[2rem] bg-gradient-to-br from-purple-600 to-indigo-700 text-white relative overflow-hidden">
          <div class="relative z-10">
            <h5 class="font-bold mb-4 text-xl">{plan?.olympiadBridge?.advancedConcept || 'Конекција со напредна математика'}</h5>
            <p class="text-purple-100 leading-relaxed mb-6">{plan?.olympiadBridge?.connectionToStandard || plan?.olympiad_bridge?.connection}</p>
            <div class="p-6 bg-white/10 rounded-2xl border border-white/20 backdrop-blur-md">
              <h6 class="text-[10px] font-black uppercase tracking-widest mb-2 text-purple-200">Олимписки Предизвик</h6>
              <p class="text-sm font-medium leading-relaxed italic">"{plan?.olympiadBridge?.sampleOlympiadProblem || plan?.olympiad_bridge?.example_problem_brief}"</p>
              {#if plan?.olympiadBridge?.solutionHint}
                <div class="mt-4 pt-4 border-t border-white/10">
                  <p class="text-[10px] font-black uppercase tracking-widest text-purple-200">Совет за решение</p>
                  <p class="text-xs text-purple-100">{plan.olympiadBridge.solutionHint}</p>
                </div>
              {/if}
            </div>
          </div>
          <div class="absolute top-0 right-0 w-32 h-32 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16"></div>
        </div>
      </section>

      <!-- Assessment -->
      <section class="space-y-4">
        <div class="flex items-center gap-3 text-emerald-600">
          <span class="text-xl font-black">05</span>
          <h4 class="font-black uppercase tracking-widest text-sm">Евалуација и Домашна ({plan?.assessment?.duration})</h4>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="p-6 rounded-3xl bg-emerald-50 border border-emerald-100">
            <h5 class="font-bold text-emerald-900 mb-2">Проверка на знаење</h5>
            <p class="text-slate-700 leading-relaxed">{plan?.assessment?.method}</p>
          </div>
          <div class="p-6 rounded-3xl bg-slate-50 border border-slate-100">
            <h5 class="font-bold text-slate-900 mb-2">Предлог Домашна</h5>
            <p class="text-slate-600 leading-relaxed">{plan?.assessment?.homework_suggestion}</p>
          </div>
        </div>
      </section>

    </div>
  </div>
</div>

<style>
  @media print {
    :global(body) { 
      background: white !important; 
      color: black !important;
    }
    .no-print { display: none !important; }
    .printable-area { 
      padding: 0 !important; 
      display: block !important;
      width: 100% !important;
    }
    .fixed { position: relative !important; background: white !important; }
    .bg-white { box-shadow: none !important; border: none !important; height: auto !important; max-width: none !important; }
    
    section { 
      page-break-inside: avoid; 
      margin-bottom: 3rem !important;
      border-bottom: 1px solid #eee;
      padding-bottom: 2rem;
    }

    /* Preserve colors in PDF */
    .bg-indigo-50 { background-color: #f5f7ff !important; -webkit-print-color-adjust: exact; }
    .bg-blue-600 { background-color: #2563eb !important; color: white !important; -webkit-print-color-adjust: exact; }
    .bg-purple-600 { background-color: #9333ea !important; color: white !important; -webkit-print-color-adjust: exact; }
    .bg-emerald-50 { background-color: #ecfdf5 !important; -webkit-print-color-adjust: exact; }
    
    .rounded-3xl, .rounded-2xl, .rounded-\[2rem\] { border-radius: 1rem !important; }
    
    /* Ensure MathJax looks good */
    :global(.mjx-chtml) { font-size: 110% !important; }
  }
</style>
