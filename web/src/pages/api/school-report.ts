import type { APIRoute } from 'astro';
import fs from 'fs';
import path from 'path';

// Curriculum alignment analysis function
function analyzeCurriculumAlignment(schoolData: any, curriculumData: any): any {
  const alignmentAnalysis = {
    subjectAlignment: {} as any,
    gradeLevelAlignment: {} as any,
    overallAlignment: {
      score: 0,
      level: 'unknown',
      strengths: [] as string[],
      areasForImprovement: [] as string[]
    },
    recommendations: [] as string[]
  };

  // Analyze mathematics subject alignment
  if (curriculumData.mathematics && schoolData.subject_performance) {
    const mathPerformance = schoolData.subject_performance.find((subj: any) => subj.subject === 'Математика');
    if (mathPerformance) {
      alignmentAnalysis.subjectAlignment.mathematics = analyzeSubjectAlignment(mathPerformance, curriculumData.mathematics);
    }
  }

  // Analyze grade-level alignment
  if (curriculumData.mathematics && schoolData.grade_success) {
    schoolData.grade_success.forEach((gradeData: any) => {
      const gradeKey = `grade_${gradeData.class.split('-')[0].toLowerCase()}`;
      if (curriculumData.mathematics[gradeKey]) {
        alignmentAnalysis.gradeLevelAlignment[gradeData.class] = analyzeGradeAlignment(gradeData, curriculumData.mathematics[gradeKey]);
      }
    });
  }

  // Calculate overall alignment score
  const subjectScores = Object.values(alignmentAnalysis.subjectAlignment).map((subj: any) => subj?.score || 0);
  const gradeScores = Object.values(alignmentAnalysis.gradeLevelAlignment).map((grade: any) => grade?.score || 0);
  const allScores = [...subjectScores, ...gradeScores];

  if (allScores.length > 0) {
    alignmentAnalysis.overallAlignment.score = allScores.reduce((sum: number, score: number) => sum + score, 0) / allScores.length;

    // Determine alignment level
    if (alignmentAnalysis.overallAlignment.score >= 85) {
      alignmentAnalysis.overallAlignment.level = 'excellent';
    } else if (alignmentAnalysis.overallAlignment.score >= 70) {
      alignmentAnalysis.overallAlignment.level = 'good';
    } else if (alignmentAnalysis.overallAlignment.score >= 55) {
      alignmentAnalysis.overallAlignment.level = 'adequate';
    } else {
      alignmentAnalysis.overallAlignment.level = 'needs_improvement';
    }
  }

  // Generate recommendations based on analysis
  alignmentAnalysis.recommendations = generateAlignmentRecommendations(alignmentAnalysis);

  return alignmentAnalysis;
}

function analyzeSubjectAlignment(subjectData: any, curriculumGrades: any): any {
  const alignment = {
    score: 0,
    coverage: 0,
    performanceVsStandards: [] as any[],
    recommendations: [] as string[]
  };

  // Analyze performance across grades
  subjectData.grades.forEach((gradeData: any) => {
    const gradeKey = `grade_${gradeData.class.split('-')[0].toLowerCase()}`;
    const gradeCurriculum = curriculumGrades[gradeKey];

    if (gradeCurriculum) {
      const gradeAnalysis = {
        grade: gradeData.class,
        curriculumTopics: Object.keys(gradeCurriculum.themes || {}).length,
        avgGrade: gradeData['5'] * 5 + gradeData['4'] * 4 + gradeData['3'] * 3 + gradeData['2'] * 2 + gradeData['1'] * 1 /
                  (gradeData['5'] + gradeData['4'] + gradeData['3'] + gradeData['2'] + gradeData['1']),
        alignmentScore: 0
      };

      // Calculate alignment score based on grade performance vs curriculum complexity
      const topicCount = Object.keys(gradeCurriculum.themes || {}).length;
      if (topicCount > 0) {
        // Higher grades should have more complex topics - adjust expectations
        const expectedAvg = Math.min(4.5, 3.5 + (parseInt(gradeData.class.split('-')[0]) - 1) * 0.1);
        gradeAnalysis.alignmentScore = Math.max(0, Math.min(100, (gradeAnalysis.avgGrade / expectedAvg) * 100));
      }

      alignment.performanceVsStandards.push(gradeAnalysis);
    }
  });

  // Calculate overall subject alignment score
  if (alignment.performanceVsStandards.length > 0) {
    alignment.score = alignment.performanceVsStandards.reduce((sum: number, item: any) => sum + item.alignmentScore, 0) / alignment.performanceVsStandards.length;
  }

  // Calculate coverage (percentage of grades with curriculum data)
  const totalGrades = subjectData.grades.length;
  const coveredGrades = alignment.performanceVsStandards.length;
  alignment.coverage = totalGrades > 0 ? (coveredGrades / totalGrades) * 100 : 0;

  return alignment;
}

