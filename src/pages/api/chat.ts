export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method not allowed' });
  }

  try {
    const { messages, model } = req.body;

    const completion = await openai.chat.completions.create({
      model: model,
      messages: messages,
      // ... other options ...
    });

    // ... existing code ...
    
  } catch (error) {
    // ... existing error handling ...
  }
} 