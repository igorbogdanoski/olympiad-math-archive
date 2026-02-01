<script>
    export let html = '';
    export let onClose = () => {};

    function downloadPresentation() {
        const blob = new Blob([html], { type: 'text/html' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'prezentacija.html';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }
</script>

<div class="fixed inset-0 z-[200] flex items-center justify-center p-4 bg-slate-900/95 backdrop-blur-xl">
    <div class="bg-white rounded-[2.5rem] shadow-2xl w-full max-w-6xl h-[90vh] flex flex-col overflow-hidden border border-slate-200">
        
        <!-- Header -->
        <div class="flex justify-between items-center p-6 border-b border-slate-100 bg-slate-50">
            <div class="flex items-center gap-4">
                <div class="w-10 h-10 bg-orange-500 rounded-xl flex items-center justify-center text-xl shadow-lg shadow-orange-200">
                    📊
                </div>
                <div>
                    <h3 class="font-black text-slate-900 text-xl">AI Презентација</h3>
                    <p class="text-slate-500 text-[10px] font-bold uppercase tracking-widest">Интерактивни слајдови за вашиот час</p>
                </div>
            </div>
            <div class="flex items-center gap-3">
                <button 
                    on:click={downloadPresentation}
                    class="px-5 py-2.5 bg-slate-900 text-white rounded-xl font-bold text-sm hover:bg-slate-800 transition-all flex items-center gap-2"
                >
                    <span>Превземи (HTML)</span> 📥
                </button>
                <button 
                    class="w-10 h-10 flex items-center justify-center rounded-xl hover:bg-slate-200 text-slate-400 hover:text-slate-900 transition-all text-xl" 
                    on:click={onClose}
                >
                    &times;
                </button>
            </div>
        </div>

        <!-- Preview -->
        <div class="flex-1 bg-slate-800 relative">
            <iframe 
                title="Presentation Preview"
                srcdoc={html} 
                class="w-full h-full border-none"
            ></iframe>
        </div>

        <!-- Instructions -->
        <div class="p-4 bg-orange-50 text-orange-800 text-center text-xs font-medium">
            Користете ги стрелките на тастатурата или допир за навигација низ слајдовите.
        </div>
    </div>
</div>
