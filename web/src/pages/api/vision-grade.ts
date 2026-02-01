import type { APIRoute } from 'astro';
import { GoogleGenerativeAI } from "@google/generative-ai";
import fs from 'fs';
import path from 'path';
import { generateLearningPath, getNode } from '../../utils/knowledgeGraph';

// Иницијализација на Gemini API
const genAI = new GoogleGenerativeAI(import.meta.env.GEMINI_API_KEY || "");

export const POST: APIRoute = async ({ request }) => {
  try {
    const data = await request.formData();
    const imageFile = data.get("image") as File;

    if (!imageFile) {
      return new Response(JSON.stringify({ error: "Нема прикачено слика." }), { 
        status: 400,
        headers: { "Content-Type": "application/json" }
      });
    }

    // Вчитување на екстерниот промпт за подобра одржливост
    const promptPath = path.resolve('./ai/vision_grading_prompt.md');
    let systemPrompt = "";
    try {
        systemPrompt = fs.readFileSync(promptPath, 'utf-8');
    } catch (e) {
        console.error("Failed to read prompt file, using fallback.");
        systemPrompt = "You are a math teacher. Analyze the handwritten solution in the image and provide feedback in JSON.";
    }

    // Конверзија на сликата во Base64 за Gemini
    const arrayBuffer = await imageFile.arrayBuffer();
    const base64Data = Buffer.from(arrayBuffer).toString('base64');

    const model = genAI.getGenerativeModel({ model: "gemini-1.5-pro" });

    const result = await model.generateContent([
      systemPrompt,
      {
        inlineData: {
          data: base64Data,
          mimeType: imageFile.type
        }
      }
    ]);

    const responseText = result.response.text();
    // Чистење на JSON одговорот (во случај AI да додаде markdown тагови)
    const jsonMatch = responseText.match(/\{[\s\S]*\}/);
    const cleanedJson = jsonMatch ? jsonMatch[0] : responseText;

    // Post-process: Enrich response with adaptive learning path
    try {
      const aiResponse = JSON.parse(cleanedJson);
      
      // If AI detected a knowledge gap, enhance it with prerequisite recommendations
      if (aiResponse.knowledgeGap && aiResponse.knowledgeGap.standard) {
        const standardId = aiResponse.knowledgeGap.standard;
        const adaptivePath = generateLearningPath(standardId);
        
        // Merge AI recommendations with knowledge graph insights
        aiResponse.learningPath = aiResponse.learningPath || {};
        aiResponse.learningPath.adaptiveRecommendation = adaptivePath;
        aiResponse.learningPath.knowledgeGraphEnhanced = true;
      }
      
      return new Response(JSON.stringify(aiResponse, null, 2), {
        status: 200,
        headers: { "Content-Type": "application/json" }
      });
    } catch (parseError) {
      // Fallback: return raw response if JSON parsing fails
      console.warn("Failed to enhance response with knowledge graph:", parseError);
      return new Response(cleanedJson, {
        status: 200,
        headers: { "Content-Type": "application/json" }
      });
    }

  } catch (error) {
    console.error("Vision AI Error:", error);
    return new Response(JSON.stringify({ 
        error: "Грешка при анализата", 
        details: error instanceof Error ? error.message : "Unknown error" 
    }), { 
      status: 500,
      headers: { "Content-Type": "application/json" }
    });
  }
};
