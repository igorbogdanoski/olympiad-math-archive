import type { APIRoute } from 'astro';
import fs from 'fs';
import path from 'path';

// Load curriculum data
const curriculumPath = path.join(process.cwd(), 'src', 'data', 'curriculum_standards.json');
const curriculumData = fs.existsSync(curriculumPath) ? JSON.parse(fs.readFileSync(curriculumPath, 'utf-8')) : null;

// Lesson plan alignment analysis function
function analyzeLessonPlanAlignment(topic: string, lessonObjectives: string[], gradeCurriculum: any): any {
  const alignment = {
    score: 0,
    matched_objectives: [] as string[],
    curriculum_relevance: [] as string[],
    gaps: [] as string[],
    suggestions: [] as string[]
  };

  // Analyze topic alignment
  const curriculumTopics = Object.keys(gradeCurriculum.topics || {});
  const topicLower = topic.toLowerCase();

  let topicMatch = false;
  for (const currTopic of curriculumTopics) {
    if (currTopic.toLowerCase().includes(topicLower) || topicLower.includes(currTopic.toLowerCase())) {
      topicMatch = true;
      alignment.curriculum_relevance.push(`Тема "${topic}" се поклопува со наставната програма: "${currTopic}"`);

      // Check objectives alignment
      const topicData = gradeCurriculum.topics[currTopic];
      if (topicData.objectives) {
        lessonObjectives.forEach(obj => {
          const objLower = obj.toLowerCase();
          topicData.objectives.forEach((currObj: string) => {
            if (currObj.toLowerCase().includes(objLower) || objLower.includes(currObj.toLowerCase())) {
              alignment.matched_objectives.push(currObj);
            }
          });
        });
      }

      // Check standards alignment
      if (topicData.standards) {
        alignment.curriculum_relevance.push(`Стандарди поврзани со темата: ${topicData.standards.slice(0, 2).join(', ')}`);
      }
      break;
    }
  }

  if (!topicMatch) {
    alignment.gaps.push(`Темата "${topic}" не е директно пронајдена во наставната програма за овој одделение`);
    alignment.suggestions.push('Разгледајте дали темата е дел од наставната програма или треба да се прилагоди');
  }

  // Calculate alignment score
  const matchedObjectivesRatio = lessonObjectives.length > 0 ? alignment.matched_objectives.length / lessonObjectives.length : 0;
  const topicRelevanceScore = topicMatch ? 100 : 0;
  alignment.score = Math.round((matchedObjectivesRatio * 60) + (topicRelevanceScore * 0.4));

  // Generate suggestions based on analysis
  if (alignment.score < 50) {
    alignment.suggestions.push('Разгледајте дополнителни ресурси за подобро покривање на наставните цели');
  }

  if (alignment.matched_objectives.length === 0) {
    alignment.suggestions.push('Додајте цели кои се поклопуваат со стандардите од наставната програма');
  }

  return alignment;
}

