<script lang="ts">
  import { onMount, createEventDispatcher } from 'svelte';
  import 'mathlive';

  export let value: string = "";
  export let label: string = "";
  
  const dispatch = createEventDispatcher();
  let mathfield: any;

  onMount(() => {
    if (mathfield) {
      mathfield.value = value;
      mathfield.addEventListener('input', (ev: any) => {
        value = ev.target.value;
        dispatch('change', value);
      });
    }
  });

  $: if (mathfield && value !== mathfield.value) {
    mathfield.value = value;
  }
</script>

<div class="math-editor-container">
  {#if label}
    <label class="block text-[10px] font-black uppercase tracking-widest text-slate-400 mb-2 ml-1">{label}</label>
  {/if}
  <math-field 
    bind:this={mathfield}
    class="w-full bg-slate-50 border-2 border-slate-100 rounded-2xl p-4 text-lg focus:outline-none focus:border-indigo-500 transition-all"
  >
    {value}
  </math-field>
</div>

<style>
  math-field {
    --caret-color: #6366f1;
    --selection-background-color: #e0e7ff;
    --outline-radius: 1rem;
    display: block;
  }
  
  math-field:focus-within {
    outline: none;
    border-color: #6366f1;
    box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.1);
  }
</style>
