import type { APIRoute } from 'astro';

import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI(import.meta.env.GEMINI_API_KEY || "");

interface LessonPlanRequest {
  subject: string;
  topic: string;
  grade: string;
  duration: number;
  studentLevel: 'basic' | 'intermediate' | 'advanced';
  learningObjectives: string[];
  specialNeeds?: string[];
  previousKnowledge?: string[];
  availableResources?: string[];
}

interface GeneratedLessonPlan {
  title: string;
  duration: number;
  grade: string;
  subject: string;
  learningObjectives: string[];
  materials: string[];
  differentiationStrategies: {
    advanced: string[];
    basic: string[];
    special_needs: string[];
  };
  lessonStructure: {
    introduction: {
      duration: number;
      activities: string[];
      objectives: string[];
    };
    mainActivities: {
      duration: number;
      activities: string[];
      grouping: string;
      assessment: string[];
    };
    conclusion: {
      duration: number;
      activities: string[];
      reflection: string[];
    };
  };
  assessment: {
    formative: string[];
    summative: string[];
    differentiation: string[];
  };
  homework: {
    assignments: string[];
    extensions: string[];
    support: string[];
  };
  manimAnimations: {
    recommended: string[];
    concepts: string[];
    implementation: string[];
  };
  extensions: {
    enrichment: string[];
    remediation: string[];
    realWorld: string[];
  };
  olympiadBridge: {
    advancedConcept: string;
    connectionToStandard: string;
    sampleOlympiadProblem: string;
    solutionHint: string;
  };
  macedonianScenario: {
    evokacija: string[];
    razbiranje: string[];
    refleksija: string[];
  };
  metadata: {
    generated_at: string;
    ai_model: string;
    pedagogical_approach: string;
    differentiation_level: string;
  };
}

