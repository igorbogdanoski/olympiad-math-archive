<script lang="ts">
	export let matches: any[] = [];

	let filterStatus = 'all'; // all, pending, approved, rejected
	let filterConfidence = 'all'; // all, high (>=0.8), medium (0.6-0.8), low (<0.6)
	let currentIndex = 0;
	let reviewedMatches = matches;
	let isSaving = false;
	let saveMessage = '';

	// Filter matches based on selected filters
	$: filteredMatches = reviewedMatches.filter(match => {
		// Status filter
		if (filterStatus !== 'all' && match.status !== filterStatus) return false;
		
		// Confidence filter
		if (filterConfidence === 'high' && match.confidence < 0.8) return false;
		if (filterConfidence === 'medium' && (match.confidence < 0.6 || match.confidence >= 0.8)) return false;
		if (filterConfidence === 'low' && match.confidence >= 0.6) return false;
		
		return true;
	});

	$: currentMatch = filteredMatches[currentIndex];
	$: stats = {
		total: reviewedMatches.length,
		pending: reviewedMatches.filter(m => m.status === 'pending').length,
		approved: reviewedMatches.filter(m => m.status === 'approved').length,
		rejected: reviewedMatches.filter(m => m.status === 'rejected').length
	};

	function handleApprove() {
		if (currentMatch) {
			currentMatch.status = 'approved';
			reviewedMatches = [...reviewedMatches]; // Trigger reactivity
			nextMatch();
		}
	}

	function handleReject() {
		if (currentMatch) {
			currentMatch.status = 'rejected';
			reviewedMatches = [...reviewedMatches];
			nextMatch();
		}
	}

	function nextMatch() {
		if (currentIndex < filteredMatches.length - 1) {
			currentIndex++;
		}
	}

	function previousMatch() {
		if (currentIndex > 0) {
			currentIndex--;
		}
	}

	async function saveMatches() {
		isSaving = true;
		saveMessage = '';
		
		try {
			const response = await fetch('/api/geogebra-save-matches', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ matches: reviewedMatches })
			});
			
			const result = await response.json();
			
			if (result.success) {
				saveMessage = `✅ Зачувано: ${result.stats.approved} одобрени, ${result.stats.rejected} одбиени`;
			} else {
				saveMessage = `❌ Грешка: ${result.error}`;
			}
		} catch (error) {
			saveMessage = `❌ Network error: ${error}`;
		} finally {
			isSaving = false;
			setTimeout(() => saveMessage = '', 5000);
		}
	}

	function getConfidenceBadgeClass(confidence: number) {
		if (confidence >= 0.8) return 'bg-green-100 text-green-800 dark:bg-green-900/40 dark:text-green-200';
		if (confidence >= 0.6) return 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900/40 dark:text-yellow-200';
		return 'bg-red-100 text-red-800 dark:bg-red-900/40 dark:text-red-200';
	}

	function getStatusBadgeClass(status: string) {
		if (status === 'approved') return 'bg-green-100 text-green-800 dark:bg-green-900/40 dark:text-green-200';
		if (status === 'rejected') return 'bg-red-100 text-red-800 dark:bg-red-900/40 dark:text-red-200';
		return 'bg-gray-100 text-gray-800 dark:bg-gray-900/40 dark:text-gray-200';
	}
</script>

