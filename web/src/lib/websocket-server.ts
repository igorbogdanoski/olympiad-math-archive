/**
 * WebSocket Server for Real-Time Manim Render Progress
 * Broadcasts job progress updates to connected clients
 */

import { WebSocketServer, WebSocket } from 'ws';
import type { Server } from 'http';

interface ProgressMessage {
  jobId: string;
  progress: number;
  status: 'waiting' | 'active' | 'completed' | 'failed';
  message?: string;
  result?: any;
}

class ManimProgressServer {
  private wss: WebSocketServer | null = null;
  private clients = new Map<string, Set<WebSocket>>();

  /**
   * Initialize WebSocket server
   */
  init(server: Server) {
    this.wss = new WebSocketServer({ 
      server,
      path: '/ws/manim-progress'
    });

    this.wss.on('connection', (ws: WebSocket) => {
      console.log('[WebSocket] Client connected');

      ws.on('message', (data: Buffer) => {
        try {
          const message = JSON.parse(data.toString());
          
          // Subscribe to job updates
          if (message.type === 'subscribe' && message.jobId) {
            this.subscribe(message.jobId, ws);
            ws.send(JSON.stringify({ 
              type: 'subscribed', 
              jobId: message.jobId 
            }));
          }
          
          // Unsubscribe from job updates
          if (message.type === 'unsubscribe' && message.jobId) {
            this.unsubscribe(message.jobId, ws);
          }
        } catch (err) {
          console.error('[WebSocket] Failed to parse message:', err);
        }
      });

      ws.on('close', () => {
        console.log('[WebSocket] Client disconnected');
        this.removeClient(ws);
      });

      ws.on('error', (error) => {
        console.error('[WebSocket] Error:', error);
      });
    });

    console.log('[WebSocket] Server initialized on /ws/manim-progress');
  }

  /**
   * Subscribe client to job progress
   */
  private subscribe(jobId: string, ws: WebSocket) {
    if (!this.clients.has(jobId)) {
      this.clients.set(jobId, new Set());
    }
    this.clients.get(jobId)!.add(ws);
    console.log(`[WebSocket] Client subscribed to job: ${jobId}`);
  }

  /**
   * Unsubscribe client from job progress
   */
  private unsubscribe(jobId: string, ws: WebSocket) {
    const jobClients = this.clients.get(jobId);
    if (jobClients) {
      jobClients.delete(ws);
      if (jobClients.size === 0) {
        this.clients.delete(jobId);
      }
    }
  }

  /**
   * Remove client from all subscriptions
   */
  private removeClient(ws: WebSocket) {
    this.clients.forEach((clients, jobId) => {
      clients.delete(ws);
      if (clients.size === 0) {
        this.clients.delete(jobId);
      }
    });
  }

  /**
   * Broadcast progress update to subscribed clients
   */
  broadcast(jobId: string, progress: ProgressMessage) {
    const jobClients = this.clients.get(jobId);
    
    if (!jobClients || jobClients.size === 0) {
      return;
    }

    const message = JSON.stringify({
      type: 'progress',
      ...progress
    });

    let sentCount = 0;
    jobClients.forEach((ws) => {
      if (ws.readyState === WebSocket.OPEN) {
        ws.send(message);
        sentCount++;
      }
    });

    console.log(`[WebSocket] Broadcast to ${sentCount} clients for job: ${jobId}`);
  }

  /**
   * Close WebSocket server
   */
  close() {
    if (this.wss) {
      this.wss.close();
      console.log('[WebSocket] Server closed');
    }
  }
}

// Singleton instance
export const progressServer = new ManimProgressServer();
