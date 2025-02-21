import streamlit as st
from src.config.settings import API_CONFIG, LLM_CONFIG, KB_CONFIG

def init_session_state():
    """初始化session state"""
    if 'api_key' not in st.session_state:
        st.session_state.api_key = ''
    if 'api_base' not in st.session_state:
        st.session_state.api_base = API_CONFIG["default_api_base"]
    if 'model' not in st.session_state:
        st.session_state.model = LLM_CONFIG["model_name"]
    if 'temperature' not in st.session_state:
        st.session_state.temperature = LLM_CONFIG["temperature"]
    if 'chunk_size' not in st.session_state:
        st.session_state.chunk_size = KB_CONFIG["chunk_size"]
    if 'chunk_overlap' not in st.session_state:
        st.session_state.chunk_overlap = KB_CONFIG["chunk_overlap"]
    if 'config_saved' not in st.session_state:
        st.session_state.config_saved = False

def save_config(api_key, api_base, model, temperature, chunk_size, chunk_overlap):
    """保存配置到session state"""
    st.session_state.api_key = api_key
    st.session_state.api_base = api_base
    st.session_state.model = model
    st.session_state.temperature = temperature
    st.session_state.chunk_size = chunk_size
    st.session_state.chunk_overlap = chunk_overlap
    st.session_state.config_saved = True

def get_config():
    """获取配置"""
    return {
        'OPENAI_API_KEY': st.session_state.api_key,
        'OPENAI_API_BASE': st.session_state.api_base,
        'MODEL_NAME': st.session_state.model,
        'TEMPERATURE': st.session_state.temperature,
        'CHUNK_SIZE': st.session_state.chunk_size,
        'CHUNK_OVERLAP': st.session_state.chunk_overlap
    } 