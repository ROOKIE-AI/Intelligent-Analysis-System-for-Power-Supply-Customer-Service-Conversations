import os
import json
import streamlit as st


# 页面配置
PAGE_CONFIG = {
    "page_title": "供电服务智能问答系统",
    "page_icon": "⚡",
    "layout": "wide"
}

# LLM配置
LLM_CONFIG = {
    "model_name": "gpt-4o-mini",
    "temperature": 0
}

# API配置
API_CONFIG = {
    "default_api_base": "https://api.openai.com/v1",
    "default_model": "gpt-4o-mini",
    "whisper_model": "whisper-1"
}

# 知识库配置
KB_CONFIG = {
    "chunk_size": 1000,
    "chunk_overlap": 200
} 

# 加载所有的模型名称列表(同级目录config/models.json)
LLM_NAME = [model['id'] for model in json.load(open(os.path.join(os.path.dirname(__file__), 'models.json')))['models']]




if __name__ == "__main__":
    print(LLM_NAME)
