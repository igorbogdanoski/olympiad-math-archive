import type { APIRoute } from 'astro';
import { execSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';

export const POST: APIRoute = async ({ request }) => {
  try {
    const { grade, field, count, difficulty, testType } = await request.json();

    // Validate input
    if (!grade || !count) {
      return new Response(JSON.stringify({
        error: 'Grade and count are required'
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Build Python command
    const scriptPath = join(process.cwd(), '../tools/generate_smart_test.py');
    console.log('Current working directory:', process.cwd());
    console.log('Script path:', scriptPath);

    const args = [
      grade.toString(),
      field || 'all',
      count.toString(),
      difficulty || 'all',
      testType || 'mixed'
    ];

    const command = `python "${scriptPath}" -g ${args[0]} -f ${args[1]} -c ${args[2]} -d ${args[3]} -t ${args[4]}`;

    console.log('Executing command:', command);

    // Execute Python script
    const output = execSync(command, {
      cwd: join(process.cwd(), '..'),
      encoding: 'utf8',
      maxBuffer: 1024 * 1024 * 10 // 10MB buffer
    });

    console.log('Python output:', output);

    // Parse output to find generated file names
    const lines = output.split('\n');
    console.log('Python output lines:', lines);

    // Extract file names from lines containing [FILE]
    const studentFileName = lines.find(line => line.includes('STUDENT.html'))?.match(/Smart_Test.*STUDENT\.html/)?.[0];
    const teacherFileName = lines.find(line => line.includes('TEACHER.html'))?.match(/Smart_Test.*TEACHER\.html/)?.[0];

    console.log('Student file name:', studentFileName);
    console.log('Teacher file name:', teacherFileName);

    if (!studentFileName || !teacherFileName) {
      return new Response(JSON.stringify({
        error: 'Failed to extract file names from output',
        output: output,
        lines: lines
      }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Build full paths to the generated files
    const studentPath = join(process.cwd(), '../tools/output_documents', studentFileName);
    const teacherPath = join(process.cwd(), '../tools/output_documents', teacherFileName);

    if (!studentPath || !teacherPath) {
      return new Response(JSON.stringify({
        error: 'Could not extract file paths'
      }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Read the generated HTML files
    const studentHtml = readFileSync(studentPath, 'utf8');
    const teacherHtml = readFileSync(teacherPath, 'utf8');

    return new Response(JSON.stringify({
      studentHtml,
      teacherHtml,
      studentPath,
      teacherPath
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    console.error('Error generating test:', error);
    return new Response(JSON.stringify({
      error: 'Failed to generate test',
      details: error instanceof Error ? error.message : String(error)
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};