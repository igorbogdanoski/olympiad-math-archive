-- Enable Citus extension
CREATE EXTENSION IF NOT EXISTS citus;

-- Create schools table (distributed by id)
CREATE TABLE schools (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    region VARCHAR(100),
    type VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Distribute schools table
SELECT create_distributed_table('schools', 'id');

-- Create school_reports table
CREATE TABLE school_reports (
    id SERIAL PRIMARY KEY,
    school_id INTEGER REFERENCES schools(id),
    semester VARCHAR(50),
    report_year INTEGER,
    attendance_summary JSONB,
    grade_success JSONB,
    subject_performance JSONB,
    summary_stats JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Distribute school_reports table
SELECT create_distributed_table('school_reports', 'school_id');

-- Create curriculum_standards table (reference table if shared)
CREATE TABLE curriculum_standards (
    id SERIAL PRIMARY KEY,
    subject VARCHAR(100),
    grade VARCHAR(50),
    topics JSONB,
    standards JSONB,
    objectives JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Make curriculum_standards a reference table (replicated on all nodes)
SELECT create_reference_table('curriculum_standards');

-- Create users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    role VARCHAR(50),
    school_id INTEGER REFERENCES schools(id),
    preferences JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Distribute users table
SELECT create_distributed_table('users', 'school_id');

-- Create sessions table
CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    token VARCHAR(500) UNIQUE,
    expires_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Distribute sessions table (by school_id via user_id, but since no direct school_id, need to handle)
-- Actually, sessions should be distributed by school_id, but since it references user_id, and user has school_id,
-- We can distribute by user_id if we make it hash, but better to add school_id or distribute by user_id.
-- For simplicity, distribute by user_id
SELECT create_distributed_table('sessions', 'user_id');

-- Add nodes (workers) to the cluster
-- This should be run after workers are up
-- SELECT * FROM citus_add_node('citus_worker1', 5433);
-- SELECT * FROM citus_add_node('citus_worker2', 5434);
-- SELECT * FROM citus_add_node('citus_worker3', 5435);