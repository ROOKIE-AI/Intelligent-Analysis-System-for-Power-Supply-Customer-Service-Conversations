import { NextApiRequest, NextApiResponse } from 'next';
import fs from 'fs';
import path from 'path';

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== 'GET') {
    return res.status(405).json({ message: 'Method not allowed' });
  }

  try {
    const configPath = path.join(process.cwd(), 'src/config/models.json');
    const configData = fs.readFileSync(configPath, 'utf8');
    const models = JSON.parse(configData);
    
    res.status(200).json(models);
  } catch (error) {
    console.error('Error reading models config:', error);
    res.status(500).json({ message: '加载模型配置失败' });
  }
} 