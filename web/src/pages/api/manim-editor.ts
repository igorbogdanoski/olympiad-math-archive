import type { APIRoute } from 'astro';
import { readFileSync, writeFileSync, existsSync, readdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { execSync } from 'node:child_process';
import { t } from '../../utils/i18n';

// Available templates
interface TemplateInfo {
  id: string;
  title: string;
  grade: string;
  category: string;
  score: number;
  description: string;
}

export const GET: APIRoute = async ({ url }) => {
  try {
    const action = url.searchParams.get('action');

    if (action === 'list-templates') {
      // Return list of available templates
      const templatesDir = join(process.cwd(), '../tools/manim_templates/top_50');
      const allFiles = readdirSync(templatesDir);
      const templateFiles = allFiles.filter(file => file.startsWith('manim_') && file.endsWith('.py'));

      const templates: TemplateInfo[] = [];

      for (const file of templateFiles) {
        try {
          const filePath = join(templatesDir, file);
          const content = readFileSync(filePath, 'utf8');

          // Extract metadata from docstring
          const problemId = file.replace('manim_', '').replace('.py', '');
          const titleMatch = content.match(/Problem: ([^\n]+)/);
          const gradeMatch = content.match(/Grade: ([^\n]+)/);
          const categoryMatch = content.match(/Category: ([^\n]+)/);
          const scoreMatch = content.match(/Score: ([^\n]+)/);
          const descMatch = content.match(/Problem Description:\s*([^\n]+)/);

          templates.push({
            id: problemId,
            title: titleMatch ? titleMatch[1].trim() : problemId,
            grade: gradeMatch ? gradeMatch[1].trim() : 'Unknown',
            category: categoryMatch ? categoryMatch[1].trim() : 'Unknown',
            score: scoreMatch ? parseInt(scoreMatch[1].trim()) : 0,
            description: descMatch ? descMatch[1].trim() : 'No description available'
          });
        } catch (error) {
          console.warn(`Failed to parse template ${file}:`, error);
        }
      }

      // Sort by score (highest first)
      templates.sort((a, b) => b.score - a.score);

      return new Response(JSON.stringify({
        templates,
        total: templates.length
      }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      });

    } else if (action === 'get-template') {
      const problemId = url.searchParams.get('id');
      if (!problemId) {
        return new Response(JSON.stringify({ error: t('errors.problem_id_required') }), {
          status: 400,
          headers: { 'Content-Type': 'application/json' }
        });
      }

      const templatePath = join(process.cwd(), '../tools/manim_templates/top_50', `manim_${problemId}.py`);

      if (!existsSync(templatePath)) {
        return new Response(JSON.stringify({ error: t('errors.template_not_found') }), {
          status: 404,
          headers: { 'Content-Type': 'application/json' }
        });
      }

      const content = readFileSync(templatePath, 'utf8');

      return new Response(JSON.stringify({
        problemId,
        content,
        path: templatePath
      }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    return new Response(JSON.stringify({ error: 'Invalid action' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    console.error('Error in manim-editor GET:', error);
    return new Response(JSON.stringify({
      error: 'Internal server error',
      details: error instanceof Error ? error.message : String(error)
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};

export const POST: APIRoute = async ({ request }) => {
  try {
    const { action, problemId, content, quality = 'low' } = await request.json();

    if (action === 'save-template') {
      if (!problemId || !content) {
        return new Response(JSON.stringify({ error: 'Problem ID and content required' }), {
          status: 400,
          headers: { 'Content-Type': 'application/json' }
        });
      }

      const templatePath = join(process.cwd(), '../tools/manim_templates/top_50', `manim_${problemId}.py`);

      // Create backup
      if (existsSync(templatePath)) {
        const backupPath = `${templatePath}.backup`;
        const originalContent = readFileSync(templatePath, 'utf8');
        writeFileSync(backupPath, originalContent);
      }

      // Save new content
      writeFileSync(templatePath, content, 'utf8');

      return new Response(JSON.stringify({
        success: true,
        message: 'Template saved successfully',
        backupCreated: existsSync(`${templatePath}.backup`)
      }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      });

    } else if (action === 'render-template') {
      if (!problemId) {
        return new Response(JSON.stringify({ error: 'Problem ID required' }), {
          status: 400,
          headers: { 'Content-Type': 'application/json' }
        });
      }

      const templatePath = join(process.cwd(), '../tools/manim_templates/top_50', `manim_${problemId}.py`);

      if (!existsSync(templatePath)) {
        return new Response(JSON.stringify({ error: 'Template not found' }), {
          status: 404,
          headers: { 'Content-Type': 'application/json' }
        });
      }

      // Generate class name (same logic as generator)
      const readableId = problemId.replace('_', ' ').replace('-', ' ');
      const words = readableId.split();
      const capitalizedWords = [];
      for (const word of words) {
        if (word.match(/^\d+$/)) {
          capitalizedWords.push(word);
        } else if (['mun', 'cnt', 'sigma', 'adv', 'geo', 'geom'].includes(word.toLowerCase())) {
          capitalizedWords.push(word.toUpperCase());
        } else {
          capitalizedWords.push(word.charAt(0).toUpperCase() + word.slice(1).toLowerCase());
        }
      }
      const className = 'Problem' + capitalizedWords.join('') + 'Scene';

      // Build Manim command
      const qualityFlags: { [key: string]: string } = {
        'low': '-ql',
        'medium': '-qm',
        'high': '-qh',
        'ultra': '-qk'
      };
      const qualityFlag = qualityFlags[quality] || '-ql';

      const command = `manim ${qualityFlag} "${templatePath}" ${className}`;

      console.log('Executing Manim command:', command);

      // Execute render
      const output = execSync(command, {
        cwd: join(process.cwd(), '../tools/manim_templates/top_50'),
        encoding: 'utf8',
        timeout: 300000, // 5 minutes timeout
        maxBuffer: 1024 * 1024 * 50 // 50MB buffer
      });

      console.log('Manim output:', output);

      // Find generated video
      const videoDir = join(process.cwd(), '../tools/manim_templates/top_50/media/videos', `manim_${problemId}`, `${quality}p15`);
      let videoFiles: string[] = [];
      try {
        const allFiles = readdirSync(videoDir);
        videoFiles = allFiles.filter(file => file.endsWith('.mp4'));
      } catch (error) {
        videoFiles = [];
      }

      if (videoFiles.length === 0) {
        return new Response(JSON.stringify({
          error: 'Video generation failed - no output file found',
          output: output
        }), {
          status: 500,
          headers: { 'Content-Type': 'application/json' }
        });
      }

      const videoPath = join(videoDir, videoFiles[0]);
      const relativeVideoPath = `/manim_templates/top_50/media/videos/manim_${problemId}/${quality}p15/${videoFiles[0]}`;

      return new Response(JSON.stringify({
        success: true,
        videoPath: relativeVideoPath,
        fullVideoPath: videoPath,
        output: output,
        className: className
      }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      });

    } else if (action === 'validate-template') {
      if (!problemId) {
        return new Response(JSON.stringify({ error: 'Problem ID required' }), {
          status: 400,
          headers: { 'Content-Type': 'application/json' }
        });
      }

      const templatePath = join(process.cwd(), '../tools/manim_templates/top_50', `manim_${problemId}.py`);

      if (!existsSync(templatePath)) {
        return new Response(JSON.stringify({ error: 'Template not found' }), {
          status: 404,
          headers: { 'Content-Type': 'application/json' }
        });
      }

      const content = readFileSync(templatePath, 'utf8');

      // Basic validation checks
      const issues = [];

      if (!content.includes('from manim import')) {
        issues.push('Missing Manim import');
      }

      if (!content.includes('class ') || !content.includes('Scene')) {
        issues.push('Invalid scene class structure');
      }

      if (content.includes('TODO:')) {
        issues.push('Template contains unimplemented sections');
      }

      if (content.includes('Problem text extraction failed')) {
        issues.push('Problem description extraction failed');
      }

      return new Response(JSON.stringify({
        problemId,
        valid: issues.length === 0,
        issues: issues,
        hasContent: content.length > 1000, // Reasonable minimum
        hasHelperFunctions: content.includes('def create_')
      }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    return new Response(JSON.stringify({ error: 'Invalid action' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    console.error('Error in manim-editor POST:', error);
    return new Response(JSON.stringify({
      error: 'Internal server error',
      details: error instanceof Error ? error.message : String(error)
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};