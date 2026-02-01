<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import MathEditor from './MathEditor.svelte';

  export let value: string = "";
  export let label: string = "";
  
  const dispatch = createEventDispatcher();
  
  let showFormulaEditor = false;
  let showGeoGebraEditor = false;
  let currentFormula = "";
  let geogebraId = "";
  let textarea: HTMLTextAreaElement;

  function insertFormula() {
    const start = textarea.selectionStart;
    const end = textarea.selectionEnd;
    const text = textarea.value;
    const before = text.substring(0, start);
    const after = text.substring(end);
    
    // Add spaces around if needed
    const formula = `$${currentFormula}$`;
    value = before + formula + after;
    
    showFormulaEditor = false;
    currentFormula = "";
    
    // Re-focus and set cursor after the inserted formula
    setTimeout(() => {
      textarea.focus();
      const newCursorPos = start + formula.length;
      textarea.setSelectionRange(newCursorPos, newCursorPos);
      dispatch('change', value);
    }, 0);
  }

  function insertGeoGebra() {
    const start = textarea.selectionStart;
    const end = textarea.selectionEnd;
    const text = textarea.value;
    const before = text.substring(0, start);
    const after = text.substring(end);
    
    const tag = ` [geogebra:${geogebraId}] `;
    value = before + tag + after;
    
    showGeoGebraEditor = false;
    geogebraId = "";
    
    setTimeout(() => {
      textarea.focus();
      const newCursorPos = start + tag.length;
      textarea.setSelectionRange(newCursorPos, newCursorPos);
      dispatch('change', value);
    }, 0);
  }

  function handleInput(e: any) {
    value = e.target.value;
    dispatch('change', value);
  }
</script>

<div class="rich-editor-container">
  {#if label}
    <label class="block text-[10px] font-black uppercase tracking-widest text-slate-400 mb-2 ml-1">{label}</label>
  {/if}
  
  <div class="relative">
    <textarea
      bind:this={textarea}
      class="w-full bg-slate-50 border-2 border-slate-100 rounded-2xl p-4 min-h-[150px] font-medium text-slate-700 focus:ring-0 focus:border-indigo-500 transition-all resize-none"
      {value}
      on:input={handleInput}
      placeholder="Внесете го текстот на задачата тука..."
    ></textarea>
    
    <div class="absolute bottom-4 right-4 flex gap-2">
      <button 
        on:click={() => { showGeoGebraEditor = !showGeoGebraEditor; showFormulaEditor = false; }}
        class="bg-white border border-slate-200 text-emerald-600 px-4 py-2 rounded-xl text-xs font-black uppercase tracking-widest shadow-sm hover:shadow-md hover:bg-emerald-50 transition-all flex items-center gap-2"
      >
        <span>📐</span> {showGeoGebraEditor ? 'Затвори' : 'Вметни График'}
      </button>
      <button 
        on:click={() => { showFormulaEditor = !showFormulaEditor; showGeoGebraEditor = false; }}
        class="bg-white border border-slate-200 text-indigo-600 px-4 py-2 rounded-xl text-xs font-black uppercase tracking-widest shadow-sm hover:shadow-md hover:bg-indigo-50 transition-all flex items-center gap-2"
      >
        <span>Σ</span> {showFormulaEditor ? 'Затвори' : 'Вметни Формула'}
      </button>
    </div>
  </div>

  {#if showFormulaEditor}
    <div class="mt-4 p-6 bg-indigo-50/50 rounded-3xl border border-indigo-100 animate-in slide-in-from-top-2">
      <div class="flex justify-between items-center mb-4">
        <h4 class="text-xs font-black uppercase tracking-widest text-indigo-400">Креирај математички израз</h4>
      </div>
      
      <MathEditor bind:value={currentFormula} />
      
      <div class="mt-4 flex justify-end">
        <button 
          on:click={insertFormula}
          disabled={!currentFormula}
          class="bg-indigo-600 text-white px-6 py-3 rounded-xl text-xs font-black uppercase tracking-widest shadow-lg shadow-indigo-200 hover:bg-indigo-700 disabled:bg-slate-300 transition-all"
        >
          Потврди и вметни
        </button>
      </div>
    </div>
  {/if}

  {#if showGeoGebraEditor}
    <div class="mt-4 p-6 bg-emerald-50/50 rounded-3xl border border-emerald-100 animate-in slide-in-from-top-2">
      <div class="flex justify-between items-center mb-4">
        <h4 class="text-xs font-black uppercase tracking-widest text-emerald-600">Вметни GeoGebra График</h4>
      </div>
      
      <div class="flex gap-4">
        <input 
          bind:value={geogebraId} 
          placeholder="Внесете GeoGebra ID (пр. mp67pxtz)"
          class="flex-grow bg-white border-2 border-emerald-100 rounded-xl px-4 py-3 text-sm font-bold text-slate-700 focus:ring-2 ring-emerald-500/20"
        />
        <button 
          on:click={insertGeoGebra}
          disabled={!geogebraId}
          class="bg-emerald-600 text-white px-6 py-3 rounded-xl text-xs font-black uppercase tracking-widest shadow-lg shadow-emerald-200 hover:bg-emerald-700 disabled:bg-slate-300 transition-all"
        >
          Вметни
        </button>
      </div>
      <p class="mt-2 text-[10px] text-emerald-600/70 font-bold italic">
        * ID-то можете да го најдете во URL-то на вашиот GeoGebra материјал.
      </p>
    </div>
  {/if}
</div>

<style>
  .rich-editor-container {
    width: 100%;
  }
</style>