// Curriculum gap analysis function
function performGapAnalysis(gradeCurriculum: any, subject: string, grade: string): any {
  const analysis = {
    grade,
    subject,
    total_topics: 0,
    total_objectives: 0,
    total_standards: 0,
    topic_completeness: [] as any[],
    identified_gaps: [] as string[],
    recommendations: [] as string[],
    coverage_score: 0,
    priority_areas: [] as string[]
  };

  // Analyze topics
  const topics = gradeCurriculum.topics || {};
  analysis.total_topics = Object.keys(topics).length;

  Object.entries(topics).forEach(([topicName, topicData]: [string, any]) => {
    const topicCompleteness = {
      topic: topicName,
      objectives_count: topicData.objectives?.length || 0,
      standards_count: topicData.standards?.length || 0,
      has_detailed_content: (topicData.objectives?.length > 0) && (topicData.standards?.length > 0),
      completeness_score: 0
    };

    // Calculate completeness score
    let score = 0;
    if (topicData.objectives?.length > 0) score += 50;
    if (topicData.standards?.length > 0) score += 50;
    topicCompleteness.completeness_score = score;

    analysis.topic_completeness.push(topicCompleteness);
    analysis.total_objectives += topicData.objectives?.length || 0;
    analysis.total_standards += topicData.standards?.length || 0;
  });

  // Identify gaps
  const topicsWithoutObjectives = analysis.topic_completeness.filter(t => t.objectives_count === 0);
  const topicsWithoutStandards = analysis.topic_completeness.filter(t => t.standards_count === 0);
  const incompleteTopics = analysis.topic_completeness.filter(t => t.completeness_score < 100);

  if (topicsWithoutObjectives.length > 0) {
    analysis.identified_gaps.push(`${topicsWithoutObjectives.length} теми немаат дефинирани цели`);
    analysis.priority_areas.push('Додадете цели за следниве теми: ' + topicsWithoutObjectives.map(t => t.topic).join(', '));
  }

  if (topicsWithoutStandards.length > 0) {
    analysis.identified_gaps.push(`${topicsWithoutStandards.length} теми немаат дефинирани стандарди`);
    analysis.priority_areas.push('Додадете стандарди за следниве теми: ' + topicsWithoutStandards.map(t => t.topic).join(', '));
  }

  if (analysis.total_topics === 0) {
    analysis.identified_gaps.push('Нема дефинирани теми за овој одделение');
    analysis.recommendations.push('Додадете теми од наставната програма за овој одделение');
  }

  if (analysis.total_objectives === 0) {
    analysis.identified_gaps.push('Нема дефинирани цели за учење');
    analysis.recommendations.push('Додадете цели за учење согласно стандардите');
  }

  // Calculate overall coverage score
  if (analysis.total_topics > 0) {
    const avgCompleteness = analysis.topic_completeness.reduce((sum, t) => sum + t.completeness_score, 0) / analysis.total_topics;
    analysis.coverage_score = Math.round(avgCompleteness);
  }

  // Generate recommendations based on gaps
  if (analysis.coverage_score < 50) {
    analysis.recommendations.push('Критична потреба од комплетирање на наставната програма');
    analysis.recommendations.push('Контактирајте BRO за најновите стандарди');
  } else if (analysis.coverage_score < 80) {
    analysis.recommendations.push('Дополнете ги преостанатите теми и цели');
    analysis.recommendations.push('Разгледајте можности за професионално развитие');
  } else {
    analysis.recommendations.push('Наставната програма е добро покриена');
    analysis.recommendations.push('Фокусирајте се на квалитетот на имплементација');
  }

  // Subject-specific recommendations
  if (subject === 'mathematics') {
    if (grade.includes('7') || grade.includes('8') || grade.includes('9')) {
      analysis.recommendations.push('Обезбедете доволно време за алгебра и геометрија');
    }
    if (grade.includes('10') || grade.includes('11') || grade.includes('12')) {
      analysis.recommendations.push('Фокусирајте се на подготовка за високото образование');
    }
  }

  return analysis;
}

