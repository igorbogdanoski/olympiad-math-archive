# AI Workflow for Problem Classification

## Input
Raw olympiad problem text (any language).

## AI Configuration
- System prompt: system_prompt.md
- Output format: output_schema.json

## Output
Strict JSON describing:
- grade
- field
- difficulty
- geometry constraints
- tags
- solution strategy

## Usage
1. Paste problem text into AI system.
2. Validate JSON output.
3. Map fields into problem_template.md.
