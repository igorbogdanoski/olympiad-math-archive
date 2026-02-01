// Phase 1: AI-Powered Semantic Search API
// This demonstrates transformer model integration for Macedonian mathematical content

import type { APIRoute } from 'astro';
import { AI_API_BASE_URL } from '../../utils/config';
import nationalStandards from '../../data/national_standards.json';
import standardsMapping from '../../data/standards_mapping.json';

// Mock transformer model responses (Phase 1 foundation)
// In production, this would be replaced with real BERT/RoBERTa inferences

interface SearchQuery {
  query: string;
  context?: {
    grade?: string;
    subject?: string;
    language?: string;
  };
}

interface SearchResult {
  id: string;
  type: 'standard' | 'olympiad' | 'curriculum';
  title: string;
  content: string;
  relevanceScore: number;
  embeddings: number[]; // Mock embeddings
  metadata: {
    grade?: string;
    subject?: string;
    difficulty?: string;
  };
}

interface AIResponse {
  results: SearchResult[];
  suggestions: string[];
  processingTime: number;
  modelVersion: string;
}

// Macedonian mathematical terminology embeddings (Phase 1 data)
const macedonianMathEmbeddings: Record<string, number[]> = {
  'прости броеви': [0.8, 0.2, 0.1, 0.9, 0.3],
  'квадратни равенки': [0.1, 0.9, 0.8, 0.2, 0.5],
  'триаголник': [0.3, 0.4, 0.9, 0.1, 0.7],
  'геометрија': [0.2, 0.3, 0.8, 0.1, 0.9],
  'алгебра': [0.9, 0.1, 0.2, 0.8, 0.4],
  'систем равенки': [0.7, 0.8, 0.1, 0.6, 0.2],
  'проценти': [0.4, 0.6, 0.3, 0.9, 0.1],
  'функции': [0.5, 0.9, 0.4, 0.2, 0.8]
};

export const POST: APIRoute = async ({ request }) => {
  try {
    const { query, context }: SearchQuery = await request.json();

    if (!query || query.trim().length < 2) {
      return new Response(JSON.stringify({
        error: 'Query too short',
        results: [],
        suggestions: []
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const startTime = Date.now();

    let aiResults;
    let modelUsed = 'Macedonian-Math-BERT-v1.5';

    try {
      // Try calling the real AI API
      const aiResponse = await fetch(`${AI_API_BASE_URL}/ai-search`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query, context })
      });

      if (aiResponse.ok) {
        aiResults = await aiResponse.json();
      } else {
        throw new Error('AI API returned error');
      }
    } catch (e) {
      console.warn('AI API failed, falling back to mocks:', e);
      aiResults = await processQueryWithTransformers(query, context);
      modelUsed = 'Phase1-Mock-Transformer-v0.1';
    }

    const processingTime = Date.now() - startTime;

    const response: AIResponse = {
      results: aiResults.results,
      suggestions: aiResults.suggestions,
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
    console.error('AI Search API error:', error);
    return new Response(JSON.stringify({
      error: 'AI search failed',
      results: [],
      suggestions: []
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};

// Mock transformer model processing (Phase 1)
async function processQueryWithTransformers(query: string, context?: any) {
  const queryLower = query.toLowerCase();

  // Find semantic matches using mock embeddings
  const results: SearchResult[] = [];
  const suggestions: string[] = [];

  // Search standards with semantic similarity
  Object.values(nationalStandards.национални_стандарди[0].знаења_и_вештини).forEach(standard => {
    const content = `${standard.шифра} ${standard.опис}`.toLowerCase();
    const similarity = calculateSemanticSimilarity(queryLower, content);

    if (similarity > 0.3) { // Similarity threshold
      results.push({
        id: standard.шифра,
        type: 'standard',
        title: standard.опис.substring(0, 100) + '...',
        content: standard.опис,
        relevanceScore: similarity,
        embeddings: generateMockEmbeddings(standard.опис),
        metadata: {
          grade: context?.grade,
          subject: 'matematika'
        }
      });
    }
  });

  // Generate contextual suggestions
  suggestions.push(
    'прости броеви и квадрати',
    'линеарни равенки',
    'геометриски фигури',
    'системи равенки'
  );

  // Add Olympiad problem suggestions based on context
  if (context?.grade) {
    const gradeNum = context.grade.replace('grade_', '');
    const olympiadSuggestions = getGradeAppropriateProblems(gradeNum);
    suggestions.push(...olympiadSuggestions);
  }

  return { results: results.slice(0, 10), suggestions: [...new Set(suggestions)] };
}

// Mock semantic similarity calculation (Phase 1)
// In production: Use cosine similarity on real embeddings
function calculateSemanticSimilarity(query: string, content: string): number {
  const queryWords = query.split(/\s+/);
  const contentWords = content.split(/\s+/);

  let matches = 0;
  queryWords.forEach(qWord => {
    contentWords.forEach(cWord => {
      if (cWord.includes(qWord) || qWord.includes(cWord)) {
        matches++;
      }
    });
  });

  return Math.min(matches / queryWords.length, 1.0);
}

// Generate mock embeddings (Phase 1 placeholder)
// In production: Real transformer model embeddings
function generateMockEmbeddings(text: string): number[] {
  const words = text.toLowerCase().split(/\s+/);
  let embedding = [0.5, 0.5, 0.5, 0.5, 0.5]; // Base embedding

  words.forEach(word => {
    if (macedonianMathEmbeddings[word]) {
      // Combine embeddings (simple average)
      embedding = embedding.map((val, i) =>
        (val + macedonianMathEmbeddings[word][i]) / 2
      );
    }
  });

  return embedding;
}

// Get grade-appropriate Olympiad problems (Phase 1 data)
function getGradeAppropriateProblems(grade: string): string[] {
  const gradeProblems: Record<string, string[]> = {
    '7': ['прости броеви', 'квадратни равенки'],
    '8': ['геометриски трансформации', 'систем равенки'],
    '9': ['комбинаторика', 'нееднакости']
  };

  return gradeProblems[grade] || ['олимписки проблеми'];
}