// Olympiad problems curriculum alignment function
function alignProblemsWithCurriculum(problems: any[], gradeCurriculum: any, grade: string): any {
  const results = {
    total_problems: problems.length,
    aligned_problems: 0,
    partially_aligned_problems: 0,
    unaligned_problems: 0,
    alignments: [] as any[],
    coverage_analysis: {
      covered_topics: [] as string[],
      uncovered_topics: [] as string[],
      topic_distribution: {} as any
    },
    difficulty_alignment: [] as any[],
    recommendations: [] as string[]
  };

  const curriculumTopics = Object.keys(gradeCurriculum.topics || {});

  problems.forEach((problem, index) => {
    const alignment = {
      problem_id: problem.id || index,
      problem_title: problem.title || `Problem ${index + 1}`,
      alignment_score: 0,
      matched_topics: [] as string[],
      matched_objectives: [] as string[],
      matched_standards: [] as string[],
      alignment_level: 'unaligned',
      difficulty_match: false,
      recommendations: [] as string[]
    };

    // Analyze topic alignment
    const problemText = (problem.title + ' ' + (problem.content || '') + ' ' + (problem.tags?.join(' ') || '')).toLowerCase();

    curriculumTopics.forEach(topic => {
      const topicLower = topic.toLowerCase();
      if (problemText.includes(topicLower) ||
          topicLower.split(' ').some(word => problemText.includes(word) && word.length > 3)) {
        alignment.matched_topics.push(topic);
        alignment.alignment_score += 30;

        // Check objectives and standards alignment
        const topicData = gradeCurriculum.topics[topic];
        if (topicData.objectives) {
          topicData.objectives.forEach((obj: string) => {
            const objWords = obj.toLowerCase().split(' ');
            const matchRatio = objWords.filter(word => problemText.includes(word) && word.length > 3).length / objWords.length;
            if (matchRatio > 0.3) {
              alignment.matched_objectives.push(obj);
              alignment.alignment_score += 10;
            }
          });
        }

        if (topicData.standards) {
          topicData.standards.forEach((std: string) => {
            const stdWords = std.toLowerCase().split(' ');
            const matchRatio = stdWords.filter(word => problemText.includes(word) && word.length > 3).length / stdWords.length;
            if (matchRatio > 0.3) {
              alignment.matched_standards.push(std);
              alignment.alignment_score += 5;
            }
          });
        }
      }
    });

    // Determine alignment level
    if (alignment.alignment_score >= 70) {
      alignment.alignment_level = 'fully_aligned';
      results.aligned_problems++;
    } else if (alignment.alignment_score >= 30) {
      alignment.alignment_level = 'partially_aligned';
      results.partially_aligned_problems++;
    } else {
      alignment.alignment_level = 'unaligned';
      results.unaligned_problems++;
      alignment.recommendations.push('Овој проблем не се поклопува добро со наставната програма');
    }

    // Difficulty analysis
    const gradeNum = parseInt(grade.replace('grade_', ''));
    const problemDifficulty = problem.difficulty || problem.level || 1;

    if (Math.abs(problemDifficulty - gradeNum) <= 1) {
      alignment.difficulty_match = true;
      alignment.alignment_score += 20;
    } else {
      alignment.recommendations.push(`Тежината на проблемот (${problemDifficulty}) може да не одговара на одделението (${gradeNum})`);
    }

    // Cap alignment score
    alignment.alignment_score = Math.min(100, alignment.alignment_score);

    results.alignments.push(alignment);

    // Update coverage analysis
    alignment.matched_topics.forEach(topic => {
      results.coverage_analysis.covered_topics.push(topic);
      results.coverage_analysis.topic_distribution[topic] = (results.coverage_analysis.topic_distribution[topic] || 0) + 1;
    });
  });

  // Identify uncovered topics
  results.coverage_analysis.uncovered_topics = curriculumTopics.filter(
    topic => !results.coverage_analysis.covered_topics.includes(topic)
  );

  // Generate recommendations
  const alignmentRatio = results.aligned_problems / results.total_problems;
  if (alignmentRatio < 0.5) {
    results.recommendations.push('Повеќе од половина од проблемите не се поклопуваат со наставната програма');
    results.recommendations.push('Разгледајте додавање на проблеми кои се фокусираат на основните теми');
  }

  if (results.coverage_analysis.uncovered_topics.length > curriculumTopics.length * 0.5) {
    results.recommendations.push('Премногу теми од наставната програма не се покриени со олимписките проблеми');
  }

  const avgAlignmentScore = results.alignments.reduce((sum, a) => sum + a.alignment_score, 0) / results.total_problems;
  if (avgAlignmentScore < 60) {
    results.recommendations.push('Потребно е подобрување на усогласеноста помеѓу олимписките проблеми и наставната програма');
  }

  return results;
}

export const GET: APIRoute = async ({ request }) => {
  try {
    const url = new URL(request.url);
    const grade = url.searchParams.get('grade');
    const subject = url.searchParams.get('subject') || 'mathematics';

    const curriculumPath = path.join(process.cwd(), 'src', 'data', 'curriculum_standards.json');

    if (!fs.existsSync(curriculumPath)) {
      return new Response(JSON.stringify({
        error: 'Curriculum data not found'
      }), {
        status: 404,
        headers: {
          'Content-Type': 'application/json'
        }
      });
    }

    const curriculumData = JSON.parse(fs.readFileSync(curriculumPath, 'utf-8'));

    let responseData = curriculumData;

    // Filter by subject if specified
    if (subject && curriculumData[subject]) {
      responseData = { [subject]: curriculumData[subject] };
    }

    // Filter by grade if specified
    if (grade && subject && curriculumData[subject]?.[grade]) {
      responseData = curriculumData[subject][grade];
    }

    return new Response(JSON.stringify(responseData), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'public, max-age=3600' // Cache for 1 hour
      }
    });

  } catch (error) {
    console.error('Error fetching curriculum data:', error);
    return new Response(JSON.stringify({
      error: 'Internal server error'
    }), {
      status: 500,
      headers: {
        'Content-Type': 'application/json'
      }
    });
  }
};

