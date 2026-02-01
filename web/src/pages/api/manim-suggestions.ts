import type { APIRoute } from 'astro';
import { readdirSync, readFileSync } from 'fs';
import { join } from 'path';

interface ManimTemplate {
  id: string;
  title: string;
  grade: string;
  category: string;
  score: number;
  description: string;
  keywords: string[];
  content: string;
}

export const GET: APIRoute = async ({ request }) => {
  try {
    const url = new URL(request.url);
    const topic = url.searchParams.get('topic') || '';
    const grade = url.searchParams.get('grade') || '';
    const category = url.searchParams.get('category') || '';

    const templates = await loadManimTemplates();

    // Filter templates based on criteria
    let relevantTemplates = templates.filter(template => {
      // Always include templates if no filters provided
      if (!topic && !grade && !category) return true;

      let isRelevant = false;

      // Check grade match
      if (grade && template.grade.includes(grade.replace('grade_', ''))) {
        isRelevant = true;
      }

      // Check topic keywords in description or content
      if (topic) {
        const topicLower = topic.toLowerCase();
        const descriptionMatch = template.description.toLowerCase().includes(topicLower);
        const keywordMatch = template.keywords.some(keyword =>
          topicLower.includes(keyword.toLowerCase()) ||
          keyword.toLowerCase().includes(topicLower)
        );
        const contentMatch = template.content.toLowerCase().includes(topicLower);

        if (descriptionMatch || keywordMatch || contentMatch) {
          isRelevant = true;
        }
      }

      // Check category match
      if (category && template.category.toLowerCase().includes(category.toLowerCase())) {
        isRelevant = true;
      }

      return isRelevant;
    });

    // If no templates match, return general geometry/algebra templates
    if (relevantTemplates.length === 0 && (topic || grade)) {
      relevantTemplates = templates
        .filter(template => template.category === 'geometry' || template.category === 'algebra')
        .slice(0, 3);
    }

    // Sort by relevance and score
    relevantTemplates.sort((a, b) => {
      // Prioritize exact grade matches
      if (grade && a.grade.includes(grade.replace('grade_', '')) &&
          !b.grade.includes(grade.replace('grade_', ''))) return -1;
      if (grade && !a.grade.includes(grade.replace('grade_', '')) &&
          b.grade.includes(grade.replace('grade_', ''))) return 1;

      // Then sort by score (higher is better for olympiad problems)
      return b.score - a.score;
    });

    // Return top 5 most relevant templates
    const topTemplates = relevantTemplates.slice(0, 5);

    return new Response(JSON.stringify({
      success: true,
      templates: topTemplates,
      totalFound: relevantTemplates.length,
      searchCriteria: { topic, grade, category }
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    console.error('Error fetching Manim suggestions:', error);
    return new Response(JSON.stringify({
      success: false,
      error: 'Failed to fetch Manim template suggestions'
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};

async function loadManimTemplates(): Promise<ManimTemplate[]> {
  const templates: ManimTemplate[] = [];

  try {
    // Load templates from tools/manim_templates directory
    const templateDir = join(process.cwd(), 'tools', 'manim_templates');

    // Check for subdirectories
    const subdirs = readdirSync(templateDir, { withFileTypes: true })
      .filter(dirent => dirent.isDirectory())
      .map(dirent => dirent.name);

    for (const subdir of subdirs) {
      const subdirPath = join(templateDir, subdir);

      try {
        const files = readdirSync(subdirPath)
          .filter(file => file.endsWith('.py'))
          .map(file => join(subdirPath, file));

        for (const file of files) {
          try {
            const content = readFileSync(file, 'utf-8');
            const template = parseManimTemplate(content, file);
            if (template) {
              templates.push(template);
            }
          } catch (fileError) {
            console.warn(`Failed to read template file ${file}:`, fileError);
          }
        }
      } catch (subdirError) {
        console.warn(`Failed to read subdirectory ${subdir}:`, subdirError);
      }
    }
  } catch (error) {
    console.error('Error loading Manim templates:', error);
  }

  return templates;
}

function parseManimTemplate(content: string, filePath: string): ManimTemplate | null {
  try {
    // Extract template information from content and file path
    const filename = filePath.split('/').pop() || '';

    // Try to extract problem ID from filename (e.g., manim_2025_mun_g8_2.py)
    const problemMatch = filename.match(/manim_(\w+)\.py/);
    const problemId = problemMatch ? problemMatch[1] : filename.replace('.py', '');

    // Extract grade from filename or content
    let grade = '8'; // default
    const gradeMatch = filename.match(/g(\d+)/);
    if (gradeMatch) {
      grade = gradeMatch[1];
    }

    // Extract category from filename or content
    let category = 'geometry'; // default
    if (filename.includes('geo')) {
      category = 'geometry';
    } else if (filename.includes('alg') || filename.includes('func')) {
      category = 'algebra';
    } else if (filename.includes('tri')) {
      category = 'trigonometry';
    }

    // Extract score/rank from content
    let score = 100; // default
    const scoreMatch = content.match(/Rank:\s*(\d+).*Score:\s*(\d+)/);
    if (scoreMatch) {
      score = parseInt(scoreMatch[2]);
    }

    // Extract description
    let description = 'Mathematical animation template';
    const descMatch = content.match(/Problem Description:\s*(.+?)(?=\n\n|$)/s);
    if (descMatch) {
      description = descMatch[1].trim().replace(/\s+/g, ' ');
    }

    // Generate keywords from content
    const keywords = extractKeywords(content);

    return {
      id: problemId,
      title: `Problem ${problemId}`,
      grade,
      category,
      score,
      description,
      keywords,
      content
    };
  } catch (error) {
    console.error('Error parsing Manim template:', error);
    return null;
  }
}

function extractKeywords(content: string): string[] {
  const keywords = new Set<string>();

  // Extract mathematical terms
  const mathTerms = [
    'trapezoid', 'triangle', 'circle', 'square', 'rectangle', 'parallelogram',
    'angle', 'diagonal', 'hypotenuse', 'theorem', 'pythagoras', 'area', 'perimeter',
    'equation', 'function', 'derivative', 'integral', 'vector', 'matrix',
    'sinus', 'cosinus', 'tangent', 'trigonometry'
  ];

  const contentLower = content.toLowerCase();
  for (const term of mathTerms) {
    if (contentLower.includes(term)) {
      keywords.add(term);
    }
  }

  // Extract Macedonian mathematical terms
  const mkMathTerms = [
    'трапез', 'троаголник', 'круг', 'квадрат', 'правоаголник', 'паралелограм',
    'агол', 'дијагонала', 'хипотенуза', 'теорема', 'питагора', 'површина', 'периметар',
    'равенка', 'функција', 'извод', 'интеграл', 'вектор', 'матрица',
    'синус', 'косинус', 'тангенс', 'тригонометрија'
  ];

  for (const term of mkMathTerms) {
    if (contentLower.includes(term)) {
      keywords.add(term);
    }
  }

  return Array.from(keywords);
}