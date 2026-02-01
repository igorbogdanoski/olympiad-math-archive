    // --- ПОПРАВЕНА ФУНКЦИЈА ЗА РЕНДЕРИРАЊЕ ---
    safeRender() {
      const latex = this.textarea.value.trim();

      // Ако нема текст, исчисти го прегледот
      if (!latex) {
         this.previewContent.innerHTML = '';
         return;
      }

      try {
         // Постави го LaTeX со стандардни MathJax делимитери
         this.previewContent.innerHTML = `$${latex}$`;

         // Рендерирај го со MathJax
         if (window.MathJax && window.MathJax.typesetPromise) {
            window.MathJax.typesetPromise([this.previewContent]);
         } else if (window.MathJax && window.MathJax.typeset) {
            window.MathJax.typeset([this.previewContent]);
         } else {
            // Fallback ако MathJax не е достапен
            this.fallbackRender();
         }
      } catch (err) {
         console.warn('MathJax rendering error:', err);
         this.fallbackRender();
      }
    }