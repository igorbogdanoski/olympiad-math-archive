<script lang="ts">
  import { onMount } from 'svelte';
  import { dndzone } from 'svelte-dnd-action';
  import { flip } from 'svelte/animate';
  import { API_BASE_URL } from '../utils/config';
  import MathRenderer from './MathRenderer.svelte';
  import RichMathEditor from './RichMathEditor.svelte';

  export let initialStandardCode = null;

  // --- 1. STATE VARIABLES ---
  let worksheetHeader = {
    title: "Нов наставен лист",
    teacher: "",
    date: new Date().toISOString().split('T')[0],
    grade: "8"
  };

  let libraryItems = [];
  let worksheetItems = [];
  let searchQuery = "";
  let isSearching = false;
  let isGeneratingPDF = false;
  let includeAnswerKey = true;
  let statusMessage = "";
  let downloadUrl = null;
  let editingId = null;

  // --- 2. LOGIC (HANDLERS) ---
  async function searchProblems() {
    isSearching = true;
    try {
      const response = await fetch(`${API_BASE_URL}/api/problems/search`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          query: searchQuery,
          grade: worksheetHeader.grade,
          limit: 15
        })
      });
      const data = await response.json();
      libraryItems = data.problems || [];
    } catch (err) {
      console.error('Search error:', err);
    } finally {
      isSearching = false;
    }
  }

  async function loadByStandard(code) {
    isSearching = true;
    try {
      const response = await fetch(`${API_BASE_URL}/api/problems/by-standard`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ standardCode: code, limit: 5 })
      });
      const data = await response.json();
      if (data.problems && data.problems.length > 0) {
        // Auto-add found problems to worksheet
        worksheetItems = data.problems.map(p => ({
          ...p,
          id: `ws-${Math.random().toString(36).substr(2, 9)}`
        }));
        
        // Update header title if we have a specific code
        worksheetHeader.title = `Наставен лист: ${code}`;
      }
    } catch (err) {
      console.error('Standard load error:', err);
    } finally {
      isSearching = false;
    }
  }

  async function generatePDF() {
    if (worksheetItems.length === 0) {
      alert("Додајте задачи во листот пред да генерирате PDF.");
      return;
    }
    
    isGeneratingPDF = true;
    downloadUrl = null;
    statusMessage = "🚀 Иницијализирање на процесот...";

    try {
      const response = await fetch(`${API_BASE_URL}/api/pdf/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          items: worksheetItems,
          header: worksheetHeader,
          include_answer_key: includeAnswerKey
        })
      });
      
      if (!response.ok) throw new Error("Грешка при стартување на задачата");
      
      const data = await response.json();
      const taskId = data.task_id;
      
      const pollInterval = setInterval(async () => {
        try {
          const statusRes = await fetch(`${API_BASE_URL}/api/tasks/${taskId}`);
          const statusData = await statusRes.json();

          if (statusData.status === 'PENDING') {
            statusMessage = "⚙️ Се обработуваат математичките формули...";
          } 
          else if (statusData.status === 'STARTED') {
             statusMessage = "🎨 Се генерира PDF документот...";
          }
          else if (statusData.status === 'SUCCESS') {
            clearInterval(pollInterval);
            isGeneratingPDF = false;
            downloadUrl = statusData.result.pdf_url; 
            statusMessage = "✅ Готово!";
          } 
          else if (statusData.status === 'FAILURE') {
            clearInterval(pollInterval);
            isGeneratingPDF = false;
            statusMessage = "❌ Грешка при генерирање.";
          }
        } catch (err) {
          console.error("Polling error:", err);
        }
      }, 2000);

    } catch (err) {
      console.error('PDF error:', err);
      isGeneratingPDF = false;
      statusMessage = "❌ Неуспешна врска со серверот.";
    }
  }

  function handleDndConsider(e) {
    worksheetItems = e.detail.items;
  }

  function handleDndFinalize(e) {
    worksheetItems = e.detail.items;
  }

  function addToWorksheet(item) {
    const newItem = { ...item, id: `ws-${Math.random().toString(36).substr(2, 9)}` };
    worksheetItems = [...worksheetItems, newItem];
  }

  function toggleEdit(id) {
    if (editingId === id) {
      editingId = null;
    } else {
      editingId = id;
    }
  }

  function handleContentChange(id, newValue) {
    worksheetItems = worksheetItems.map(item => 
      item.id === id ? { ...item, content_markdown: newValue } : item
    );
  }

  function removeProblem(id) {
    worksheetItems = worksheetItems.filter(item => item.id !== id);
    if (editingId === id) editingId = null;
  }

  async function generateVariants(item) {
    statusMessage = "🧬 Генерирање варијанти со AI...";
    try {
      const response = await fetch(`${API_BASE_URL}/api/problems/mutate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          problem_id: item.id,
          content: item.content_markdown,
          count: 1
        })
      });
      const data = await response.json();
      if (data.variations && data.variations.length > 0) {
        const variant = data.variations[0];
        const newItem = { 
          ...item, 
          content_markdown: variant.content_markdown,
          solution: variant.solution,
          id: `variant-${Math.random().toString(36).substr(2, 9)}`,
          isVariant: true
        };
        worksheetItems = [...worksheetItems, newItem];
        statusMessage = "✅ Варијантата е додадена!";
      }
    } catch (err) {
      console.error('Mutation error:', err);
      statusMessage = "❌ Неуспешно генерирање варијанта.";
    }
  }

  onMount(() => {
    if (initialStandardCode) {
      loadByStandard(initialStandardCode);
    } else {
      searchProblems();
    }
  });

  $: if (worksheetHeader.grade) {
    searchProblems();
  }
