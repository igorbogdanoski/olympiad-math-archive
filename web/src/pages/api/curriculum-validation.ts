import type { APIRoute } from 'astro';
import curriculumData from '../../data/complete_math_curriculum.json';
import nationalStandards from '../../data/national_standards.json';

export const POST: APIRoute = async ({ request }) => {
  try {
    const body = await request.json();
    const { grade, section, lessonPlan } = body;

    // Validate required fields
    if (!grade || !section || !lessonPlan) {
      return new Response(JSON.stringify({
        error: 'Missing required fields: grade, section, lessonPlan'
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Check if grade and section exist in curriculum
    const curriculumSection = (curriculumData.subjects.mathematics as any)[section];
    if (!curriculumSection || !curriculumSection[grade]) {
      return new Response(JSON.stringify({
        error: `Invalid grade or section: ${section}/${grade}`
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const gradeCurriculum = curriculumSection[grade];
    const validationResults: {
      compliance: boolean;
      issues: Array<{ type: string; severity: string; message: string }>;
      suggestions: Array<{ type: string; message: string }>;
      standards_alignment: Array<{ topic: string; alignment: string; coverage: string }>;
    } = {
      compliance: true,
      issues: [],
      suggestions: [],
      standards_alignment: []
    };

    // Validate lesson objectives against curriculum standards
    const curriculumTopics = gradeCurriculum.topics || [];
    const lessonObjectives = lessonPlan.objectives || [];
    const lessonContent = lessonPlan.content || '';

    // Check topic alignment
    let topicAligned = false;
    for (const topic of curriculumTopics) {
      if (lessonContent.toLowerCase().includes(topic.name.toLowerCase())) {
        topicAligned = true;
        validationResults.standards_alignment.push({
          topic: topic.name,
          alignment: 'direct',
          coverage: 'partial'
        });
        break;
      }
    }

    if (!topicAligned) {
      validationResults.issues.push({
        type: 'topic_alignment',
        severity: 'warning',
        message: 'Наставата не е директно поврзана со дефинираните наставни теми'
      });
    }

    // Validate learning objectives
    if (lessonObjectives.length === 0) {
      validationResults.issues.push({
        type: 'objectives',
        severity: 'error',
        message: 'Нема дефинирани цели на учење'
      });
    } else {
      // Check against national standards
      const mathStandards = nationalStandards.mathematics_standards;
      const crossCurricular = mathStandards.cross_curricular_competences;

      let objectivesAligned = false;
      for (const objective of lessonObjectives) {
        for (const competence of Object.values(crossCurricular)) {
          if (competence.indicators.some(indicator =>
            objective.toLowerCase().includes(indicator.toLowerCase().slice(0, 20))
          )) {
            objectivesAligned = true;
            break;
          }
        }
      }

      if (!objectivesAligned) {
        validationResults.suggestions.push({
          type: 'standards_alignment',
          message: 'Размислете за вклучување на цели кои развиваат критичко размислување или комуникациски вештини'
        });
      }
    }

    // Validate duration
    const lessonDuration = parseInt(lessonPlan.duration);
    const expectedWeeklyHours = gradeCurriculum.weekly_hours || 3;

    if (lessonDuration > expectedWeeklyHours * 60) {
      validationResults.issues.push({
        type: 'duration',
        severity: 'warning',
        message: `Времетраењето (${lessonDuration} мин) надминува препорачаното за овој одделение (${expectedWeeklyHours * 60} мин неделно)`
      });
    }

    // Check for assessment inclusion
    if (!lessonPlan.homework && !lessonPlan.assessment) {
      validationResults.suggestions.push({
        type: 'assessment',
        message: 'Размислете за вклучување на форми за проверка на учењето'
      });
    }

    // Determine overall compliance
    validationResults.compliance = !validationResults.issues.some(
      issue => issue.severity === 'error'
    );

    return new Response(JSON.stringify(validationResults), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    console.error('Curriculum validation error:', error);
    return new Response(JSON.stringify({
      error: 'Internal server error during validation'
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};