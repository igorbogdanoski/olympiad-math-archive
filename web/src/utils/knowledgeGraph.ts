/**
 * Knowledge Graph Utility - Adaptive Learning Path Engine
 * 
 * Provides prerequisite tracking and learning recommendations
 * based on curriculum standards graph structure.
 */

import knowledgeGraphData from '../data/knowledge_graph.json';

export interface KnowledgeNode {
  id: string;
  label: string;
  grade: string;
  theme: string;
  prerequisites?: string[];
}

/**
 * Get all nodes from the knowledge graph
 */
export function getAllNodes(): KnowledgeNode[] {
  return knowledgeGraphData.nodes as KnowledgeNode[];
}

/**
 * Find a specific node by ID
 */
export function getNode(standardId: string): KnowledgeNode | undefined {
  return getAllNodes().find(node => node.id === standardId);
}

/**
 * Get inferred prerequisites based on grade level and theme
 * 
 * Logic: Prerequisites are standards from:
 * 1. Same grade, earlier themes
 * 2. Previous grade, similar themes
 */
export function getPrerequisites(standardId: string): KnowledgeNode[] {
  const node = getNode(standardId);
  if (!node) return [];

  const allNodes = getAllNodes();
  
  // Extract grade number (e.g., "grade_7" -> 7)
  const currentGrade = parseInt(node.grade.replace('grade_', ''));
  const previousGrade = currentGrade - 1;

  // Strategy 1: Same grade, foundational topics
  const sameGradePrereqs = allNodes.filter(n => {
    const nGrade = parseInt(n.grade.replace('grade_', ''));
    return nGrade === currentGrade && n.id < node.id; // Earlier in curriculum
  }).slice(-3); // Last 3 standards from same grade

  // Strategy 2: Previous grade, related themes
  const prevGradePrereqs = allNodes.filter(n => {
    const nGrade = parseInt(n.grade.replace('grade_', ''));
    return nGrade === previousGrade && n.theme.includes(node.theme.split(' ')[0]); // Similar theme
  }).slice(-2); // Last 2 from previous grade

  return [...prevGradePrereqs, ...sameGradePrereqs];
}

/**
 * Generate adaptive learning path recommendation
 * 
 * Use case: Student failed on standard X -> recommend review path
 */
export function generateLearningPath(failedStandard: string): string {
  const node = getNode(failedStandard);
  if (!node) return "Стандардот не е пронајден во базата.";

  const prereqs = getPrerequisites(failedStandard);
  
  if (prereqs.length === 0) {
    return `Ова е основен стандард (${node.label}). Препорака: Повтори основните концепти од "${node.theme}".`;
  }

  const prereqList = prereqs.map(p => `- **${p.id}**: ${p.label}`).join('\n');
  
  return `
**Детектирана празнина:** ${node.label} (${failedStandard})

**Препорачан пат за учење:**

${prereqList}

**Следен чекор:** Дополнително вежбај од "${node.theme}" пред да се вратиш на оваа задача.
`.trim();
}

/**
 * Get all standards for a specific grade
 */
export function getStandardsByGrade(grade: number): KnowledgeNode[] {
  return getAllNodes().filter(n => n.grade === `grade_${grade}`);
}

/**
 * Get all standards for a specific theme
 */
export function getStandardsByTheme(theme: string): KnowledgeNode[] {
  return getAllNodes().filter(n => n.theme.toLowerCase().includes(theme.toLowerCase()));
}

/**
 * Find next logical standard after mastering current one
 */
export function getNextStandard(currentStandard: string): KnowledgeNode | undefined {
  const node = getNode(currentStandard);
  if (!node) return undefined;

  const allNodes = getAllNodes();
  const currentIndex = allNodes.findIndex(n => n.id === currentStandard);
  
  return currentIndex >= 0 && currentIndex < allNodes.length - 1 
    ? allNodes[currentIndex + 1] 
    : undefined;
}
