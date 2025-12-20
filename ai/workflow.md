# AI Workflow for Problem Classification & Generation

## 1. Input Phase
- **Source:** Raw text from PDF/Image (Numerus, Competitions).
- **Tool:** Google AI Studio (Gemini 1.5 Pro).
- **Configuration:** 
  - System Prompt: `ai/system_prompt.md`
  - Output Schema: `ai/output_schema.json`

## 2. Processing Phase (The "Brain")
- Paste raw text into AI.
- **Human Check:** Verify the `primary_skill` assignment. 
  - *Does this really use Invariants, or just simple algebra?*
- **Output:** Copy the generated JSON object.

## 3. Build Phase (The "Engine")
- **Action:** Run `python tools/build_problem.py` (види подолу).
- **Input:** Paste the JSON.
- **Result:** The script automatically:
  1. Selects the correct template (Geometry vs Standard).
  2. Fills in all fields (Tags, Skills, Solution).
  3. Creates the file at: `grade_{G}/{field}/{source_id}.md`.

## 4. Linking Phase (The "Web")
- The script automatically appends the new problem link to the relevant `tools/skill_guides/{skill}.md` file.