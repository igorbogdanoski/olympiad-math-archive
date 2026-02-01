// Phase 1: AI-Powered Recommendation Engine API
// Demonstrates collaborative filtering and content-based recommendations

import type { APIRoute } from 'astro';
import { AI_API_BASE_URL } from '../../utils/config';
import nationalStandards from '../../data/national_standards.json';

interface RecommendationQuery {
  userId?: string;
  selectedItems: string[]; // Standard codes or curriculum topics
  context: {
    grade?: string;
    subject?: string;
    currentTopic?: string;
  };
  preferences?: {
    difficulty?: 'easy' | 'medium' | 'hard';
    focus?: 'olympiad' | 'curriculum' | 'mixed';
  };
}

interface Recommendation {
  id: string;
  type: 'standard' | 'olympiad' | 'curriculum' | 'teaching_strategy';
  title: string;
  description: string;
  confidence: number; // 0-1, how confident the AI is in this recommendation
  reason: string;
  metadata: {
    grade?: string;
    subject?: string;
    difficulty?: string;
    prerequisites?: string[];
  };
}

interface AIRecommendationResponse {
  recommendations: Recommendation[];
  personalizedInsights: string[];
  nextBestActions: string[];
  processingTime: number;
  modelVersion: string;
}

// Mock user interaction history (Phase 1 foundation)
// In production: This would come from a database
const mockUserHistory: Record<string, Array<{item: string, interaction: string, timestamp: number}>> = {
  'teacher_123': [
    { item: 'M1.1.1', interaction: 'viewed', timestamp: Date.now() - 86400000 },
    { item: 'algebra', interaction: 'selected', timestamp: Date.now() - 3600000 },
    { item: 'geometry', interaction: 'searched', timestamp: Date.now() - 1800000 }
  ]
};

// Macedonian teaching strategy recommendations
const teachingStrategies = {
  'problem_based': {
    title: 'Проблем-базирано учење',
    description: 'Користење на олимписки задачи за развивање критичко мислење',
    applicableTo: ['algebra', 'geometry', 'number_theory']
  },
  'collaborative': {
    title: 'Колаборативна работа',
    description: 'Групни решенија на комплексни математички проблеми',
    applicableTo: ['systems', 'combinatorics', 'inequalities']
  },
  'differentiated': {
    title: 'Диференцирана инструкција',
    description: 'Прилагодување на задачи според ниво на учениците',
    applicableTo: ['mixed_difficulty', 'remedial', 'enrichment']
  }
};