export const POST: APIRoute = async ({ request }) => {
  try {
    const body: LessonPlanRequest = await request.json();
    const {
      subject,
      topic,
      grade,
      duration,
      studentLevel,
      learningObjectives,
      specialNeeds = [],
      previousKnowledge = [],
      availableResources = []
    } = body;

    // Generate comprehensive lesson plan using advanced pedagogical AI
    const lessonPlan = await generateAIPoweredLessonPlan({
      subject,
      topic,
      grade,
      duration,
      studentLevel,
      learningObjectives,
      specialNeeds,
      previousKnowledge,
      availableResources
    });

    return new Response(JSON.stringify({
      success: true,
      lessonPlan,
      metadata: {
        generated_at: new Date().toISOString(),
        processing_time: Date.now(),
        model: 'Advanced Pedagogical AI v2.0'
      }
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    console.error('AI Lesson Generation Error:', error);
    return new Response(JSON.stringify({
      success: false,
      error: 'Failed to generate lesson plan',
      details: error instanceof Error ? error.message : 'Unknown error'
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};

async function generateAIPoweredLessonPlan(params: LessonPlanRequest): Promise<GeneratedLessonPlan> {
  const {
    subject,
    topic,
    grade,
    duration,
    studentLevel,
    learningObjectives,
    specialNeeds,
    previousKnowledge,
    availableResources
  } = params;

  // Advanced pedagogical prompt engineering
  const systemPrompt = createAdvancedPedagogicalPrompt();
  const userPrompt = createDetailedLessonPrompt(params);

  // Use real Gemini API
  const aiResponse = await callGeminiAI(systemPrompt, userPrompt);

  return parseAILessonPlanResponse(aiResponse, params);
}

async function callGeminiAI(systemPrompt: string, userPrompt: string): Promise<string> {
  try {
    const model = genAI.getGenerativeModel({ model: "gemini-1.5-pro" });
    
    const prompt = `${systemPrompt}\n\n${userPrompt}\n\nIMPORTANT: Return ONLY a valid JSON object. Do not include markdown code blocks.`;
    
    const result = await model.generateContent(prompt);
    const response = await result.response;
    let text = response.text();
    
    // Clean up response if AI included markdown blocks
    text = text.replace(/```json/g, "").replace(/```/g, "").trim();
    
    return text;
  } catch (error) {
    console.error("Gemini API Error:", error);
    throw new Error("Failed to generate content from Gemini API");
  }
}

function createAdvancedPedagogicalPrompt(): string {
  return `# Advanced Pedagogical AI Lesson Plan Generator

You are an expert educational AI with deep knowledge in:
- Macedonian national curriculum standards (2025)
- Universal Design for Learning (UDL) principles
- Differentiated instruction strategies
- Assessment design and rubrics
- Cognitive science and learning theories
- Special education accommodations
- Manim animation techniques for complex concepts

## Core Pedagogical Framework

### 1. **Backwards Design Approach**
- Start with desired learning outcomes
- Design assessments before activities
- Plan learning experiences to achieve outcomes

### 2. **Universal Design for Learning (UDL)**
- **Multiple Means of Engagement**: Recruit interest and sustain effort
- **Multiple Means of Representation**: Present information in various ways
- **Multiple Means of Action & Expression**: Differentiate ways students respond

### 3. **Differentiated Instruction**
- **Content**: What students learn
- **Process**: How students learn
- **Product**: How students demonstrate learning
- **Learning Environment**: Classroom management

### 4. **Assessment FOR Learning**
- Formative assessment integrated throughout
- Clear success criteria communicated
- Descriptive feedback provided
- Student self-assessment encouraged

### 6. **Olympiad Bridge (Connecting Standard to Advanced)**
- Identify an advanced Olympiad-level concept that naturally extends from the current standard.
- Provide a clear connection between the standard classroom activity and the advanced concept.
- Include a sample Olympiad problem that is accessible yet challenging.

### 7. **Macedonian "ERR" Framework (Евокација, Разбирање, Рефлексија)**
- **Евокација (Evocation)**: Activities to hook students and activate prior knowledge.
- **Разбирање на значењето (Understanding Meaning)**: Core instruction and active learning.
- **Рефлексија (Reflection)**: Consolidation and application of new knowledge.

## Subject-Specific Expertise

### Mathematics
- Concrete → Pictorial → Abstract progression
- Conceptual understanding before procedural fluency
- Problem-solving strategies and heuristics
- Visual representations and manipulatives

### Macedonian Language & Literature
- Phonological awareness and decoding
- Vocabulary development and morphology
- Reading comprehension strategies
- Writing process and genres
- Literary analysis and interpretation

## Manim Animation Integration

Use Manim for visualizing complex concepts:
- Geometric transformations and proofs
- Algebraic function transformations
- Statistical data visualization
- Literary text structure mapping
- Historical timeline animations

## Response Structure

Generate comprehensive lesson plans with:
1. Clear learning objectives aligned with standards
2. Differentiated activities for all learners
3. Integrated assessment strategies
4. Real-world connections
5. Technology integration suggestions
6. Extension activities for advanced learners
7. Support strategies for struggling students`;
}

function createDetailedLessonPrompt(params: LessonPlanRequest): string {
  const {
    subject,
    topic,
    grade,
    duration,
    studentLevel,
    learningObjectives,
    specialNeeds = [],
    previousKnowledge = [],
    availableResources = []
  } = params;

  return `# Lesson Plan Generation Request

## Context
- **Subject**: ${subject}
- **Topic**: ${topic}
- **Grade**: ${grade}
- **Duration**: ${duration} minutes
- **Student Level**: ${studentLevel}
- **Learning Objectives**: ${learningObjectives.join(', ')}

## Student Profile
- **Previous Knowledge**: ${previousKnowledge.join(', ')}
- **Special Needs**: ${specialNeeds.join(', ')}
- **Available Resources**: ${availableResources.join(', ')}

## Required Output Format

Generate a complete lesson plan following this structure:

### 1. Lesson Title
Create an engaging, descriptive title

### 2. Learning Objectives
- List 3-5 specific, measurable objectives
- Align with Macedonian national standards
- Include cognitive, affective, and psychomotor domains

### 3. Materials & Resources
- Required materials
- Technology resources
- Differentiated supports

### 4. Differentiation Strategies
#### Advanced Learners
- Extension activities
- Leadership roles
- Independent projects

#### Basic Learners
- Scaffolding strategies
- Simplified explanations
- Additional supports

#### Special Needs
- Accommodations based on specific needs
- Assistive technology
- Modified activities

### 5. Lesson Structure
#### Introduction (${Math.round(duration * 0.15)} minutes)
- Hook/attention getter
- Learning objectives review
- Prior knowledge activation
- Vocabulary preview

#### Main Activities (${Math.round(duration * 0.65)} minutes)
- Core instruction with differentiation
- Guided practice
- Independent practice
- Formative assessment checkpoints

#### Conclusion (${Math.round(duration * 0.20)} minutes)
- Learning consolidation
- Self-assessment
- Reflection activities
- Preview of next lesson

### 6. Assessment
#### Formative Assessment
- During lesson checks
- Exit tickets
- Observation protocols

#### Summative Assessment
- Performance tasks
- Projects or presentations
- Traditional quizzes/tests

### 7. Homework & Extensions
#### Assignments
- Practice activities
- Real-world applications
- Reading/writing tasks

#### Extensions
- Enrichment projects
- Advanced problem-solving
- Research opportunities

### 8. Manim Animation Recommendations
Based on ${topic}, suggest:
- Key concepts to visualize
- Animation types (transformations, sequences, interactions)
- Implementation complexity
- Integration points in lesson

### 9. Real-World Connections
- Authentic applications
- Career connections
- Community relevance
- Current events integration

### 11. Olympiad Bridge
- **Advanced Concept**: What is the next-level concept?
- **Connection**: How does it connect to the lesson?
- **Sample Problem**: A challenging problem in Macedonian.
- **Hint**: A hint for the solution.

### 12. Macedonian Lesson Scenario (ERR Framework)
- **Evokacija**: 2-3 activities.
- **Razbiranje**: 3-4 activities.
- **Refleksija**: 2-3 activities.

## Quality Assurance Checklist
- [ ] Objectives measurable and standards-aligned
- [ ] Activities differentiated for all learners
- [ ] Assessment integrated throughout
- [ ] Real-world connections included
- [ ] Technology meaningfully integrated
- [ ] Special needs accommodations provided
- [ ] Manim animations appropriately suggested
- [ ] Time allocations realistic and balanced`;
}



function parseAILessonPlanResponse(aiResponse: string, params: LessonPlanRequest): GeneratedLessonPlan {
  try {
    // Parse the AI response and structure it properly
    const parsed = JSON.parse(aiResponse);

    // Ensure all required fields are present
    return {
      title: parsed.title || `Настава за ${params.topic}`,
      duration: params.duration,
      grade: params.grade,
      subject: params.subject,
      learningObjectives: parsed.learningObjectives || params.learningObjectives,
      materials: parsed.materials || [],
      differentiationStrategies: parsed.differentiationStrategies || {
        advanced: [],
        basic: [],
        special_needs: []
      },
      lessonStructure: parsed.lessonStructure || {
        introduction: { duration: 0, activities: [], objectives: [] },
        mainActivities: { duration: 0, activities: [], grouping: '', assessment: [] },
        conclusion: { duration: 0, activities: [], reflection: [] }
      },
      assessment: parsed.assessment || {
        formative: [],
        summative: [],
        differentiation: []
      },
      homework: parsed.homework || {
        assignments: [],
        extensions: [],
        support: []
      },
      manimAnimations: parsed.manimAnimations || {
        recommended: [],
        concepts: [],
        implementation: []
      },
      olympiadBridge: parsed.olympiadBridge || {
        advancedConcept: '',
        connectionToStandard: '',
        sampleOlympiadProblem: '',
        solutionHint: ''
      },
      macedonianScenario: parsed.macedonianScenario || {
        evokacija: [],
        razbiranje: [],
        refleksija: []
      },
      extensions: parsed.extensions || {
        enrichment: [],
        remediation: [],
        realWorld: []
      },
      metadata: parsed.metadata || {
        generated_at: new Date().toISOString(),
        ai_model: 'Advanced Pedagogical AI v2.0',
        pedagogical_approach: 'Universal Design for Learning',
        differentiation_level: 'Advanced'
      }
    };
  } catch (error) {
    console.error('Error parsing AI response:', error);
    // Return a fallback lesson plan
    return createFallbackLessonPlan(params);
  }
}

function createFallbackLessonPlan(params: LessonPlanRequest): GeneratedLessonPlan {
  return {
    title: `Настава за ${params.topic}`,
    duration: params.duration,
    grade: params.grade,
    subject: params.subject,
    learningObjectives: params.learningObjectives,
    materials: ['Основни учебници', 'Рабошници', 'Табла'],
    differentiationStrategies: {
      advanced: ['Напредни проблеми', 'Истражувачки проекти'],
      basic: ['Визуелни помагала', 'Парна работа'],
      special_needs: ['Индивидуална поддршка', 'Адаптирани материјали']
    },
    lessonStructure: {
      introduction: {
        duration: Math.round(params.duration * 0.15),
        activities: ['Активирање на претходни знаења', 'Презентација на цели'],
        objectives: ['Зainteresување', 'Јасни цели']
      },
      mainActivities: {
        duration: Math.round(params.duration * 0.65),
        activities: ['Директна инструкција', 'Во групна работа', 'Индивидуална практика'],
        grouping: 'Хетерогени групи',
        assessment: ['Набљудување', 'Кратки проверки']
      },
      conclusion: {
        duration: Math.round(params.duration * 0.20),
        activities: ['Резиме', 'Рефлексија'],
        reflection: ['Самооценување', 'Планирање за подобрување']
      }
    },
    assessment: {
      formative: ['Тековни проверки', 'Exit tickets'],
      summative: ['Тест', 'Проект'],
      differentiation: ['Множество формати', 'Прилагодени критериуми']
    },
    homework: {
      assignments: ['Практични задачи', 'Читање'],
      extensions: ['Дополнителни истражувања'],
      support: ['Онлајн ресурси', 'Врсничка помош']
    },
    manimAnimations: {
      recommended: ['Базични визуелизации'],
      concepts: [params.topic],
      implementation: ['Едноставни анимации']
    },
    olympiadBridge: {
      advancedConcept: 'Логички задачи поврзани со ' + params.topic,
      connectionToStandard: 'Примена на основните поими во нестандардни ситуации',
      sampleOlympiadProblem: 'Дали може да се најде пример каде ова правило не важи директно?',
      solutionHint: 'Проверете ги екстремните вредности.'
    },
    macedonianScenario: {
      evokacija: ['Повторување на претходни знаења'],
      razbiranje: ['Нови поими и примери'],
      refleksija: ['Заклучок и дискусија']
    },
    extensions: {
      enrichment: ['Напредни теми'],
      remediation: ['Дополнителна практика'],
      realWorld: ['Реални апликации']
    },
    metadata: {
      generated_at: new Date().toISOString(),
      ai_model: 'Fallback Generator',
      pedagogical_approach: 'Basic Structure',
      differentiation_level: 'Standard'
    }
  };
}