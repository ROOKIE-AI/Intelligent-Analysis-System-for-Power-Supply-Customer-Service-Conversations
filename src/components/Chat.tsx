import { useState, useEffect } from 'react';
import { Message } from '../types';

interface ModelConfig {
  models: {
    id: string;
    name: string;
  }[];
  defaultModel: string;
}

interface ModelSelectProps {
  selectedModel: string;
  models: ModelConfig['models'];
  onChange: (model: string) => void;
}

const ModelSelect: React.FC<ModelSelectProps> = ({ selectedModel, models, onChange }) => {
  return (
    <select 
      value={selectedModel}
      onChange={(e) => onChange(e.target.value)}
      className="p-2 border rounded"
    >
      {models.map(model => (
        <option key={model.id} value={model.id}>
          {model.name}
        </option>
      ))}
    </select>
  );
};

interface ChatProps {
  initialMessages?: Message[];
  onSend?: (message: string) => void;
}

function Chat({ initialMessages = [], onSend }: ChatProps) {
  const [modelConfig, setModelConfig] = useState<ModelConfig | null>(null);
  const [selectedModel, setSelectedModel] = useState<string>('');
  const [loading, setLoading] = useState(true);
  const [messages, setMessages] = useState<Message[]>(initialMessages);
  const [input, setInput] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);

  useEffect(() => {
    const loadModelConfig = async () => {
      try {
        const response = await fetch('/api/models');
        const config = await response.json();
        setModelConfig(config);
        setSelectedModel(config.defaultModel);
      } catch (error) {
        console.error('Error loading model config:', error);
      } finally {
        setLoading(false);
      }
    };

    loadModelConfig();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isProcessing) return;

    const newMessage = {
      role: 'user',
      content: input,
    };

    setMessages(prev => [...prev, newMessage]);
    setInput('');
    setIsProcessing(true);

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          messages: [...messages, newMessage],
          model: selectedModel
        }),
      });

      if (!response.ok) {
        throw new Error('请求失败');
      }

      const data = await response.json();
      setMessages(prev => [...prev, {
        role: 'assistant',
        content: data.content
      }]);

      if (onSend) {
        onSend(input);
      }
    } catch (error) {
      console.error('发送消息失败:', error);
      // 可以添加错误提示
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <div className="flex flex-col h-full">
      <div className="mb-4 flex items-center">
        {!loading && modelConfig && (
          <ModelSelect 
            selectedModel={selectedModel}
            models={modelConfig.models}
            onChange={setSelectedModel}
          />
        )}
      </div>

      <div className="flex-1 overflow-y-auto mb-4 p-4 border rounded">
        {messages.map((message, index) => (
          <div 
            key={index}
            className={`mb-4 p-3 rounded ${
              message.role === 'user' 
                ? 'bg-blue-100 ml-auto' 
                : 'bg-gray-100'
            }`}
            style={{ maxWidth: '80%' }}
          >
            <div className="text-sm text-gray-600 mb-1">
              {message.role === 'user' ? '你' : 'AI'}
            </div>
            <div className="whitespace-pre-wrap">{message.content}</div>
          </div>
        ))}
      </div>

      <form onSubmit={handleSubmit} className="flex gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="输入你的问题..."
          className="flex-1 p-2 border rounded"
          disabled={isProcessing}
        />
        <button
          type="submit"
          disabled={isProcessing || !input.trim()}
          className={`px-4 py-2 rounded ${
            isProcessing || !input.trim()
              ? 'bg-gray-300'
              : 'bg-blue-500 hover:bg-blue-600 text-white'
          }`}
        >
          {isProcessing ? '发送中...' : '发送'}
        </button>
      </form>
    </div>
  );
}

export default Chat; 