function analyzeGradeAlignment(gradeData: any, gradeCurriculum: any): any {
  const alignment = {
    score: 0,
    curriculumCoverage: 0,
    performanceIndicators: [] as string[],
    gaps: [] as string[]
  };

  // Analyze curriculum coverage
  const curriculumTopics = Object.keys(gradeCurriculum.themes || {});
  alignment.curriculumCoverage = curriculumTopics.length;

  // Performance indicators based on grade distribution
  const totalStudents = gradeData.students;
  const excellentRate = (gradeData.grades['5'] / totalStudents) * 100;
  const goodRate = (gradeData.grades['4'] / totalStudents) * 100;
  const passingRate = ((gradeData.grades['5'] + gradeData.grades['4'] + gradeData.grades['3']) / totalStudents) * 100;

  if (excellentRate > 30) alignment.performanceIndicators.push('High excellence rate');
  if (passingRate > 90) alignment.performanceIndicators.push('Strong passing rate');
  if (gradeData.stats.avg > 4.0) alignment.performanceIndicators.push('Above average performance');

  // Identify potential gaps
  if (gradeData.stats.negative > totalStudents * 0.1) {
    alignment.gaps.push('High failure rate may indicate curriculum gaps');
  }
  if (gradeData.grades['1'] > totalStudents * 0.05) {
    alignment.gaps.push('Significant number of failing students');
  }

  // Calculate alignment score based on performance and curriculum complexity
  const complexityFactor = Math.min(1, curriculumTopics.length / 10); // More topics = higher complexity
  const performanceScore = (gradeData.stats.avg / 5.0) * 100;
  alignment.score = (performanceScore * 0.7) + (complexityFactor * 30); // 70% performance, 30% curriculum coverage

  return alignment;
}

function generateAlignmentRecommendations(alignmentAnalysis: any): string[] {
  const recommendations: string[] = [];

  // Overall alignment recommendations
  const overallScore = alignmentAnalysis.overallAlignment.score;
  if (overallScore < 60) {
    recommendations.push('Consider curriculum review and additional teacher training');
    recommendations.push('Implement targeted intervention programs for struggling students');
  } else if (overallScore < 80) {
    recommendations.push('Focus on advanced topics and enrichment activities');
    recommendations.push('Strengthen support for students performing below grade level');
  } else {
    recommendations.push('Continue current successful teaching strategies');
    recommendations.push('Consider advanced curriculum extensions for high-performing students');
  }

  // Subject-specific recommendations
  Object.entries(alignmentAnalysis.subjectAlignment).forEach(([subject, analysis]: [string, any]) => {
    if (analysis.score < 70) {
      recommendations.push(`Enhance ${subject} curriculum implementation with additional resources`);
    }
    if (analysis.coverage < 80) {
      recommendations.push(`Expand ${subject} curriculum coverage across all grade levels`);
    }
  });

  // Grade-specific recommendations
  Object.entries(alignmentAnalysis.gradeLevelAlignment).forEach(([grade, analysis]: [string, any]) => {
    if (analysis.score < 65) {
      recommendations.push(`Provide additional support for ${grade} students`);
    }
    if (analysis.gaps.length > 0) {
      recommendations.push(`Address curriculum gaps in ${grade}`);
    }
  });

  return recommendations;
}