// POST endpoint for saving lesson plans
export const POST: APIRoute = async ({ request }) => {
  try {
    const body = await request.json();
    const { action } = body;

    if (action === 'save_lesson_plan') {
      const { grade, subject, topic, objectives } = body;

      // Load curriculum data for alignment
      let curriculumAlignment = null;
      if (subject && grade && curriculumData[subject]?.[grade]) {
        const gradeCurriculum = curriculumData[subject][grade];
        curriculumAlignment = analyzeLessonPlanAlignment(topic, objectives, gradeCurriculum);
      }

      const lessonPlan = {
        id: `lesson_${Date.now()}`,
        ...body,
        curriculum_alignment: curriculumAlignment,
        created_at: new Date().toISOString()
      };

      // In a real implementation, save to database
      // For now, we'll just validate and return success
      console.log('Saving lesson plan:', lessonPlan);

      return new Response(JSON.stringify({
        success: true,
        message: 'Lesson plan saved successfully',
        lesson_id: lessonPlan.id,
        curriculum_alignment: curriculumAlignment
      }), {
        status: 200,
        headers: {
          'Content-Type': 'application/json'
        }
      });
    }

    if (action === 'generate_homework') {
      const { topic, grade, objectives } = body;

      // Simulate AI homework generation
      const generatedHomework = {
        topic,
        grade,
        problems: [
          {
            type: 'calculation',
            difficulty: 'basic',
            problem: `Реши ја равенката: 2x + 5 = ${Math.floor(Math.random() * 20) + 10}`,
            solution: 'x = ...'
          },
          {
            type: 'word_problem',
            difficulty: 'intermediate',
            problem: 'Во една школа има 120 ученици. 3/5 од нив се девојчиња. Колку се момчињата?',
            solution: '120 × 2/5 = 48 момчиња'
          },
          {
            type: 'geometry',
            difficulty: 'basic',
            problem: 'Нацртај правоаголник со страни 6cm и 8cm. Пресметај периметар и плоштина.',
            solution: 'P = 28cm, A = 48cm²'
          }
        ],
        generated_at: new Date().toISOString()
      };

      return new Response(JSON.stringify({
        success: true,
        homework: generatedHomework
      }), {
        status: 200,
        headers: {
          'Content-Type': 'application/json'
        }
      });
    }

    if (action === 'generate_video_concept') {
      const { topic, content, grade } = body;

      // Simulate video concept generation
      const videoConcept = {
        topic,
        grade,
        scenes: [
          {
            title: 'Вовед',
            description: `Објаснување на основниот концепт: ${topic}`,
            duration: '30 секунди'
          },
          {
            title: 'Примери',
            description: 'Практични примери со визуелизации',
            duration: '2 минути'
          },
          {
            title: 'Вежба',
            description: 'Интерактивни вежби за учениците',
            duration: '1.5 минути'
          },
          {
            title: 'Заклучок',
            description: 'Резиме на најважните поенти',
            duration: '30 секунди'
          }
        ],
        total_duration: '4.5 минути',
        generated_at: new Date().toISOString()
      };

      return new Response(JSON.stringify({
        success: true,
        video_concept: videoConcept
      }), {
        status: 200,
        headers: {
          'Content-Type': 'application/json'
        }
      });
    }

    if (action === 'analyze_curriculum_gaps') {
      const { grade, subject } = body;

      if (!curriculumData || !curriculumData[subject]?.[grade]) {
        return new Response(JSON.stringify({
          error: 'Curriculum data not found for the specified grade and subject'
        }), {
          status: 404,
          headers: {
            'Content-Type': 'application/json'
          }
        });
      }

      const gradeCurriculum = curriculumData[subject][grade];
      const gapAnalysis = performGapAnalysis(gradeCurriculum, subject, grade);

      return new Response(JSON.stringify({
        success: true,
        gap_analysis: gapAnalysis
      }), {
        status: 200,
        headers: {
          'Content-Type': 'application/json'
        }
      });
    }

    if (action === 'align_olympiad_problems') {
      const { problems, grade, subject } = body;

      if (!curriculumData || !curriculumData[subject]?.[grade]) {
        return new Response(JSON.stringify({
          error: 'Curriculum data not found for the specified grade and subject'
        }), {
          status: 404,
          headers: {
            'Content-Type': 'application/json'
          }
        });
      }

      const gradeCurriculum = curriculumData[subject][grade];
      const alignmentResults = alignProblemsWithCurriculum(problems, gradeCurriculum, grade);

      return new Response(JSON.stringify({
        success: true,
        alignment_results: alignmentResults
      }), {
        status: 200,
        headers: {
          'Content-Type': 'application/json'
        }
      });
    }

    return new Response(JSON.stringify({
      error: 'Invalid action'
    }), {
      status: 400,
      headers: {
        'Content-Type': 'application/json'
      }
    });

  } catch (error) {
    console.error('Error processing curriculum request:', error);
    return new Response(JSON.stringify({
      error: 'Internal server error'
    }), {
      status: 500,
      headers: {
        'Content-Type': 'application/json'
      }
    });
  }
};