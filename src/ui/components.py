import streamlit as st
from src.utils.session import save_config
from src.config.settings import API_CONFIG, LLM_CONFIG, KB_CONFIG, LLM_NAME

def config_ui():
    """配置界面"""
    with st.sidebar:
        st.header("API配置")
        
        # API密钥配置说明
        with st.expander("配置说明"):
            st.markdown("""
            ### API配置说明
            1. **API Key**: 
               - OpenAI API密钥
               - 获取方式：[OpenAI API Keys](https://platform.openai.com/api-keys)
            
            2. **API Base URL**: 
               - API接口地址
               - 默认使用OpenAI官方接口
               - 也可使用其他兼容的API服务商
            
            3. **注意事项**:
               - 请妥善保管API密钥
               - 建议使用环境变量管理密钥
            """)
        
        # API配置
        api_key = st.text_input("API Key", value=st.session_state.api_key, type="password")
        api_base = st.text_input(
            "API Base URL", 
            value=st.session_state.api_base or API_CONFIG["default_api_base"],
            help="默认使用OpenAI官方接口，可选择其他兼容的API服务商"
        )
        
        # 模型参数配置
        st.subheader("模型参数")
        model = st.selectbox(
            "选择模型",
            LLM_NAME,
            index=0,
            help="选择要使用的语言模型"
        )
        
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=float(LLM_CONFIG["temperature"]),
            step=0.1,
            help="控制输出的随机性：0表示固定输出，1表示最大随机性"
        )
        
        # 知识库参数
        with st.expander("知识库参数"):
            chunk_size = st.number_input(
                "分块大小",
                min_value=100,
                max_value=2000,
                value=int(KB_CONFIG["chunk_size"]),
                help="文档分块大小，影响检索精度"
            )
            chunk_overlap = st.number_input(
                "重叠大小",
                min_value=0,
                max_value=500,
                value=int(KB_CONFIG["chunk_overlap"]),
                help="文档分块重叠大小，防止上下文断裂"
            )
        
        if st.button("保存配置"):
            if not api_key:
                st.error("请填写API Key")
                return False
                
            save_config(
                api_key=api_key,
                api_base=api_base or API_CONFIG["default_api_base"],
                model=model,
                temperature=temperature,
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )
            st.success("配置已保存")
            return True
    
    return st.session_state.config_saved