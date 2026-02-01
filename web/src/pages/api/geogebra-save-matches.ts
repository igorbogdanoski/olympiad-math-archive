import type { APIRoute } from 'astro';
import fs from 'fs/promises';
import path from 'path';

export const POST: APIRoute = async ({ request }) => {
  try {
    const { matches } = await request.json();
    
    if (!matches || !Array.isArray(matches)) {
      return new Response(JSON.stringify({ 
        success: false, 
        error: 'Invalid matches data' 
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Save to file (will be processed by Python script later)
    const outputPath = path.join(process.cwd(), '..', 'geogebra_approved_matches.json');
    
    await fs.writeFile(
      outputPath, 
      JSON.stringify(matches, null, 2),
      'utf-8'
    );

    // Count approved matches
    const approvedCount = matches.filter(m => m.status === 'approved').length;
    const rejectedCount = matches.filter(m => m.status === 'rejected').length;
    const pendingCount = matches.filter(m => m.status === 'pending').length;

    return new Response(JSON.stringify({ 
      success: true,
      message: `Saved ${matches.length} matches`,
      stats: {
        approved: approvedCount,
        rejected: rejectedCount,
        pending: pendingCount
      },
      outputPath
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    console.error('Error saving matches:', error);
    return new Response(JSON.stringify({ 
      success: false, 
      error: error instanceof Error ? error.message : 'Unknown error' 
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};
