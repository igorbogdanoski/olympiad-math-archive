import type { APIRoute } from 'astro';
import type { AssessmentData, AssessmentSummary, StudentProgress } from '../../types/assessment';

// In-memory storage for assessments (in a real app, this would be a database)
let assessments: AssessmentData[] = [];

export const GET: APIRoute = async ({ request }) => {
  const url = new URL(request.url);
  const action = url.searchParams.get('action');
  const studentId = url.searchParams.get('studentId');
  const lessonId = url.searchParams.get('lessonId');

  try {
    switch (action) {
      case 'student':
        if (!studentId) {
          return new Response(JSON.stringify({ error: 'Student ID is required' }), {
            status: 400,
            headers: { 'Content-Type': 'application/json' }
          });
        }
        const studentAssessments = assessments.filter(a => a.studentId === studentId);
        const studentProgress = calculateStudentProgress(studentId, studentAssessments);

        return new Response(JSON.stringify({
          success: true,
          assessments: studentAssessments,
          progress: studentProgress
        }), {
          status: 200,
          headers: { 'Content-Type': 'application/json' }
        });

      case 'lesson':
        if (!lessonId) {
          return new Response(JSON.stringify({ error: 'Lesson ID is required' }), {
            status: 400,
            headers: { 'Content-Type': 'application/json' }
          });
        }
        const lessonAssessments = assessments.filter(a => a.lessonId === lessonId);
        const summary = calculateAssessmentSummary(lessonAssessments);

        return new Response(JSON.stringify({
          success: true,
          assessments: lessonAssessments,
          summary
        }), {
          status: 200,
          headers: { 'Content-Type': 'application/json' }
        });

      case 'summary':
        const allSummary = calculateAssessmentSummary(assessments);
        return new Response(JSON.stringify({
          success: true,
          summary: allSummary
        }), {
          status: 200,
          headers: { 'Content-Type': 'application/json' }
        });

      default:
        return new Response(JSON.stringify({
          success: true,
          assessments,
          total: assessments.length
        }), {
          status: 200,
          headers: { 'Content-Type': 'application/json' }
        });
    }
  } catch (error) {
    return new Response(JSON.stringify({
      error: 'Internal server error',
      details: error instanceof Error ? error.message : 'Unknown error'
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};

export const POST: APIRoute = async ({ request }) => {
  try {
    const assessmentData: AssessmentData = await request.json();

    // Validate required fields
    if (!assessmentData.studentId || !assessmentData.lessonId) {
      return new Response(JSON.stringify({
        error: 'Student ID and Lesson ID are required'
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Add timestamp if not provided
    if (!assessmentData.timestamp) {
      assessmentData.timestamp = new Date().toISOString();
    }

    // Check if assessment already exists (for updates)
    const existingIndex = assessments.findIndex(
      a => a.studentId === assessmentData.studentId && a.lessonId === assessmentData.lessonId
    );

    if (existingIndex >= 0) {
      // Update existing assessment
      assessments[existingIndex] = { ...assessments[existingIndex], ...assessmentData };
    } else {
      // Add new assessment
      assessments.push(assessmentData);
    }

    return new Response(JSON.stringify({
      success: true,
      message: existingIndex >= 0 ? 'Assessment updated successfully' : 'Assessment created successfully',
      assessment: assessmentData
    }), {
      status: 201,
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    return new Response(JSON.stringify({
      error: 'Failed to save assessment',
      details: error instanceof Error ? error.message : 'Unknown error'
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};

export const DELETE: APIRoute = async ({ request }) => {
  try {
    const url = new URL(request.url);
    const studentId = url.searchParams.get('studentId');
    const lessonId = url.searchParams.get('lessonId');

    if (!studentId || !lessonId) {
      return new Response(JSON.stringify({
        error: 'Student ID and Lesson ID are required'
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const initialLength = assessments.length;
    assessments = assessments.filter(
      a => !(a.studentId === studentId && a.lessonId === lessonId)
    );

    const deleted = initialLength - assessments.length;

    return new Response(JSON.stringify({
      success: true,
      message: `Deleted ${deleted} assessment(s)`
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    return new Response(JSON.stringify({
      error: 'Failed to delete assessment',
      details: error instanceof Error ? error.message : 'Unknown error'
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};

// Helper functions for calculations
function calculateStudentProgress(studentId: string, studentAssessments: AssessmentData[]): StudentProgress {
  const sortedAssessments = studentAssessments.sort((a, b) =>
    new Date(a.timestamp).getTime() - new Date(b.timestamp).getTime()
  );

  const latestAssessment = sortedAssessments[sortedAssessments.length - 1];
  const earliestAssessment = sortedAssessments[0];

  let trend: 'improving' | 'stable' | 'declining' = 'stable';
  if (sortedAssessments.length >= 2) {
    const improvement = latestAssessment.progressMetrics.overallScore - earliestAssessment.progressMetrics.overallScore;
    if (improvement > 0.5) trend = 'improving';
    else if (improvement < -0.5) trend = 'declining';
  }

  const currentLevel = latestAssessment?.progressMetrics.overallScore || 3;
  const targetLevel = 5; // Could be configurable
  const progressPercentage = (currentLevel / targetLevel) * 100;

  // Collect all recommendations
  const allRecommendations = studentAssessments.flatMap(a => a.recommendations);
  const uniqueRecommendations = [...new Set(allRecommendations)];

  return {
    studentId,
    studentName: latestAssessment?.studentName || 'Unknown Student',
    assessments: sortedAssessments,
    overallProgress: {
      currentLevel,
      targetLevel,
      progressPercentage,
      trend
    },
    recommendations: uniqueRecommendations.slice(0, 5), // Top 5 recommendations
    nextSteps: generateNextSteps(latestAssessment)
  };
}

function calculateAssessmentSummary(assessmentList: AssessmentData[]): AssessmentSummary {
  if (assessmentList.length === 0) {
    return {
      totalAssessments: 0,
      averageScore: 0,
      improvementRate: 0,
      topStrengths: [],
      commonChallenges: [],
      recommendations: []
    };
  }

  const totalAssessments = assessmentList.length;
  const averageScore = assessmentList.reduce((sum, a) => sum + a.progressMetrics.overallScore, 0) / totalAssessments;

  // Calculate improvement rate (simplified)
  const improvingCount = assessmentList.filter(a => a.progressMetrics.trend === 'improving').length;
  const improvementRate = (improvingCount / totalAssessments) * 100;

  // Collect strengths and challenges
  const allStrengths = assessmentList.flatMap(a => a.progressMetrics.strengths);
  const allChallenges = assessmentList.flatMap(a => a.progressMetrics.areasForImprovement);
  const allRecommendations = assessmentList.flatMap(a => a.recommendations);

  // Get most common items (simplified frequency count)
  const topStrengths = getMostCommon(allStrengths, 5);
  const commonChallenges = getMostCommon(allChallenges, 5);
  const topRecommendations = getMostCommon(allRecommendations, 5);

  return {
    totalAssessments,
    averageScore: Math.round(averageScore * 10) / 10,
    improvementRate: Math.round(improvementRate),
    topStrengths,
    commonChallenges,
    recommendations: topRecommendations
  };
}

function getMostCommon(items: string[], limit: number): string[] {
  const frequency: { [key: string]: number } = {};

  items.forEach(item => {
    if (item.trim()) {
      frequency[item.trim()] = (frequency[item.trim()] || 0) + 1;
    }
  });

  return Object.entries(frequency)
    .sort(([,a], [,b]) => b - a)
    .slice(0, limit)
    .map(([item]) => item);
}

function generateNextSteps(latestAssessment?: AssessmentData): string[] {
  if (!latestAssessment) return ['Continue regular assessments'];

  const steps: string[] = [];

  // Based on competencies
  latestAssessment.competencies.forEach(comp => {
    if (comp.score < 3) {
      steps.push(`Focus on improving ${comp.skill.toLowerCase()}`);
    }
  });

  // Based on progress trend
  if (latestAssessment.progressMetrics.trend === 'declining') {
    steps.push('Schedule additional support sessions');
  }

  // Based on engagement
  if (latestAssessment.progressMetrics.engagementLevel < 3) {
    steps.push('Implement engagement improvement strategies');
  }

  // Default steps
  if (steps.length === 0) {
    steps.push('Continue with current learning plan');
    steps.push('Prepare for next assessment cycle');
  }

  return steps.slice(0, 3);
}