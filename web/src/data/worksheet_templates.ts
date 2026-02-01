/**
 * Worksheet Template System
 * Created: February 2, 2026
 * Purpose: Define 15+ worksheet templates with professional styling
 */

export interface WorksheetTemplate {
  id: string;
  name_mk: string;
  name_en: string;
  description_mk: string;
  description_en: string;
  recommended_problems: number; // Recommended number of problems
  recommended_time_minutes: number;
  show_work_space: boolean;
  include_header: boolean;
  include_footer: boolean;
  points_per_problem: number;
  styles: TemplateStyles;
}

export interface TemplateStyles {
  font_family: string;
  font_size: number;
  line_spacing: number;
  margin_top: number;
  margin_bottom: number;
  margin_left: number;
  margin_right: number;
  header_color: string;
  accent_color: string;
}

/**
 * All available worksheet templates
 */
export const WORKSHEET_TEMPLATES: WorksheetTemplate[] = [
  {
    id: 'test',
    name_mk: 'Тест',
    name_en: 'Test',
    description_mk: 'Стандарден тест со оценување',
    description_en: 'Standard test with grading',
    recommended_problems: 10,
    recommended_time_minutes: 45,
    show_work_space: true,
    include_header: true,
    include_footer: true,
    points_per_problem: 10,
    styles: {
      font_family: 'Times New Roman',
      font_size: 12,
      line_spacing: 1.5,
      margin_top: 20,
      margin_bottom: 20,
      margin_left: 25,
      margin_right: 25,
      header_color: '#2c3e50',
      accent_color: '#3498db',
    },
  },
  {
    id: 'quiz',
    name_mk: 'Квиз',
    name_en: 'Quiz',
    description_mk: 'Краток квиз за проверка',
    description_en: 'Short quiz for assessment',
    recommended_problems: 5,
    recommended_time_minutes: 15,
    show_work_space: false,
    include_header: true,
    include_footer: false,
    points_per_problem: 20,
    styles: {
      font_family: 'Arial',
      font_size: 11,
      line_spacing: 1.3,
      margin_top: 15,
      margin_bottom: 15,
      margin_left: 20,
      margin_right: 20,
      header_color: '#e74c3c',
      accent_color: '#e67e22',
    },
  },
  {
    id: 'homework',
    name_mk: 'Домашна работа',
    name_en: 'Homework',
    description_mk: 'Домашна задача за вежбање',
    description_en: 'Homework assignment for practice',
    recommended_problems: 15,
    recommended_time_minutes: 60,
    show_work_space: true,
    include_header: true,
    include_footer: true,
    points_per_problem: 5,
    styles: {
      font_family: 'Arial',
      font_size: 11,
      line_spacing: 1.8,
      margin_top: 20,
      margin_bottom: 20,
      margin_left: 25,
      margin_right: 25,
      header_color: '#16a085',
      accent_color: '#27ae60',
    },
  },
  {
    id: 'practice',
    name_mk: 'Вежбање',
    name_en: 'Practice',
    description_mk: 'Вежби за развивање вештини',
    description_en: 'Practice problems for skill development',
    recommended_problems: 20,
    recommended_time_minutes: 45,
    show_work_space: true,
    include_header: true,
    include_footer: false,
    points_per_problem: 5,
    styles: {
      font_family: 'Arial',
      font_size: 11,
      line_spacing: 1.6,
      margin_top: 20,
      margin_bottom: 20,
      margin_left: 25,
      margin_right: 25,
      header_color: '#8e44ad',
      accent_color: '#9b59b6',
    },
  },
  {
    id: 'warm_up',
    name_mk: 'Загревање',
    name_en: 'Warm-up',
    description_mk: 'Брзи задачи за почеток на час',
    description_en: 'Quick problems to start the lesson',
    recommended_problems: 3,
    recommended_time_minutes: 10,
    show_work_space: false,
    include_header: true,
    include_footer: false,
    points_per_problem: 0, // Not graded
    styles: {
      font_family: 'Arial',
      font_size: 12,
      line_spacing: 1.5,
      margin_top: 15,
      margin_bottom: 15,
      margin_left: 20,
      margin_right: 20,
      header_color: '#f39c12',
      accent_color: '#f1c40f',
    },
  },
  {
    id: 'review',
    name_mk: 'Повторување',
    name_en: 'Review',
    description_mk: 'Преглед на претходни теми',
    description_en: 'Review of previous topics',
    recommended_problems: 12,
    recommended_time_minutes: 40,
    show_work_space: true,
    include_header: true,
    include_footer: true,
    points_per_problem: 8,
    styles: {
      font_family: 'Arial',
      font_size: 11,
      line_spacing: 1.5,
      margin_top: 20,
      margin_bottom: 20,
      margin_left: 25,
      margin_right: 25,
      header_color: '#34495e',
      accent_color: '#95a5a6',
    },
  },
  {
    id: 'challenge',
    name_mk: 'Предизвик',
    name_en: 'Challenge',
    description_mk: 'Тешки задачи за напредни ученици',
    description_en: 'Difficult problems for advanced students',
    recommended_problems: 5,
    recommended_time_minutes: 30,
    show_work_space: true,
    include_header: true,
    include_footer: true,
    points_per_problem: 20,
    styles: {
      font_family: 'Times New Roman',
      font_size: 12,
      line_spacing: 2.0,
      margin_top: 25,
      margin_bottom: 25,
      margin_left: 30,
      margin_right: 30,
      header_color: '#c0392b',
      accent_color: '#e74c3c',
    },
  },
  {
    id: 'exam',
    name_mk: 'Испит',
    name_en: 'Exam',
    description_mk: 'Финален испит',
    description_en: 'Final exam',
    recommended_problems: 15,
    recommended_time_minutes: 90,
    show_work_space: true,
    include_header: true,
    include_footer: true,
    points_per_problem: 10,
    styles: {
      font_family: 'Times New Roman',
      font_size: 12,
      line_spacing: 1.8,
      margin_top: 25,
      margin_bottom: 25,
      margin_left: 30,
      margin_right: 30,
      header_color: '#2c3e50',
      accent_color: '#34495e',
    },
  },
  {
    id: 'diagnostic',
    name_mk: 'Дијагностика',
    name_en: 'Diagnostic',
    description_mk: 'Проценка на знаење',
    description_en: 'Knowledge assessment',
    recommended_problems: 20,
    recommended_time_minutes: 45,
    show_work_space: false,
    include_header: true,
    include_footer: true,
    points_per_problem: 5,
    styles: {
      font_family: 'Arial',
      font_size: 11,
      line_spacing: 1.4,
      margin_top: 20,
      margin_bottom: 20,
      margin_left: 25,
      margin_right: 25,
      header_color: '#2980b9',
      accent_color: '#3498db',
    },
  },
  {
    id: 'formative',
    name_mk: 'Формативна оценка',
    name_en: 'Formative Assessment',
    description_mk: 'Оценување за напредок',
    description_en: 'Assessment for progress',
    recommended_problems: 8,
    recommended_time_minutes: 30,
    show_work_space: true,
    include_header: true,
    include_footer: false,
    points_per_problem: 10,
    styles: {
      font_family: 'Arial',
      font_size: 11,
      line_spacing: 1.5,
      margin_top: 20,
      margin_bottom: 20,
      margin_left: 25,
      margin_right: 25,
      header_color: '#16a085',
      accent_color: '#1abc9c',
    },
  },
  {
    id: 'summative',
    name_mk: 'Сумативна оценка',
    name_en: 'Summative Assessment',
    description_mk: 'Финална оценка за период',
    description_en: 'Final assessment for period',
    recommended_problems: 12,
    recommended_time_minutes: 60,
    show_work_space: true,
    include_header: true,
    include_footer: true,
    points_per_problem: 10,
    styles: {
      font_family: 'Times New Roman',
      font_size: 12,
      line_spacing: 1.6,
      margin_top: 25,
      margin_bottom: 25,
      margin_left: 30,
      margin_right: 30,
      header_color: '#27ae60',
      accent_color: '#2ecc71',
    },
  },
  {
    id: 'project',
    name_mk: 'Проект',
    name_en: 'Project',
    description_mk: 'Задачи за истражувачки проект',
    description_en: 'Problems for research project',
    recommended_problems: 5,
    recommended_time_minutes: 120,
    show_work_space: true,
    include_header: true,
    include_footer: true,
    points_per_problem: 20,
    styles: {
      font_family: 'Arial',
      font_size: 11,
      line_spacing: 2.0,
      margin_top: 25,
      margin_bottom: 25,
      margin_left: 30,
      margin_right: 30,
      header_color: '#8e44ad',
      accent_color: '#9b59b6',
    },
  },
  {
    id: 'investigation',
    name_mk: 'Истражување',
    name_en: 'Investigation',
    description_mk: 'Задачи за аналитичко размислување',
    description_en: 'Problems for analytical thinking',
    recommended_problems: 6,
    recommended_time_minutes: 45,
    show_work_space: true,
    include_header: true,
    include_footer: true,
    points_per_problem: 15,
    styles: {
      font_family: 'Arial',
      font_size: 11,
      line_spacing: 1.8,
      margin_top: 25,
      margin_bottom: 25,
      margin_left: 30,
      margin_right: 30,
      header_color: '#d35400',
      accent_color: '#e67e22',
    },
  },
  {
    id: 'exploration',
    name_mk: 'Истражување',
    name_en: 'Exploration',
    description_mk: 'Задачи за самостојно истражување',
    description_en: 'Problems for independent exploration',
    recommended_problems: 8,
    recommended_time_minutes: 60,
    show_work_space: true,
    include_header: true,
    include_footer: false,
    points_per_problem: 10,
    styles: {
      font_family: 'Arial',
      font_size: 11,
      line_spacing: 1.8,
      margin_top: 25,
      margin_bottom: 25,
      margin_left: 30,
      margin_right: 30,
      header_color: '#2c3e50',
      accent_color: '#34495e',
    },
  },
  {
    id: 'mixed',
    name_mk: 'Мешовито',
    name_en: 'Mixed',
    description_mk: 'Комбинација од различни типови задачи',
    description_en: 'Combination of different problem types',
    recommended_problems: 15,
    recommended_time_minutes: 45,
    show_work_space: true,
    include_header: true,
    include_footer: true,
    points_per_problem: 10,
    styles: {
      font_family: 'Arial',
      font_size: 11,
      line_spacing: 1.6,
      margin_top: 20,
      margin_bottom: 20,
      margin_left: 25,
      margin_right: 25,
      header_color: '#7f8c8d',
      accent_color: '#95a5a6',
    },
  },
];

/**
 * Get template by ID
 */
export function getTemplateById(id: string): WorksheetTemplate | undefined {
  return WORKSHEET_TEMPLATES.find((t) => t.id === id);
}

/**
 * Get all template IDs
 */
export function getAllTemplateIds(): string[] {
  return WORKSHEET_TEMPLATES.map((t) => t.id);
}

/**
 * Get templates by recommended problem count
 */
export function getTemplatesByProblemCount(min: number, max: number): WorksheetTemplate[] {
  return WORKSHEET_TEMPLATES.filter(
    (t) => t.recommended_problems >= min && t.recommended_problems <= max
  );
}