</script>

<div class="flex h-[85vh] bg-slate-50 p-6 gap-6 rounded-3xl overflow-hidden border border-slate-200 shadow-inner">
  
  <!-- Left Column: The Canvas (Worksheet) -->
  <div class="w-2/3 bg-white shadow-xl rounded-[2rem] p-10 flex flex-col overflow-y-auto border border-slate-100">
    <div class="border-b border-slate-100 pb-8 mb-8">
      <input 
        bind:value={worksheetHeader.title} 
        class="text-4xl font-black w-full border-none focus:ring-0 placeholder-slate-200 text-slate-800" 
        placeholder="Наслов на листот..."
      />
      <div class="flex gap-6 mt-4">
        <div class="flex flex-col gap-1">
          <label class="text-[10px] font-black uppercase tracking-widest text-slate-400 ml-1">Наставник</label>
          <input bind:value={worksheetHeader.teacher} class="bg-slate-50 border-none rounded-xl px-4 py-2 text-sm font-bold text-slate-700 focus:ring-2 ring-indigo-500/20" placeholder="Име и презиме" />
        </div>
        <div class="flex flex-col gap-1">
          <label class="text-[10px] font-black uppercase tracking-widest text-slate-400 ml-1">Датум</label>
          <input type="date" bind:value={worksheetHeader.date} class="bg-slate-50 border-none rounded-xl px-4 py-2 text-sm font-bold text-slate-700 focus:ring-2 ring-indigo-500/20" />
        </div>
        <div class="flex flex-col gap-1">
            <label class="text-[10px] font-black uppercase tracking-widest text-slate-400 ml-1">Одделение</label>
            <select bind:value={worksheetHeader.grade} class="bg-slate-50 border-none rounded-xl px-4 py-2 text-sm font-bold text-slate-700 focus:ring-2 ring-indigo-500/20">
                <option value="6">6 одд.</option>
                <option value="7">7 одд.</option>
                <option value="8">8 одд.</option>
                <option value="9">9 одд.</option>
                <option value="10">I год.</option>
            </select>
          </div>
      </div>
    </div>

    <section 
      use:dndzone={{items: worksheetItems, flipDurationMs: 300}} 
      on:consider={handleDndConsider} 
      on:finalize={handleDndFinalize}
      class="flex-grow min-h-[400px] border-2 border-dashed border-slate-100 rounded-[2rem] p-6 bg-slate-50/30"
    >
      {#each worksheetItems as item (item.id)}
        <div animate:flip="{{duration: 300}}" class="bg-white border border-slate-100 p-8 mb-6 rounded-3xl shadow-sm flex justify-between group relative hover:shadow-md transition-all border-l-4 border-l-indigo-500">
          <div class="w-full">
            <div class="flex items-center gap-2 mb-4">
                <span class="bg-indigo-50 text-indigo-600 text-[10px] font-black px-3 py-1 rounded-full uppercase tracking-wider">{item.topic}</span>
                {#if item.curriculum_codes && item.curriculum_codes.length > 0}
                  {#each item.curriculum_codes as code}
                    <span class="bg-purple-100 text-purple-700 text-[9px] font-bold px-2 py-0.5 rounded border border-purple-200" title="Национален стандард">
                      {code}
                    </span>
                  {/each}
                {/if}
                <span class="text-slate-300 text-[10px] font-bold">ID: {item.id}</span>
            </div>
            {#if editingId === item.id}
              <RichMathEditor 
                value={item.content_markdown} 
                on:change={(e) => handleContentChange(item.id, e.detail)}
              />
            {:else}
              <MathRenderer content={item.content_markdown} />
            {/if}
            <div class="mt-4 flex gap-2">
              <button 
                on:click={() => toggleEdit(item.id)} 
                class="text-[10px] font-black uppercase tracking-widest px-4 py-2 {editingId === item.id ? 'bg-indigo-600 text-white' : 'bg-slate-100 text-slate-500'} rounded-xl hover:opacity-90 transition-all flex items-center gap-2"
              >
                <span>{editingId === item.id ? '💾 Зачувај' : '✍️ Уреди'}</span>
              </button>
              <button 
                on:click={() => generateVariants(item)} 
                class="text-[10px] font-black uppercase tracking-widest px-4 py-2 bg-slate-100 text-slate-500 rounded-xl hover:bg-indigo-50 hover:text-indigo-600 transition-all flex items-center gap-2"
              >
                <span>🧬</span> Направи варијанта (AI)
              </button>
              {#if item.isVariant}
                <span class="text-[10px] font-black uppercase tracking-widest px-4 py-2 bg-amber-50 text-amber-600 rounded-xl border border-amber-100 flex items-center gap-2">
                  <span>✨</span> AI Варијанта
                </span>
              {/if}
            </div>
          </div>
          <button on:click={() => removeProblem(item.id)} class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center rounded-full bg-red-50 text-red-400 opacity-0 group-hover:opacity-100 hover:bg-red-500 hover:text-white transition-all">
            &times;
          </button>
        </div>
      {/each}
      
      {#if worksheetItems.length === 0}
        <div class="flex flex-col items-center justify-center h-full text-slate-300 gap-4 opacity-50">
          <div class="text-6xl">📥</div>
          <div class="font-black uppercase tracking-widest text-sm text-center">
            Влечи задачи тука од десната страна<br>за да го составиш твојот наставен лист
          </div>
        </div>
      {/if}
    </section>

    <div class="mt-8 flex flex-col gap-4">
        <div class="flex justify-between items-center">
            <div class="flex items-center gap-4">
                <p class="text-slate-400 text-xs font-bold uppercase tracking-widest">Вкупно задачи: {worksheetItems.length}</p>
                <label class="flex items-center gap-2 cursor-pointer bg-slate-100 px-4 py-2 rounded-xl border border-slate-200 hover:bg-white transition-all">
                    <input type="checkbox" bind:checked={includeAnswerKey} class="w-4 h-4 text-indigo-600 rounded focus:ring-indigo-500 border-slate-300" />
                    <span class="text-[10px] font-black uppercase tracking-widest text-slate-600">Клуч со одговори</span>
                </label>
            </div>
            <button 
                on:click={generatePDF}
                disabled={isGeneratingPDF || worksheetItems.length === 0}
                class="px-8 py-4 bg-indigo-600 text-white rounded-2xl font-black text-sm hover:bg-indigo-700 disabled:bg-slate-300 disabled:cursor-not-allowed transition-all shadow-xl shadow-indigo-100 flex items-center gap-3"
            >
                {#if isGeneratingPDF}
                    ⏳ Се генерира...
                {:else}
                    Генерирај PDF 📄
                {/if}
            </button>
        </div>

        {#if isGeneratingPDF}
            <div class="text-sm text-indigo-600 bg-indigo-50 px-6 py-3 rounded-2xl border border-indigo-100 animate-pulse font-bold flex items-center gap-3">
                <span class="inline-block animate-spin">⚙️</span> {statusMessage}
            </div>
        {/if}

        {#if downloadUrl}
            <div class="flex items-center gap-4 bg-emerald-50 border border-emerald-100 p-6 rounded-[2rem] w-full justify-between animate-in fade-in slide-in-from-bottom-4 shadow-lg shadow-emerald-100/50">
                <div class="flex items-center gap-4 text-emerald-800">
                    <div class="w-12 h-12 bg-emerald-500 rounded-2xl flex items-center justify-center text-2xl shadow-lg shadow-emerald-200">
                        📄
                    </div>
                    <div>
                        <p class="font-black text-lg leading-tight">Вашиот документ е подготвен!</p>
                        <p class="text-sm text-emerald-600 font-bold">Кликнете на копчето за да го преземете.</p>
                    </div>
                </div>
                <a 
                    href={`${API_BASE_URL}${downloadUrl}`} 
                    target="_blank" 
                    class="bg-emerald-600 hover:bg-emerald-700 text-white px-8 py-4 rounded-2xl font-black text-sm shadow-xl shadow-emerald-200 transition-all flex items-center gap-2"
                >
                    📥 ПРЕЗЕМИ PDF
                </a>
            </div>
        {/if}

        {#if statusMessage.includes('❌')}
            <div class="text-red-600 text-sm bg-red-50 p-4 rounded-2xl w-full text-center border border-red-100 font-bold">
                {statusMessage}
            </div>
        {/if}
    </div>
  </div>

  <!-- Right Column: The Library -->
  <div class="w-1/3 bg-white shadow-xl rounded-[2rem] p-8 flex flex-col border border-slate-100">
    <div class="flex items-center gap-3 mb-8">
        <div class="w-10 h-10 bg-amber-500 rounded-xl flex items-center justify-center text-xl shadow-lg shadow-amber-100">
            🏛️
        </div>
        <h2 class="font-black text-slate-800 text-xl tracking-tight">Банка на задачи</h2>
    </div>
    
    <div class="relative mb-6">
      <input 
        type="text" 
        placeholder="Пребарај задачи..." 
        bind:value={searchQuery}
        on:input={searchProblems}
        class="w-full bg-slate-50 border-none rounded-2xl px-6 py-4 text-sm font-bold text-slate-700 focus:ring-2 ring-indigo-500/20 pl-12" 
      />
      <span class="absolute left-4 top-4 opacity-30">🔍</span>
    </div>

    <div class="overflow-y-auto flex-grow space-y-4 pr-2 custom-scrollbar">
      {#if isSearching}
        <div class="flex justify-center p-10">
            <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-500"></div>
        </div>
      {:else}
        {#each libraryItems as item}
            <div class="bg-slate-50 border border-slate-100 p-5 rounded-2xl hover:bg-white hover:shadow-lg transition-all cursor-grab active:cursor-grabbing group relative">
                <div class="flex items-center justify-between mb-3">
                    <span class="text-[9px] font-black text-slate-400 uppercase tracking-widest">{item.topic}</span>
                    <span class="px-2 py-0.5 rounded-md text-[9px] font-black uppercase {item.difficulty > 3 ? 'bg-red-100 text-red-600' : 'bg-emerald-100 text-emerald-600'}">
                        {item.difficulty > 3 ? 'Тешка' : 'Средна'}
                    </span>
                </div>
                <div class="text-xs text-slate-600 line-clamp-3 mb-3">
                    <MathRenderer content={item.content_markdown} />
                </div>
                {#if item.curriculum_codes && item.curriculum_codes.length > 0}
                  <div class="flex flex-wrap gap-1 mb-3">
                    {#each item.curriculum_codes as code}
                      <span class="text-[8px] bg-purple-50 text-purple-600 px-1.5 py-0.5 rounded border border-purple-100 font-bold">
                        {code}
                      </span>
                    {/each}
                  </div>
                {/if}
                <button 
                    on:click={() => addToWorksheet(item)} 
                    class="w-full py-2 bg-white border border-slate-200 rounded-xl text-xs font-black text-slate-400 hover:bg-indigo-600 hover:text-white hover:border-indigo-600 transition-all"
                >
                    ДОДАЈ ВО ЛИСТ +
                </button>
            </div>
        {/each}
      {/if}
    </div>
  </div>
</div>

<style>
    .custom-scrollbar::-webkit-scrollbar {
        width: 4px;
    }
    .custom-scrollbar::-webkit-scrollbar-track {
        background: transparent;
    }
    .custom-scrollbar::-webkit-scrollbar-thumb {
        background: #e2e8f0;
        border-radius: 10px;
    }
    :global(.math-content p) {
        margin: 0;
    }
</style>
