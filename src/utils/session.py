import streamlit as st

def init_session_state():
    """初始化session state"""
    if 'api_key' not in st.session_state:
        st.session_state.api_key = ''
    if 'api_base' not in st.session_state:
        st.session_state.api_base = ''
    if 'config_saved' not in st.session_state:
        st.session_state.config_saved = False

def save_config(api_key, api_base):
    """保存配置到session state"""
    st.session_state.api_key = api_key
    st.session_state.api_base = api_base
    st.session_state.config_saved = True

def get_config():
    """获取配置"""
    return {
        'OPENAI_API_KEY': st.session_state.api_key,
        'OPENAI_API_BASE': st.session_state.api_base
    } 