<div class="space-y-6">
	<!-- Filters -->
	<div class="bg-white dark:bg-slate-800 rounded-xl shadow-lg border border-slate-200 dark:border-slate-700 p-6">
		<div class="flex flex-wrap items-center gap-6">
			<div class="flex-1 min-w-[200px]">
				<label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
					Статус
				</label>
				<select 
					bind:value={filterStatus}
					class="w-full px-4 py-2 bg-slate-50 dark:bg-slate-900 border border-slate-300 dark:border-slate-600 rounded-lg focus:ring-2 focus:ring-emerald-500 outline-none"
				>
					<option value="all">Сите ({stats.total})</option>
					<option value="pending">На чекање ({stats.pending})</option>
					<option value="approved">Одобрени ({stats.approved})</option>
					<option value="rejected">Одбиени ({stats.rejected})</option>
				</select>
			</div>

			<div class="flex-1 min-w-[200px]">
				<label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
					Доверба
				</label>
				<select 
					bind:value={filterConfidence}
					class="w-full px-4 py-2 bg-slate-50 dark:bg-slate-900 border border-slate-300 dark:border-slate-600 rounded-lg focus:ring-2 focus:ring-emerald-500 outline-none"
				>
					<option value="all">Сите нивоа</option>
					<option value="high">Висока (≥0.8)</option>
					<option value="medium">Средна (0.6-0.8)</option>
					<option value="low">Ниска (&lt;0.6)</option>
				</select>
			</div>

			<div class="flex items-end gap-3">
				<div class="text-sm text-slate-600 dark:text-slate-400">
					<strong class="text-lg text-slate-900 dark:text-slate-100">{filteredMatches.length}</strong> matches
				</div>
				
				{#if stats.approved > 0 || stats.rejected > 0}
					<button
						on:click={saveMatches}
						disabled={isSaving}
						class="px-6 py-2 bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 disabled:opacity-50 disabled:cursor-not-allowed text-white rounded-lg font-bold transition-all shadow-lg hover:shadow-xl"
					>
						{#if isSaving}
							💾 Зачувување...
						{:else}
							💾 Зачувај Промени
						{/if}
					</button>
				{/if}
				
				{#if saveMessage}
					<div class="text-sm font-medium {saveMessage.includes('✅') ? 'text-green-600 dark:text-green-400' : 'text-red-600 dark:text-red-400'}">
						{saveMessage}
					</div>
				{/if}
			</div>
		</div>
	</div>

	{#if filteredMatches.length === 0}
		<div class="bg-white dark:bg-slate-800 rounded-xl shadow-lg border border-slate-200 dark:border-slate-700 p-12 text-center">
			<div class="text-6xl mb-4">🎉</div>
			<h3 class="text-2xl font-bold text-slate-900 dark:text-slate-100 mb-2">Нема matches за оваа комбинација на филтри</h3>
			<p class="text-slate-600 dark:text-slate-400">Променете ги филтрите или одобрете сите matches!</p>
		</div>
	{:else if currentMatch}
		<!-- Navigation -->
		<div class="flex items-center justify-between bg-white dark:bg-slate-800 rounded-xl shadow-lg border border-slate-200 dark:border-slate-700 p-4">
			<button 
				on:click={previousMatch}
				disabled={currentIndex === 0}
				class="px-4 py-2 bg-slate-100 dark:bg-slate-700 hover:bg-slate-200 dark:hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed rounded-lg font-medium transition-all"
			>
				← Претходна
			</button>

			<div class="text-center">
				<div class="text-sm text-slate-600 dark:text-slate-400">Match</div>
				<div class="text-xl font-bold text-slate-900 dark:text-slate-100">
					{currentIndex + 1} / {filteredMatches.length}
				</div>
			</div>

			<button 
				on:click={nextMatch}
				disabled={currentIndex === filteredMatches.length - 1}
				class="px-4 py-2 bg-slate-100 dark:bg-slate-700 hover:bg-slate-200 dark:hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed rounded-lg font-medium transition-all"
			>
				Следна →
			</button>
		</div>

		<!-- Match Card -->
		<div class="bg-white dark:bg-slate-800 rounded-xl shadow-lg border border-slate-200 dark:border-slate-700 overflow-hidden">
			<!-- Header -->
			<div class="bg-gradient-to-r from-emerald-50 to-teal-50 dark:from-emerald-900/20 dark:to-teal-900/20 p-6 border-b border-slate-200 dark:border-slate-700">
				<div class="flex items-start justify-between mb-4">
					<div>
						<div class="flex items-center gap-3 mb-2">
							<span class="text-2xl">📝</span>
							<h3 class="text-xl font-bold text-slate-900 dark:text-slate-100">Проблем #{currentMatch.problem_id}</h3>
						</div>
						<div class="flex gap-2 flex-wrap">
							<span class="px-3 py-1 bg-blue-100 dark:bg-blue-900/40 text-blue-800 dark:text-blue-200 text-xs font-medium rounded-full">
								{currentMatch.problem_grade}. одделение
							</span>
							<span class="px-3 py-1 bg-purple-100 dark:bg-purple-900/40 text-purple-800 dark:text-purple-200 text-xs font-medium rounded-full">
								{currentMatch.problem_topic}
							</span>
						</div>
					</div>
					<span class={`px-4 py-2 text-sm font-bold rounded-lg ${getStatusBadgeClass(currentMatch.status)}`}>
						{currentMatch.status === 'approved' ? '✓ Одобрено' : currentMatch.status === 'rejected' ? '✗ Одбиено' : '⏳ На чекање'}
					</span>
				</div>

				<p class="text-slate-700 dark:text-slate-300 text-lg leading-relaxed">
					{currentMatch.problem_text}
				</p>
			</div>

			<!-- Match Info -->
			<div class="p-6 border-b border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900/40">
				<div class="flex items-center gap-3 mb-4">
					<span class="text-2xl">🎯</span>
					<h4 class="text-lg font-bold text-slate-900 dark:text-slate-100">AI Match</h4>
					<span class={`px-3 py-1 text-xs font-bold rounded-full ${getConfidenceBadgeClass(currentMatch.confidence)}`}>
						{Math.round(currentMatch.confidence * 100)}% доверба
					</span>
				</div>

				<div class="bg-white dark:bg-slate-800 rounded-lg p-4 mb-4">
					<div class="flex items-start gap-4">
						<div class="flex-shrink-0 w-12 h-12 bg-gradient-to-br from-emerald-400 to-teal-400 rounded-lg flex items-center justify-center text-white text-xl font-bold">
							G
						</div>
						<div class="flex-1">
							<h5 class="font-bold text-slate-900 dark:text-slate-100">{currentMatch.material_title_mk}</h5>
							<p class="text-sm text-slate-600 dark:text-slate-400">{currentMatch.material_title}</p>
							<p class="text-sm text-slate-700 dark:text-slate-300 mt-2 italic">"{currentMatch.reason}"</p>
						</div>
					</div>
				</div>

				{#if currentMatch.alternatives && currentMatch.alternatives.length > 0}
					<div class="text-sm text-slate-600 dark:text-slate-400">
						<strong>Алтернативи:</strong> {currentMatch.alternatives.join(', ')}
					</div>
				{/if}
			</div>

			<!-- GeoGebra Preview -->
			<div class="p-6">
				<div class="flex items-center gap-3 mb-4">
					<span class="text-2xl">👁️</span>
					<h4 class="text-lg font-bold text-slate-900 dark:text-slate-100">GeoGebra Преглед</h4>
				</div>
				
				<div class="bg-slate-100 dark:bg-slate-900 rounded-lg overflow-hidden border border-slate-200 dark:border-slate-700" style="height: 500px;">
					<iframe 
						src={`https://www.geogebra.org/material/iframe/id/${currentMatch.material_id}/width/800/height/500/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false`}
						width="100%" 
						height="100%" 
						style="border:0;"
						title="GeoGebra Preview"
						loading="lazy"
					></iframe>
				</div>

				<div class="mt-4 flex gap-2">
					<a 
						href={`https://www.geogebra.org/m/${currentMatch.material_id}`}
						target="_blank"
						rel="noopener noreferrer"
						class="text-sm text-emerald-600 dark:text-emerald-400 hover:underline"
					>
						🔗 Отвори во GeoGebra
					</a>
				</div>
			</div>

			<!-- Action Buttons -->
			{#if currentMatch.status === 'pending'}
				<div class="p-6 bg-slate-50 dark:bg-slate-900/40 border-t border-slate-200 dark:border-slate-700">
					<div class="flex gap-4">
						<button 
							on:click={handleReject}
							class="flex-1 px-6 py-4 bg-red-500 hover:bg-red-600 text-white rounded-xl font-bold text-lg transition-all shadow-lg hover:shadow-xl"
						>
							✗ Одбиј Match
						</button>
						<button 
							on:click={handleApprove}
							class="flex-1 px-6 py-4 bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 text-white rounded-xl font-bold text-lg transition-all shadow-lg hover:shadow-xl"
						>
							✓ Одобри Match
						</button>
					</div>
				</div>
			{/if}
		</div>
	{/if}
</div>

<style>
	:global(body.dark) select {
		color-scheme: dark;
	}
</style>
