<script lang="ts">
	import { onMount } from 'svelte';
	import confetti from 'canvas-confetti';

	// Props
	export let curriculumData: any;

	// State
	let selectedGrade: number = 7;
	let selectedBroCode: string = '';
	let selectedTopic: string = '';
	let duration: number = 45;
	let includeAiNotes: boolean = true;
	let difficultyMix = {
		easy: 0.4,
		medium: 0.4,
		hard: 0.2
	};

	let lessonPlan: any = null;
	let loading: boolean = false;
	let error: string = '';
	let showAdvanced: boolean = false;

	// Templates
	let templates: any[] = [];
	let selectedTemplate: string = 'standard_45';

	// BRO codes for selected grade
	let availableBroCodes: any[] = [];

	// Extract BRO codes from curriculum
	$: if (curriculumData && selectedGrade) {
		const dataArray = Array.isArray(curriculumData) ? curriculumData : [];
		availableBroCodes = dataArray
			.filter((item: any) => item.grade === selectedGrade.toString())
			.map((item: any) => ({
				code: item.bro_code,
				topic: item.topic || item.title || item.bro_code,
				description: item.description || ''
			}));
	}

	// Update topic when BRO code changes
	$: if (selectedBroCode) {
		const found = availableBroCodes.find((item) => item.code === selectedBroCode);
		if (found) {
			selectedTopic = found.topic;
		}
	}

	// Load templates on mount
	onMount(async () => {
		try {
			const response = await fetch('http://localhost:8000/api/lesson-planner/templates');
			const data = await response.json();
			templates = data.templates || [];
		} catch (err) {
			console.error('Failed to load templates:', err);
		}
	});

	// Apply template
	function applyTemplate(templateId: string) {
		const template = templates.find((t) => t.id === templateId);
		if (template) {
			duration = template.duration;
			if (template.difficulty_mix) {
				difficultyMix = template.difficulty_mix;
			}
			selectedTemplate = templateId;
			
			// Toast notification
			showToast('✅ Темплејтот е применет');
		}
	}

	// Generate lesson plan
	async function generateLessonPlan() {
		if (!selectedBroCode || !selectedTopic) {
			error = 'Ве молиме изберете БРО код';
			return;
		}

		loading = true;
		error = '';
		lessonPlan = null;

		try {
			const response = await fetch('http://localhost:8000/api/lesson-planner/generate', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					bro_code: selectedBroCode,
					duration: duration,
					grade: selectedGrade,
					topic: selectedTopic,
					include_ai_notes: includeAiNotes,
					difficulty_mix: difficultyMix
				})
			});

			if (!response.ok) {
				throw new Error('Грешка при генерирање на сценарио');
			}

			lessonPlan = await response.json();
			
			// Confetti celebration
			confetti({
				particleCount: 100,
				spread: 70,
				origin: { y: 0.6 }
			});

			// Scroll to results
			setTimeout(() => {
				document.getElementById('lesson-results')?.scrollIntoView({ behavior: 'smooth' });
			}, 100);
			
			showToast('🎉 Сценариото е генерирано!');
		} catch (err: any) {
			error = err.message || 'Настана грешка. Обидете се повторно.';
			console.error('Error generating lesson plan:', err);
		} finally {
			loading = false;
		}
	}

	// Export to PDF
	async function exportToPdf() {
		if (!lessonPlan) return;
		
		try {
			const response = await fetch(`http://localhost:8000/api/lesson-planner/export-pdf/${lessonPlan.id}`, {
				method: 'POST'
			});
			
			if (response.ok) {
				showToast('📄 PDF е подготвен за превземање');
			}
		} catch (err) {
			console.error('Error exporting PDF:', err);
		}
	}

	// Save as template
	async function saveAsTemplate() {
		if (!lessonPlan) return;
		
		const templateName = prompt('Име на темплејт:');
		if (!templateName) return;
		
		try {
			const response = await fetch('http://localhost:8000/api/lesson-planner/save-template', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					name: templateName,
					description: `Темплејт за ${selectedTopic}`,
					sections: lessonPlan.sections,
					created_by: 'teacher_123',
					is_public: false
				})
			});
			
			if (response.ok) {
				showToast('✅ Темплејтот е зачуван');
			}
		} catch (err) {
			console.error('Error saving template:', err);
		}
	}

	// Share with colleague
	function shareLessonPlan() {
		if (!lessonPlan) return;
		
		const shareUrl = `${window.location.origin}/lesson/${lessonPlan.id}`;
		navigator.clipboard.writeText(shareUrl);
		showToast('🔗 Линкот е копиран');
	}

	// Toast notification
	function showToast(message: string) {
		const toast = document.createElement('div');
		toast.className = 'fixed top-4 right-4 bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg z-50';
		toast.textContent = message;
		document.body.appendChild(toast);
		
		setTimeout(() => {
			toast.remove();
		}, 3000);
	}

	// Format duration
	function formatDuration(minutes: number): string {
		return `${minutes} мин`;
	}

	// Get difficulty badge color
	function getDifficultyColor(difficulty: number): string {
		if (difficulty <= 2) return 'bg-green-100 text-green-700';
		if (difficulty <= 4) return 'bg-orange-100 text-orange-700';
		return 'bg-red-100 text-red-700';
	}