export const GET: APIRoute = async ({ request }) => {
  try {
    const dataPath = path.join(process.cwd(), 'src', 'data', 'semester_report.json');
    const curriculumPath = path.join(process.cwd(), 'src', 'data', 'curriculum_standards.json');

    if (!fs.existsSync(dataPath)) {
      return new Response(JSON.stringify({
        error: 'School report data not found'
      }), {
        status: 404,
        headers: {
          'Content-Type': 'application/json'
        }
      });
    }

    const data = JSON.parse(fs.readFileSync(dataPath, 'utf-8'));
    const curriculumData = fs.existsSync(curriculumPath) ? JSON.parse(fs.readFileSync(curriculumPath, 'utf-8')) : null;

    // Add computed fields
    const enhancedData = {
      ...data,
      summary: {
        totalStudents: data.attendance_summary.reduce((sum: number, item: any) => sum + item.total, 0),
        totalExcused: data.attendance_summary.reduce((sum: number, item: any) => sum + item.absences.excused, 0),
        totalUnexcused: data.attendance_summary.reduce((sum: number, item: any) => sum + item.absences.unexcused, 0),
        avgGrade: data.grade_success.reduce((sum: number, item: any) => sum + (item.stats.avg * item.students), 0) /
                  data.grade_success.reduce((sum: number, item: any) => sum + item.students, 0),
        passRate: (data.grade_success.reduce((sum: number, item: any) => sum + item.stats.passed, 0) /
                   data.grade_success.reduce((sum: number, item: any) => sum + item.students, 0) * 100).toFixed(1)
      },
      generatedAt: new Date().toISOString(),
      semester: '2025/26 - Прво полугодие'
    };

    // Add curriculum alignment analysis if curriculum data is available
    if (curriculumData && curriculumData.mathematics) {
      enhancedData.curriculumAlignment = analyzeCurriculumAlignment(data, curriculumData);
    }

    return new Response(JSON.stringify(enhancedData), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'public, max-age=300' // Cache for 5 minutes
      }
    });

  } catch (error) {
    console.error('Error fetching school report data:', error);
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

export const POST: APIRoute = async ({ request }) => {
  try {
    const body = await request.json();

    // Validate the incoming data structure
    if (!body.attendance_summary || !body.grade_success) {
      return new Response(JSON.stringify({
        error: 'Invalid data structure. Required: attendance_summary, grade_success'
      }), {
        status: 400,
        headers: {
          'Content-Type': 'application/json'
        }
      });
    }

    // In a real implementation, you would save this to a database
    // For now, we'll just validate and return success
    const dataPath = path.join(process.cwd(), 'src', 'data', 'semester_report.json');

    // Create backup of existing data
    if (fs.existsSync(dataPath)) {
      const backupPath = path.join(process.cwd(), 'src', 'data', `semester_report_backup_${Date.now()}.json`);
      fs.copyFileSync(dataPath, backupPath);
    }

    // Save new data (in real implementation, validate more thoroughly)
    fs.writeFileSync(dataPath, JSON.stringify(body, null, 2), 'utf-8');

    return new Response(JSON.stringify({
      success: true,
      message: 'School report data updated successfully',
      timestamp: new Date().toISOString()
    }), {
      status: 200,
      headers: {
        'Content-Type': 'application/json'
      }
    });

  } catch (error) {
    console.error('Error updating school report data:', error);
    return new Response(JSON.stringify({
      error: 'Failed to update school report data'
    }), {
      status: 500,
      headers: {
        'Content-Type': 'application/json'
      }
    });
  }
};