import { useState, useEffect } from 'react';

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

function Chat() {
  const [modelConfig, setModelConfig] = useState<ModelConfig | null>(null);
  const [selectedModel, setSelectedModel] = useState<string>('');
  const [loading, setLoading] = useState(true);

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
    if (!input.trim()) return;

    const newMessage = {
      role: 'user',
      content: input,
    };

    setMessages(prev => [...prev, newMessage]);
    setInput('');

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
      // ... existing code ...
    } catch (error) {
      // ... existing error handling ...
    }
  };

  return (
    <div>
      <div className="mb-4">
        {!loading && modelConfig && (
          <ModelSelect 
            selectedModel={selectedModel}
            models={modelConfig.models}
            onChange={setSelectedModel}
          />
        )}
      </div>
      
      {/* ... existing chat UI code ... */}
    </div>
  );
}

export default Chat; 