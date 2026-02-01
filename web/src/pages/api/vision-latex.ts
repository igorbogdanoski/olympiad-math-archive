import { GoogleGenerativeAI } from '@google/generative-ai';

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

export async function POST({ request }) {
  try {
    const { image } = await request.json();

    // Remove the data:image/png;base64, prefix
    const base64Data = image.replace(/^data:image\/png;base64,/, '');

    const model = genAI.getGenerativeModel({ model: 'gemini-1.5-flash' });

    const prompt = "Look at this handwritten math image. Output ONLY the valid LaTeX code corresponding to the math expression. Do not output markdown code blocks like ```latex. Do not output explanations.";

    const imagePart = {
      inlineData: {
        data: base64Data,
        mimeType: "image/png",
      },
    };

    const result = await model.generateContent([prompt, imagePart]);
    const response = await result.response;
    const latex = response.text().trim();

    return new Response(JSON.stringify({ latex }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (error) {
    console.error('Error in vision-latex API:', error);
    return new Response(JSON.stringify({ error: 'Failed to process image' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}