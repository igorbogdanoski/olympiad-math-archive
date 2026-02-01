-- Worksheet Generator Database Schema
-- Created: February 2, 2026
-- Purpose: Store teacher-created worksheets with problems

-- Worksheets table - stores worksheet metadata
CREATE TABLE IF NOT EXISTS worksheets (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    template_type VARCHAR(50) NOT NULL, -- 'test', 'quiz', 'homework', 'practice', etc.
    grade_level INTEGER NOT NULL CHECK (grade_level >= 6 AND grade_level <= 9),
    subject VARCHAR(50) NOT NULL, -- 'geometry', 'algebra', 'number_theory', etc.
    created_by VARCHAR(255), -- Teacher name/email
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Worksheet settings
    include_answer_key BOOLEAN DEFAULT TRUE,
    show_work_space BOOLEAN DEFAULT TRUE,
    points_per_problem INTEGER DEFAULT 10,
    time_limit_minutes INTEGER, -- NULL = no time limit
    
    -- БРО standards covered (array of standard codes)
    bro_standards TEXT[], -- ['М.6.2.1', 'М.7.1.3']
    
    -- Metadata
    difficulty_level VARCHAR(20), -- 'easy', 'medium', 'hard', 'mixed'
    total_points INTEGER,
    estimated_time_minutes INTEGER,
    
    -- PDF metadata
    pdf_generated BOOLEAN DEFAULT FALSE,
    pdf_path TEXT,
    pdf_generated_at TIMESTAMP,
    
    -- Usage tracking
    download_count INTEGER DEFAULT 0,
    last_downloaded_at TIMESTAMP
);

-- Worksheet problems junction table - links worksheets to problems
CREATE TABLE IF NOT EXISTS worksheet_problems (
    id SERIAL PRIMARY KEY,
    worksheet_id INTEGER NOT NULL REFERENCES worksheets(id) ON DELETE CASCADE,
    problem_id VARCHAR(50) NOT NULL, -- Reference to problems.json problem_id
    
    -- Problem ordering and customization
    problem_order INTEGER NOT NULL, -- 1, 2, 3, etc.
    points_allocated INTEGER DEFAULT 10,
    custom_instructions TEXT, -- Optional custom instructions for this problem
    
    -- Metadata (denormalized for performance)
    problem_title_mk TEXT,
    problem_title_en TEXT,
    problem_difficulty VARCHAR(20),
    problem_topic VARCHAR(100),
    
    UNIQUE(worksheet_id, problem_order)
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_worksheets_created_by ON worksheets(created_by);
CREATE INDEX IF NOT EXISTS idx_worksheets_grade_level ON worksheets(grade_level);
CREATE INDEX IF NOT EXISTS idx_worksheets_subject ON worksheets(subject);
CREATE INDEX IF NOT EXISTS idx_worksheets_created_at ON worksheets(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_worksheet_problems_worksheet_id ON worksheet_problems(worksheet_id);
CREATE INDEX IF NOT EXISTS idx_worksheet_problems_problem_id ON worksheet_problems(problem_id);

-- Create updated_at trigger
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_worksheets_updated_at BEFORE UPDATE ON worksheets
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Insert sample templates metadata (for reference)
COMMENT ON COLUMN worksheets.template_type IS 'Template types: test, quiz, homework, practice, warm_up, review, challenge, exam, diagnostic, formative, summative, project, investigation, exploration, mixed';
COMMENT ON COLUMN worksheets.subject IS 'Subjects: geometry, algebra, number_theory, combinatorics, logic, mixed';
COMMENT ON COLUMN worksheets.difficulty_level IS 'Difficulty levels: easy, medium, hard, mixed (auto-calculated from problems)';
