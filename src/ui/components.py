import streamlit as st
from src.utils.session import save_config

def config_ui():
    """配置界面"""
    with st.sidebar:
        st.header("API配置")
        api_key = st.text_input("API Key", value=st.session_state.api_key, type="password")
        api_base = st.text_input("API Base URL", value=st.session_state.api_base)
        
        if st.button("保存配置"):
            if not api_key or not api_base:
                st.error("请填写完整的配置信息")
                return False
            save_config(api_key, api_base)
            st.success("配置已保存")
            return True
    
    return st.session_state.config_saved 