<script>
  import katex from 'katex';
  import 'katex/dist/katex.min.css'; // Импортирај го CSS-от за да изгледа убаво

  export let text = '';

  // Оваа функција бара текст помеѓу долари ($...$) и го претвора во HTML
  function renderMath(input) {
    // Regex што бара текст помеѓу $ и $ (на пр. $x^2$)
    // Ова е едноставна верзија. За посложени случаи може да се прошири.
    const parts = input.split(/(\$[^\$]+\$)/g);
    
    return parts.map(part => {
      if (part.startsWith('$') && part.endsWith('$')) {
        // Извади ги доларите
        const math = part.slice(1, -1);
        try {
          // Рендерирај со KaTeX
          return katex.renderToString(math, {
            throwOnError: false,
            displayMode: false // Inline math
          });
        } catch (e) {
          return part;
        }
      }
      return part;
    }).join('');
  }
</script>

<span>{@html renderMath(text)}</span>

<style>
  span {
    font-family: 'Inter', sans-serif;
  }
</style>