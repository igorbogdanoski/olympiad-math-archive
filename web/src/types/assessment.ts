// Assessment types for student progress tracking

export interface AssessmentData {
  studentId: string;
  lessonId: string;
  competencies: CompetencyScore[];
  progressMetrics: ProgressData;
  recommendations: string[];
  timestamp: string;
  studentName?: string;
  assessmentDate?: string;
  subject?: string;
  grade?: string;
}

export interface CompetencyScore {
  skill: string;
  score: number; // 1-5 scale
  feedback: string;
  improvement: string;
}

export interface ProgressData {
  overallScore: number;
  trend: 'improving' | 'stable' | 'declining';
  strengths: string[];
  areasForImprovement: string[];
  engagementLevel: number; // 1-5
}

export interface AssessmentSummary {
  totalAssessments: number;
  averageScore: number;
  improvementRate: number;
  topStrengths: string[];
  commonChallenges: string[];
  recommendations: string[];
}

export interface StudentProgress {
  studentId: string;
  studentName: string;
  assessments: AssessmentData[];
  overallProgress: {
    currentLevel: number;
    targetLevel: number;
    progressPercentage: number;
    trend: 'improving' | 'stable' | 'declining';
  };
  recommendations: string[];
  nextSteps: string[];
}