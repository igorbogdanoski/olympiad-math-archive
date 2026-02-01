<script lang="ts">
  import { onMount } from 'svelte';

  export let content: string = "";
  let element: HTMLElement;

  function renderMath() {
    if (window.MathJax && element) {
      window.MathJax.typesetPromise([element]).catch((err) => console.error('MathJax error:', err));
    }
  }

  onMount(() => {
    renderMath();
  });

  $: if (content && element) {
    // We wait a tick to ensure DOM is updated before typesetting
    setTimeout(renderMath, 0);
  }
</script>

<div bind:this={element} class="math-content">
  {@html content}
</div>

<style>
  .math-content {
    line-height: 1.6;
  }
</style>