</script>

<div class="lesson-planner-container">
	<!-- Configuration Panel -->
	<div class="config-panel bg-white dark:bg-slate-900 rounded-[2.5rem] shadow-2xl p-8 mb-8">
		<h2 class="text-2xl font-bold text-slate-900 dark:text-white mb-6">⚙️ Конфигурација</h2>
		
		<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
			<!-- Grade Selection -->
			<div>
				<label class="block text-sm font-semibold text-slate-700 dark:text-slate-300 mb-2">
					Одделение
				</label>
				<select
					bind:value={selectedGrade}
					class="w-full px-4 py-3 rounded-xl border-2 bg-white dark:bg-slate-800 text-slate-900 dark:text-white"
				>
					{#each [1, 2, 3, 4, 5, 6, 7, 8, 9] as grade}
						<option value={grade}>{grade} одделение</option>
					{/each}
				</select>
			</div>

			<!-- Duration -->
			<div>
				<label class="block text-sm font-semibold text-slate-700 dark:text-slate-300 mb-2">
					Времетраење
				</label>
				<select
					bind:value={duration}
					class="w-full px-4 py-3 rounded-xl border-2 bg-white dark:bg-slate-800 text-slate-900 dark:text-white"
				>
					<option value={40}>40 минути</option>
					<option value={45}>45 минути</option>
					<option value={60}>60 минути</option>
				</select>
			</div>

			<!-- BRO Code -->
			<div class="md:col-span-2">
				<label class="block text-sm font-semibold text-slate-700 dark:text-slate-300 mb-2">
					БРО Код / Тема
				</label>
				<select
					bind:value={selectedBroCode}
					class="w-full px-4 py-3 rounded-xl border-2 bg-white dark:bg-slate-800 text-slate-900 dark:text-white"
				>
					<option value="">Изберете тема...</option>
					{#each availableBroCodes as broCode}
						<option value={broCode.code}>
							{broCode.code} - {broCode.topic}
						</option>
					{/each}
				</select>
			</div>
		</div>

		<!-- Templates -->
		<div class="mt-6">
			<h3 class="text-lg font-bold text-slate-900 dark:text-white mb-4">📋 Темплејти</h3>
			<div class="grid grid-cols-1 md:grid-cols-3 gap-4">
				{#each templates as template}
					<button
						on:click={() => applyTemplate(template.id)}
						class="p-4 rounded-xl border-2 transition-all text-left {selectedTemplate === template.id ? 'border-blue-500 bg-blue-50' : 'border-slate-200 hover:border-blue-300'}"
					>
						<div class="font-bold text-slate-900 mb-1">{template.name}</div>
						<div class="text-xs text-slate-500">{template.description}</div>
					</button>
				{/each}
			</div>
		</div>

		<!-- Advanced Options -->
		<div class="mt-6">
			<button
				on:click={() => showAdvanced = !showAdvanced}
				class="text-sm font-semibold text-blue-600 hover:underline"
			>
				{showAdvanced ? '▼' : '▶'} Напредни опции
			</button>
			
			{#if showAdvanced}
				<div class="mt-4 p-4 bg-slate-50 dark:bg-slate-800 rounded-xl">
					<h4 class="font-bold text-slate-900 dark:text-white mb-3">Распределба на тежина</h4>
					
					<div class="space-y-3">
						<div>
							<label class="text-sm text-slate-700">
								Лесно: {(difficultyMix.easy * 100).toFixed(0)}%
							</label>
							<input type="range" min="0" max="1" step="0.1" bind:value={difficultyMix.easy} class="w-full" />
						</div>
						
						<div>
							<label class="text-sm text-slate-700">
								Средно: {(difficultyMix.medium * 100).toFixed(0)}%
							</label>
							<input type="range" min="0" max="1" step="0.1" bind:value={difficultyMix.medium} class="w-full" />
						</div>
						
						<div>
							<label class="text-sm text-slate-700">
								Тешко: {(difficultyMix.hard * 100).toFixed(0)}%
							</label>
							<input type="range" min="0" max="1" step="0.1" bind:value={difficultyMix.hard} class="w-full" />
						</div>
					</div>
					
					<div class="mt-4">
						<label class="flex items-center gap-2">
							<input type="checkbox" bind:checked={includeAiNotes} class="rounded" />
							<span class="text-sm text-slate-700">Вклучи AI наставни белешки</span>
						</label>
					</div>
				</div>
			{/if}
		</div>

		<!-- Generate Button -->
		<button
			on:click={generateLessonPlan}
			disabled={loading || !selectedBroCode}
			class="w-full mt-6 py-4 px-8 rounded-xl font-bold text-lg bg-gradient-to-r from-blue-600 to-indigo-600 text-white disabled:opacity-50 transition-all"
		>
			{loading ? '⏳ Генерирам...' : '🚀 Генерирај Сценарио'}
		</button>

		{#if error}
			<div class="mt-4 p-4 bg-red-50 border border-red-200 rounded-xl text-red-700">
				❌ {error}
			</div>
		{/if}
	</div>

	<!-- Results -->
	{#if lessonPlan}
		<div id="lesson-results" class="results-panel bg-white dark:bg-slate-900 rounded-[2.5rem] shadow-2xl p-8">
			<!-- Header -->
			<div class="flex justify-between items-start mb-8">
				<div>
					<h2 class="text-3xl font-black text-slate-900 dark:text-white mb-2">
						{lessonPlan.topic}
					</h2>
					<div class="flex gap-3 items-center">
						<span class="px-3 py-1 bg-blue-100 text-blue-700 rounded-lg text-sm font-bold">
							{lessonPlan.bro_code}
						</span>
						<span class="text-slate-500">
							{lessonPlan.grade} одделение
						</span>
						<span class="text-slate-500">
							⏱️ {formatDuration(lessonPlan.duration)}
						</span>
						<span class="text-slate-500">
							📝 {lessonPlan.total_problems} задачи
						</span>
					</div>
				</div>

				<!-- Actions -->
				<div class="flex gap-2">
					<button on:click={exportToPdf} class="px-4 py-2 bg-slate-100 hover:bg-slate-200 rounded-lg font-semibold" title="Превземи PDF">
						📄 PDF
					</button>
					<button on:click={saveAsTemplate} class="px-4 py-2 bg-slate-100 hover:bg-slate-200 rounded-lg font-semibold" title="Зачувај">
						💾 Зачувај
					</button>
					<button on:click={shareLessonPlan} class="px-4 py-2 bg-slate-100 hover:bg-slate-200 rounded-lg font-semibold" title="Сподели">
						🔗 Сподели
					</button>
				</div>
			</div>

			<!-- AI Notes -->
			{#if lessonPlan.ai_notes}
				<div class="mb-8 p-6 bg-purple-50 rounded-2xl border border-purple-200">
					<h3 class="text-lg font-bold text-purple-900 mb-3 flex items-center gap-2">
						🤖 AI Наставни Белешки
					</h3>
					<div class="text-slate-700 prose prose-sm">
						{@html lessonPlan.ai_notes.replace(/\n/g, '<br>')}
					</div>
				</div>
			{/if}

			<!-- Sections -->
			<div class="space-y-6">
				{#each lessonPlan.sections as section}
					<div class="p-6 bg-slate-50 rounded-2xl border">
						<div class="flex justify-between items-center mb-4">
							<h3 class="text-xl font-bold text-slate-900">
								{section.title}
							</h3>
							<span class="px-3 py-1 bg-blue-100 text-blue-700 rounded-lg text-sm font-bold">
								⏱️ {formatDuration(section.duration_minutes)}
							</span>
						</div>

						{#if section.activities && section.activities.length > 0}
							<div class="mb-4">
								<h4 class="text-sm font-semibold text-slate-600 mb-2">Активности:</h4>
								<ul class="space-y-1">
									{#each section.activities as activity}
										<li class="text-sm text-slate-700">• {activity}</li>
									{/each}
								</ul>
							</div>
						{/if}

						{#if section.problems && section.problems.length > 0}
							<div>
								<h4 class="text-sm font-semibold text-slate-600 mb-3">Задачи ({section.problems.length}):</h4>
								<div class="grid grid-cols-1 md:grid-cols-2 gap-3">
									{#each section.problems as problem}
										<div class="p-4 bg-white rounded-xl border">
											<div class="flex justify-between items-start mb-2">
												<span class="font-mono text-xs text-slate-500">
													{problem.id}
												</span>
												{#if problem.difficulty}
													<span class="px-2 py-1 rounded-md text-xs font-bold {getDifficultyColor(problem.difficulty)}">
														{problem.difficulty}/5
													</span>
												{/if}
											</div>
											<p class="text-sm text-slate-700 line-clamp-2">
												{problem.content_markdown || problem.title || 'Проблем без содржина'}
											</p>
											{#if problem.bro_code}
												<span class="inline-block mt-2 px-2 py-0.5 bg-green-100 text-green-700 rounded text-xs font-mono">
													{problem.bro_code}
												</span>
											{/if}
										</div>
									{/each}
								</div>
							</div>
						{/if}
					</div>
				{/each}
			</div>
		</div>
	{/if}
</div>

<style>
	.line-clamp-2 {
		display: -webkit-box;
		-webkit-line-clamp: 2;
		-webkit-box-orient: vertical;
		overflow: hidden;
	}
</style>
