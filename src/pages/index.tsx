import React, { useState } from 'react';
import Chat from '../components/Chat';

export default function Home() {
  const [analysisComplete, setAnalysisComplete] = useState(false);
  const [analysisResult, setAnalysisResult] = useState('');

  const handleAnalysisComplete = (result: string) => {
    // 将分析结果作为初始消息传入Chat组件
    const initialMessages = [
      {
        role: 'assistant',
        content: result
      }
    ];
    
    setAnalysisResult(result);
    setAnalysisComplete(true);
    return <Chat initialMessages={initialMessages} />;
  };

  return (
    <div className="container mx-auto p-4">
      {/* 其他组件 */}
      {analysisComplete && (
        <div className="mt-8">
          <h2 className="text-xl font-bold mb-4">继续对话</h2>
          <Chat 
            initialMessages={[{
              role: 'assistant',
              content: analysisResult
            }]} 
          />
        </div>
      )}
    </div>
  );
} 