export const POST: APIRoute = async ({ request }) => {
  try {
    const query: RecommendationQuery = await request.json();
    const startTime = Date.now();

    let aiRecommendations;
    let modelUsed = 'Macedonian-Math-Recommendation-Engine-v1.5';

    try {
      // Try calling the real AI API
      const aiResponse = await fetch(`${AI_API_BASE_URL}/ai-recommend`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(query)
      });

      if (aiResponse.ok) {
        aiRecommendations = await aiResponse.json();
      } else {
        throw new Error('AI API returned error');
      }
    } catch (e) {
      console.warn('AI API failed, falling back to mocks:', e);
      const mockResult = await generateAIRecommendations(query);
      aiRecommendations = {
        recommendations: mockResult.recommendations,
        personalizedInsights: mockResult.insights,
        nextBestActions: mockResult.actions
      };
      modelUsed = 'Phase1-Collaborative-Filtering-v0.1';
    }

    const processingTime = Date.now() - startTime;

    const response: AIRecommendationResponse = {
      recommendations: aiRecommendations.recommendations,
      personalizedInsights: aiRecommendations.personalizedInsights,
      nextBestActions: aiRecommendations.nextBestActions,
      processingTime,
      modelVersion: modelUsed
    };

    return new Response(JSON.stringify(response), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'X-AI-Model': modelUsed,
        'X-Processing-Time': `${processingTime}ms`
      }
    });

  } catch (error) {
    console.error('AI Recommendation API error:', error);
    return new Response(JSON.stringify({
      error: 'AI recommendation failed',
      recommendations: []
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};

// Mock AI recommendation generation (Phase 1)
async function generateAIRecommendations(query: RecommendationQuery) {
  const recommendations: Recommendation[] = [];
  const insights: string[] = [];
  const actions: string[] = [];

  // Content-based filtering based on selected items
  query.selectedItems.forEach(item => {
    const similarItems = findSimilarContent(item, query.context);

    similarItems.forEach(similar => {
      if (!query.selectedItems.includes(similar.id)) {
        recommendations.push({
          id: similar.id,
          type: similar.type,
          title: similar.title,
          description: similar.description,
          confidence: similar.confidence,
          reason: similar.reason,
          metadata: {
            grade: query.context.grade,
            subject: query.context.subject,
            difficulty: similar.difficulty,
            prerequisites: similar.prerequisites
          }
        });
      }
    });
  });

  // Collaborative filtering based on user history
  if (query.userId && mockUserHistory[query.userId]) {
    const collaborativeRecs = generateCollaborativeRecommendations(
      query.userId,
      query.selectedItems
    );
    recommendations.push(...collaborativeRecs);
  }

  // Generate personalized insights
  insights.push(
    'Врз основа на вашите преференции, препорачуваме фокус на олимписки задачи',
    'Учениците од овој одделение одлично реагираат на визуелизации',
    'Размислете за диференцирана инструкција за подобри резултати'
  );

  // Suggest next best actions
  actions.push(
    'Истражете олимписки проблеми поврзани со стандардот',
    'Креирајте настава со Bloom\'s таксономија',
    'Додајте визуелизации за подобро разбирање'
  );

  return {
    recommendations: recommendations.slice(0, 8), // Limit to 8 recommendations
    insights,
    actions
  };
}

// Content similarity matching (Phase 1)
function findSimilarContent(itemId: string, context: any) {
  const similar: any[] = [];

  // Find similar standards
  Object.values(nationalStandards.национални_стандарди[0].знаења_и_вештини).forEach(standard => {
    if (standard.шифра !== itemId) {
      const similarity = calculateContentSimilarity(
        getStandardContent(itemId),
        standard.опис
      );

      if (similarity > 0.4) { // Higher threshold for recommendations
        similar.push({
          id: standard.шифра,
          type: 'standard',
          title: standard.опис.substring(0, 80) + '...',
          description: standard.опис,
          confidence: similarity,
          reason: 'Слична математичка содржина',
          difficulty: context.grade ? 'medium' : 'mixed',
          prerequisites: []
        });
      }
    }
  });

  // Add teaching strategy recommendations
  Object.entries(teachingStrategies).forEach(([key, strategy]) => {
    if (strategy.applicableTo.some(topic => itemId.includes(topic) || context.subject === topic)) {
      similar.push({
        id: key,
        type: 'teaching_strategy',
        title: strategy.title,
        description: strategy.description,
        confidence: 0.8,
        reason: 'Ефективна стратегија за оваа тема',
        difficulty: 'mixed',
        prerequisites: []
      });
    }
  });

  return similar;
}

// Get standard content by ID
function getStandardContent(standardId: string): string {
  const standardsObj = nationalStandards.национални_стандарди[0].знаења_и_вештини as any;
  const standard = standardsObj[standardId];
  return standard ? standard.опис : '';
}

// Simple content similarity calculation
function calculateContentSimilarity(text1: string, text2: string): number {
  if (!text1 || !text2) return 0;

  const words1 = new Set(text1.toLowerCase().split(/\s+/));
  const words2 = new Set(text2.toLowerCase().split(/\s+/));

  const intersection = new Set([...words1].filter(x => words2.has(x)));
  const union = new Set([...words1, ...words2]);

  return intersection.size / union.size;
}

// Mock collaborative filtering (Phase 1)
function generateCollaborativeRecommendations(userId: string, selectedItems: string[]): Recommendation[] {
  const recommendations: Recommendation[] = [];

  // Based on user history, recommend related items
  const userInteractions = mockUserHistory[userId] || [];

  // Find patterns in user behavior
  const preferredTopics = userInteractions
    .filter(interaction => interaction.interaction === 'selected')
    .map(interaction => interaction.item);

  // Recommend items similar to preferred topics
  preferredTopics.forEach(topic => {
    if (!selectedItems.includes(topic)) {
      recommendations.push({
        id: `${topic}_advanced`,
        type: 'curriculum',
        title: `Напредни концепти за ${topic}`,
        description: `Продлабочени теми поврзани со ${topic}`,
        confidence: 0.7,
        reason: 'Врз основа на вашите претходни избори',
        metadata: {
          subject: topic,
          difficulty: 'advanced'
        }
      });
    }
  });

  return recommendations;
}