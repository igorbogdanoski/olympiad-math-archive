/**
 * Manim Queue Worker - Background processing for Manim renders
 * Uses Bull queue with Redis for async, scalable video generation
 */

import Queue from 'bull';
import { exec } from 'child_process';
import { promisify } from 'util';
import { readFileSync, readdirSync, existsSync } from 'fs';
import { join } from 'path';
import crypto from 'crypto';

const execAsync = promisify(exec);

// Redis connection config
const REDIS_URL = process.env.REDIS_URL || 'redis://localhost:6379';

// Create Manim render queue
export const manimQueue = new Queue('manim-renders', REDIS_URL, {
  defaultJobOptions: {
    attempts: 3,
    backoff: {
      type: 'exponential',
      delay: 2000
    },
    timeout: 300000, // 5 minutes
    removeOnComplete: 100, // Keep last 100 completed jobs
    removeOnFail: 50 // Keep last 50 failed jobs
  }
});

// Job data interface
interface ManimRenderJob {
  problemId: string;
  quality: 'low' | 'medium' | 'high' | 'ultra';
  templatePath: string;
  className: string;
  templateContent?: string;
}

// Result interface
interface ManimRenderResult {
  success: boolean;
  videoUrl?: string;
  videoPath?: string;
  duration?: number;
  error?: string;
  cached?: boolean;
}

/**
 * Generate content hash for caching
 */
function getContentHash(content: string, quality: string): string {
  return crypto
    .createHash('sha256')
    .update(content + quality)
    .digest('hex')
    .substring(0, 16);
}

/**
 * Check if render is cached
 */
async function checkCache(hash: string): Promise<string | null> {
  const cacheDir = join(process.cwd(), '../cache/manim-renders');
  const cachePath = join(cacheDir, `${hash}.mp4`);
  
  if (existsSync(cachePath)) {
    console.log(`[Cache HIT] Found cached render: ${hash}`);
    return cachePath;
  }
  
  return null;
}

/**
 * Main render processor
 */
manimQueue.process(async (job) => {
  const startTime = Date.now();
  const { problemId, quality, templatePath, className, templateContent } = job.data as ManimRenderJob;
  
  console.log(`[Worker] Starting render for problem: ${problemId}, quality: ${quality}`);
  
  try {
    // Update progress: Initializing
    await job.progress(10);
    
    // Check cache if we have template content
    if (templateContent) {
      const hash = getContentHash(templateContent, quality);
      const cached = await checkCache(hash);
      
      if (cached) {
        await job.progress(100);
        return {
          success: true,
          videoPath: cached,
          videoUrl: `/cache/manim-renders/${hash}.mp4`,
          duration: Date.now() - startTime,
          cached: true
        } as ManimRenderResult;
      }
    }
    
    // Update progress: Validating template
    await job.progress(20);
    
    // Validate template exists
    if (!existsSync(templatePath)) {
      throw new Error(`Template not found: ${templatePath}`);
    }
    
    // Quality flags mapping
    const qualityFlags: { [key: string]: string } = {
      'low': '-ql',
      'medium': '-qm',
      'high': '-qh',
      'ultra': '-qk'
    };
    const qualityFlag = qualityFlags[quality] || '-ql';
    
    // Update progress: Preparing render
    await job.progress(30);
    
    // Build command
    const command = `manim ${qualityFlag} "${templatePath}" ${className}`;
    const cwd = join(process.cwd(), '../tools/manim_templates/top_50');
    
    console.log(`[Worker] Executing: ${command}`);
    console.log(`[Worker] CWD: ${cwd}`);
    
    // Update progress: Rendering (this is the long part)
    await job.progress(40);
    
    // Execute Manim render (async, non-blocking)
    const { stdout, stderr } = await execAsync(command, {
      cwd,
      encoding: 'utf8',
      timeout: 300000,
      maxBuffer: 50 * 1024 * 1024
    });
    
    console.log(`[Worker] Manim output:`, stdout);
    if (stderr) console.warn(`[Worker] Manim stderr:`, stderr);
    
    // Update progress: Processing output
    await job.progress(80);
    
    // Find generated video
    const videoDir = join(cwd, 'media/videos', `manim_${problemId}`, `${quality}p15`);
    let videoFiles: string[] = [];
    
    try {
      videoFiles = readdirSync(videoDir).filter(f => f.endsWith('.mp4'));
    } catch (dirError) {
      console.error(`[Worker] Failed to read video directory: ${videoDir}`, dirError);
      throw new Error(`Video output directory not found: ${videoDir}`);
    }
    
    if (videoFiles.length === 0) {
      throw new Error('No video file generated');
    }
    
    const videoFile = videoFiles[0];
    const videoPath = join(videoDir, videoFile);
    const duration = Date.now() - startTime;
    
    // Update progress: Complete
    await job.progress(100);
    
    console.log(`[Worker] Render complete in ${duration}ms: ${videoPath}`);
    
    return {
      success: true,
      videoPath,
      videoUrl: `/media/videos/manim_${problemId}/${quality}p15/${videoFile}`,
      duration
    } as ManimRenderResult;
    
  } catch (error) {
    console.error(`[Worker] Render failed for ${problemId}:`, error);
    
    return {
      success: false,
      error: error instanceof Error ? error.message : String(error),
      duration: Date.now() - startTime
    } as ManimRenderResult;
  }
});

// Event handlers for monitoring
manimQueue.on('completed', (job, result) => {
  console.log(`[Queue] Job ${job.id} completed in ${result.duration}ms`);
  if (result.cached) {
    console.log(`[Queue] Used cached render`);
  }
});

manimQueue.on('failed', (job, err) => {
  console.error(`[Queue] Job ${job?.id} failed:`, err.message);
});

manimQueue.on('stalled', (job) => {
  console.warn(`[Queue] Job ${job.id} stalled, will retry`);
});

manimQueue.on('error', (error) => {
  console.error('[Queue] Redis connection error:', error);
});

// Graceful shutdown
process.on('SIGTERM', async () => {
  console.log('[Worker] Received SIGTERM, closing queue gracefully...');
  await manimQueue.close();
  process.exit(0);
});

process.on('SIGINT', async () => {
  console.log('[Worker] Received SIGINT, closing queue gracefully...');
  await manimQueue.close();
  process.exit(0);
});

console.log('[Worker] Manim Queue Worker started and ready for jobs');
console.log(`[Worker] Redis URL: ${REDIS_URL}`);
console.log(`[Worker] Concurrency: ${manimQueue.concurrency}`);

export default manimQueue;
