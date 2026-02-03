<script lang="ts">
	import { onMount } from 'svelte';
	import confetti from 'canvas-confetti';

	// Props
	export let curriculumData: any;

	// State
	let selectedBroCodes: string[] = [];
	let questionCount: number = 10;
	let selectedFormats: string[] = ['multiple_choice', 'true_false', 'short_answer'];
	let difficulty: string = 'mixed';
	let timeLimit: number | null = null;
	let generateAnswerKey: boolean = true;
	let includeImages: boolean = true;

	let quiz: any = null;
	let loading: boolean = false;
	let error: string = '';
	let showAdvanced: boolean = false;

	// Available formats
	let formats: any[] = [];
	let availableBroCodes: any[] = [];

	// Extract unique BRO codes from curriculum
	$: {
		const unique = new Set<string>();
		if (curriculumData) {
			curriculumData.forEach((item: any) => {
				if (item.bro_code) {
					unique.add(item.bro_code);
				}
			});
		}
		availableBroCodes = Array.from(unique).map(code => {
			const item = curriculumData.find((i: any) => i.bro_code === code);
			return {
				code,
				topic: item?.topic || item?.title || code,
				grade: item?.grade || ''
			};
		});
	}

	// Load formats on mount
	onMount(async () => {
		try {
			const response = await fetch('http://localhost:8000/api/quiz-generator/formats');
			const data = await response.json();
			formats = data.formats || [];
		} catch (err) {
			console.error('Failed to load formats:', err);
		}
	});

	// Toggle BRO code
	function toggleBroCode(code: string) {
		const index = selectedBroCodes.indexOf(code);
		if (index > -1) {
			selectedBroCodes = selectedBroCodes.filter(c => c !== code);
		} else {
			selectedBroCodes = [...selectedBroCodes, code];
		}
	}

	// Toggle format
	function toggleFormat(formatId: string) {
		const index = selectedFormats.indexOf(formatId);
		if (index > -1) {
			selectedFormats = selectedFormats.filter(f => f !== formatId);
		} else {
			selectedFormats = [...selectedFormats, formatId];
		}
	}

	// Generate quiz
	async function generateQuiz() {
		if (selectedBroCodes.length === 0) {
			error = 'Изберете барем еден БРО код';
			return;
		}

		if (selectedFormats.length === 0) {
			error = 'Изберете барем еден формат';
			return;
		}

		loading = true;
		error = '';
		quiz = null;

		try {
			const response = await fetch('http://localhost:8000/api/quiz-generator/generate', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					bro_codes: selectedBroCodes,
					question_count: questionCount,
					formats: selectedFormats,
					difficulty: difficulty,
					include_images: includeImages,
					generate_answer_key: generateAnswerKey,
					time_limit: timeLimit
				})
			});

			if (!response.ok) {
				throw new Error('Грешка при генерирање на квиз');
			}

			quiz = await response.json();

			// Confetti
			confetti({
				particleCount: 150,
				spread: 80,
				origin: { y: 0.6 }
			});

			// Scroll to results
			setTimeout(() => {
				document.getElementById('quiz-results')?.scrollIntoView({ behavior: 'smooth' });
			}, 100);

			showToast('🎉 Квизот е генериран!');
		} catch (err: any) {
			error = err.message || 'Настана грешка. Обидете се повторно.';
			console.error('Error generating quiz:', err);
		} finally {
			loading = false;
		}
	}

	// Export to PDF
	async function exportToPdf() {
		if (!quiz) return;

		try {
			const response = await fetch(`http://localhost:8000/api/quiz-generator/export-pdf/${quiz.id}?include_answers=${generateAnswerKey}`, {
				method: 'POST'
			});

			if (response.ok) {
				showToast('📄 PDF е подготвен за превземање');
			}
		} catch (err) {
			console.error('Error exporting PDF:', err);
		}
	}

	// Export to Excel
	async function exportToExcel() {
		if (!quiz) return;

		try {
			const response = await fetch(`http://localhost:8000/api/quiz-generator/export-excel/${quiz.id}`, {
				method: 'POST'
			});

			if (response.ok) {
				showToast('📊 Excel е подготвен за превземање');
			}
		} catch (err) {
			console.error('Error exporting Excel:', err);
		}
	}

	// Save to question bank
	async function saveToBank() {
		if (!quiz) return;

		const bankName = prompt('Име на Question Bank:');
		if (!bankName) return;

		try {
			const response = await fetch('http://localhost:8000/api/quiz-generator/save-bank', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					questions: quiz.questions,
					bank_name: bankName
				})
			});

			if (response.ok) {
				showToast('✅ Банката е зачувана');
			}
		} catch (err) {
			console.error('Error saving bank:', err);
		}
	}

	// Toast notification
	function showToast(message: string) {
		const toast = document.createElement('div');
		toast.className = 'fixed top-4 right-4 bg-purple-500 text-white px-6 py-3 rounded-lg shadow-lg z-50';
		toast.textContent = message;
		document.body.appendChild(toast);

		setTimeout(() => {
			toast.remove();
		}, 3000);
	}

	// Get format icon
	function getFormatIcon(format: string): string {
		const icons: any = {
			multiple_choice: '🔘',
			true_false: '✓✗',
			short_answer: '📝',
			essay: '📄'
		};
		return icons[format] || '❓';
	}

	// Get difficulty badge
	function getDifficultyBadge(diff: number): string {
		if (diff <= 2) return 'bg-green-100 text-green-700';
		if (diff <= 4) return 'bg-orange-100 text-orange-700';
		return 'bg-red-100 text-red-700';
	}
