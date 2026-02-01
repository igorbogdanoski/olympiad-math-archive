/**
 * Manim Job Status API - Check render job progress and results
 * GET /api/manim-status?jobId=123
 */

import type { APIRoute } from 'astro';
import Queue from 'bull';

const REDIS_URL = process.env.REDIS_URL || 'redis://localhost:6379';
const manimQueue = new Queue('manim-renders', REDIS_URL);

export const GET: APIRoute = async ({ url }) => {
  try {
    const jobId = url.searchParams.get('jobId');

    if (!jobId) {
      return new Response(JSON.stringify({
        error: 'Missing jobId parameter'
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Get job from queue
    const job = await manimQueue.getJob(jobId);

    if (!job) {
      return new Response(JSON.stringify({
        error: 'Job not found',
        jobId
      }), {
        status: 404,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Get job state
    const state = await job.getState();
    const progress = (job as any)._progress || 0;
    const result = job.returnvalue;
    const failedReason = job.failedReason;

    // Return job status
    return new Response(JSON.stringify({
      jobId,
      state,
      progress,
      result: state === 'completed' ? result : null,
      error: state === 'failed' ? failedReason : null,
      timestamp: job.timestamp,
      processedOn: job.processedOn,
      finishedOn: job.finishedOn
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    console.error('[manim-status] Error:', error);
    return new Response(JSON.stringify({
      error: 'Internal server error',
      details: error instanceof Error ? error.message : String(error)
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};