</script>

<div class="quiz-generator-container">
	<!-- Configuration Panel -->
	<div class="config-panel bg-white dark:bg-slate-900 rounded-[2.5rem] shadow-2xl p-8 mb-8">
		<h2 class="text-2xl font-bold text-slate-900 dark:text-white mb-6">⚙️ Конфигурација</h2>

		<!-- BRO Code Selection -->
		<div class="mb-6">
			<label class="block text-sm font-semibold text-slate-700 dark:text-slate-300 mb-3">
				Изберете БРО Кодови ({selectedBroCodes.length} избрани)
			</label>
			<div class="max-h-48 overflow-y-auto p-4 bg-slate-50 dark:bg-slate-800 rounded-xl border-2 border-slate-200 dark:border-slate-700">
				<div class="grid grid-cols-1 md:grid-cols-2 gap-2">
					{#each availableBroCodes as broCode}
						<label class="flex items-center gap-2 p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-700 cursor-pointer">
							<input
								type="checkbox"
								checked={selectedBroCodes.includes(broCode.code)}
								on:change={() => toggleBroCode(broCode.code)}
								class="rounded"
							/>
							<span class="text-sm text-slate-700 dark:text-slate-300">
								{broCode.code} - {broCode.topic}
							</span>
						</label>
					{/each}
				</div>
			</div>
		</div>

		<!-- Question Count & Difficulty -->
		<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
			<div>
				<label class="block text-sm font-semibold text-slate-700 dark:text-slate-300 mb-2">
					Број на прашања
				</label>
				<select
					bind:value={questionCount}
					class="w-full px-4 py-3 rounded-xl border-2 bg-white dark:bg-slate-800 text-slate-900 dark:text-white"
				>
					<option value={5}>5 прашања (брз квиз)</option>
					<option value={10}>10 прашања (стандард)</option>
					<option value={15}>15 прашања (опширен)</option>
					<option value={20}>20 прашања (детален тест)</option>
				</select>
			</div>

			<div>
				<label class="block text-sm font-semibold text-slate-700 dark:text-slate-300 mb-2">
					Тежина
				</label>
				<select
					bind:value={difficulty}
					class="w-full px-4 py-3 rounded-xl border-2 bg-white dark:bg-slate-800 text-slate-900 dark:text-white"
				>
					<option value="easy">Лесно (70% easy, 20% medium, 10% hard)</option>
					<option value="mixed">Мешано (40% easy, 40% medium, 20% hard)</option>
					<option value="medium">Средно (30% easy, 50% medium, 20% hard)</option>
					<option value="hard">Тешко (10% easy, 30% medium, 60% hard)</option>
				</select>
			</div>
		</div>

		<!-- Formats -->
		<div class="mb-6">
			<label class="block text-sm font-semibold text-slate-700 dark:text-slate-300 mb-3">
				Формати на прашања
			</label>
			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-3">
				{#each formats as format}
					<button
						on:click={() => toggleFormat(format.id)}
						class="p-4 rounded-xl border-2 transition-all text-left {selectedFormats.includes(format.id) ? 'border-purple-500 bg-purple-50 dark:bg-purple-900/20' : 'border-slate-200 dark:border-slate-700'}"
					>
						<div class="text-2xl mb-2">{format.icon}</div>
						<div class="font-bold text-slate-900 dark:text-white text-sm mb-1">{format.name}</div>
						<div class="text-xs text-slate-500 dark:text-slate-400">{format.description}</div>
						<div class="mt-2 text-xs font-bold text-purple-600 dark:text-purple-400">
							{format.points} {format.points === 1 ? 'поен' : 'поени'}
						</div>
					</button>
				{/each}
			</div>
		</div>

		<!-- Advanced Options -->
		<div class="mb-6">
			<button
				on:click={() => showAdvanced = !showAdvanced}
				class="text-sm font-semibold text-purple-600 dark:text-purple-400 hover:underline"
			>
				{showAdvanced ? '▼' : '▶'} Напредни опции
			</button>

			{#if showAdvanced}
				<div class="mt-4 p-4 bg-slate-50 dark:bg-slate-800 rounded-xl space-y-4">
					<div>
						<label class="block text-sm font-semibold text-slate-700 dark:text-slate-300 mb-2">
							Временско ограничување (минути)
						</label>
						<input
							type="number"
							bind:value={timeLimit}
							placeholder="Опционално"
							min="5"
							max="180"
							class="w-full px-4 py-2 rounded-lg border-2 bg-white dark:bg-slate-900"
						/>
					</div>

					<div class="space-y-2">
						<label class="flex items-center gap-2">
							<input type="checkbox" bind:checked={generateAnswerKey} class="rounded" />
							<span class="text-sm text-slate-700 dark:text-slate-300">Генерирај клуч за поени (решенија)</span>
						</label>

						<label class="flex items-center gap-2">
							<input type="checkbox" bind:checked={includeImages} class="rounded" />
							<span class="text-sm text-slate-700 dark:text-slate-300">Вклучи слики (ако достапни)</span>
						</label>
					</div>
				</div>
			{/if}
		</div>

		<!-- Generate Button -->
		<button
			on:click={generateQuiz}
			disabled={loading || selectedBroCodes.length === 0}
			class="w-full py-4 px-8 rounded-xl font-bold text-lg bg-gradient-to-r from-purple-600 to-pink-600 text-white disabled:opacity-50 transition-all hover:shadow-xl"
		>
			{loading ? '⏳ Генерирам...' : '🚀 Генерирај Квиз'}
		</button>

		{#if error}
			<div class="mt-4 p-4 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-xl text-red-700 dark:text-red-400">
				❌ {error}
			</div>
		{/if}
	</div>

	<!-- Results -->
	{#if quiz}
		<div id="quiz-results" class="results-panel bg-white dark:bg-slate-900 rounded-[2.5rem] shadow-2xl p-8">
			<!-- Header -->
			<div class="flex justify-between items-start mb-8">
				<div>
					<h2 class="text-3xl font-black text-slate-900 dark:text-white mb-2">
						{quiz.title}
					</h2>
					<div class="flex gap-3 items-center flex-wrap">
						<span class="px-3 py-1 bg-purple-100 dark:bg-purple-900/30 text-purple-700 dark:text-purple-400 rounded-lg text-sm font-bold">
							📝 {quiz.question_count} прашања
						</span>
						<span class="px-3 py-1 bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-400 rounded-lg text-sm font-bold">
							🎯 {quiz.total_points} поени
						</span>
						{#if quiz.time_limit}
							<span class="px-3 py-1 bg-orange-100 dark:bg-orange-900/30 text-orange-700 dark:text-orange-400 rounded-lg text-sm font-bold">
								⏱️ {quiz.time_limit} мин
							</span>
						{/if}
					</div>
				</div>

				<!-- Actions -->
				<div class="flex gap-2">
					<button
						on:click={exportToPdf}
						class="px-4 py-2 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 rounded-lg font-semibold"
						title="Превземи PDF"
					>
						📄 PDF
					</button>
					<button
						on:click={exportToExcel}
						class="px-4 py-2 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 rounded-lg font-semibold"
						title="Excel за оценување"
					>
						📊 Excel
					</button>
					<button
						on:click={saveToBank}
						class="px-4 py-2 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 rounded-lg font-semibold"
						title="Зачувај во банка"
					>
						💾 Банка
					</button>
				</div>
			</div>

			<!-- Difficulty Distribution -->
			<div class="mb-8 p-6 bg-gradient-to-r from-green-50 to-orange-50 dark:from-green-900/20 dark:to-orange-900/20 rounded-2xl">
				<h3 class="text-lg font-bold text-slate-900 dark:text-white mb-4">📊 Распределба на Тежина</h3>
				<div class="grid grid-cols-3 gap-4">
					<div class="text-center">
						<div class="text-3xl font-black text-green-600 dark:text-green-400">
							{quiz.difficulty_distribution.easy}
						</div>
						<div class="text-sm text-slate-600 dark:text-slate-400">Лесни</div>
					</div>
					<div class="text-center">
						<div class="text-3xl font-black text-orange-600 dark:text-orange-400">
							{quiz.difficulty_distribution.medium}
						</div>
						<div class="text-sm text-slate-600 dark:text-slate-400">Средни</div>
					</div>
					<div class="text-center">
						<div class="text-3xl font-black text-red-600 dark:text-red-400">
							{quiz.difficulty_distribution.hard}
						</div>
						<div class="text-sm text-slate-600 dark:text-slate-400">Тешки</div>
					</div>
				</div>
			</div>

			<!-- Questions -->
			<div class="space-y-6">
				{#each quiz.questions as question}
					<div class="question-card p-6 bg-slate-50 dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700">
						<!-- Question Header -->
						<div class="flex justify-between items-start mb-4">
							<div class="flex items-center gap-3">
								<span class="text-2xl font-black text-purple-600 dark:text-purple-400">
									#{question.question_number}
								</span>
								<span class="text-lg font-semibold">
									{getFormatIcon(question.format)} {question.format.replace('_', ' ')}
								</span>
							</div>
							<div class="flex items-center gap-2">
								<span class="px-3 py-1 {getDifficultyBadge(question.difficulty)} rounded-lg text-xs font-bold">
									{question.difficulty}/5
								</span>
								<span class="px-3 py-1 bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-400 rounded-lg text-xs font-bold">
									{question.points} {question.points === 1 ? 'поен' : 'поени'}
								</span>
							</div>
						</div>

						<!-- Question Text -->
						<div class="mb-4 p-4 bg-white dark:bg-slate-900 rounded-xl">
							<p class="text-slate-800 dark:text-slate-200 font-medium">
								{question.question_text}
							</p>
							{#if question.image_url}
								<img src={question.image_url} alt="Question illustration" class="mt-3 rounded-lg max-w-md" />
							{/if}
						</div>

						<!-- Options (if applicable) -->
						{#if question.options}
							<div class="space-y-2">
								{#each question.options as option, i}
									<div class="p-3 bg-white dark:bg-slate-900 rounded-lg border border-slate-200 dark:border-slate-700">
										<span class="font-bold text-purple-600 dark:text-purple-400 mr-2">
											{String.fromCharCode(65 + i)}.
										</span>
										{option}
									</div>
								{/each}
							</div>
						{/if}

						<!-- БРО Code -->
						{#if question.bro_code}
							<div class="mt-3">
								<span class="inline-block px-2 py-1 bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-400 rounded text-xs font-mono">
									{question.bro_code}
								</span>
							</div>
						{/if}
					</div>
				{/each}
			</div>

			<!-- Answer Key -->
			{#if quiz.answer_key}
				<div class="mt-8 p-6 bg-gradient-to-br from-emerald-50 to-teal-50 dark:from-emerald-900/20 dark:to-teal-900/20 rounded-2xl border border-emerald-200 dark:border-emerald-800">
					<h3 class="text-xl font-bold text-emerald-900 dark:text-emerald-300 mb-4 flex items-center gap-2">
						✅ Клуч за Поени (Решенија)
					</h3>
					<div class="grid grid-cols-1 md:grid-cols-2 gap-3">
						{#each Object.entries(quiz.answer_key.answers) as [num, answer]}
							<div class="p-3 bg-white dark:bg-slate-900 rounded-xl">
								<div class="flex justify-between items-center">
									<span class="font-bold text-emerald-700 dark:text-emerald-400">
										#{num}:
									</span>
									<span class="px-2 py-1 bg-emerald-100 dark:bg-emerald-900/30 text-emerald-700 dark:text-emerald-400 rounded text-sm font-mono">
										{answer.correct_answer}
									</span>
								</div>
								<div class="text-xs text-slate-500 dark:text-slate-400 mt-1">
									{quiz.answer_key.scoring_guide[num]}
								</div>
							</div>
						{/each}
					</div>
					<div class="mt-4 p-3 bg-emerald-100 dark:bg-emerald-900/30 rounded-xl text-center">
						<span class="text-sm font-bold text-emerald-900 dark:text-emerald-300">
							Вкупно поени: {quiz.answer_key.total_points}
						</span>
					</div>
				</div>
			{/if}
		</div>
	{/if}
</div>

<style>
	.quiz-generator-container {
		max-width: 1200px;
		margin: 0 auto;
	}

	.question-card {
		transition: all 0.2s;
	}

	.question-card:hover {
		transform: translateY(-2px);
		box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
	}
</style>
