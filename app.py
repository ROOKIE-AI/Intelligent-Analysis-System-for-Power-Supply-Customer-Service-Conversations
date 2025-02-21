import warnings
import streamlit as st
from src.config.settings import PAGE_CONFIG
from src.utils.session import init_session_state, get_config
from src.core.llm import init_llm
from src.core.qa_chain import load_knowledge_base
from src.services.audio import process_audio
from src.services.analysis import analyze_conversation, generate_solution
from src.ui.components import config_ui

# 忽略警告
warnings.filterwarnings("ignore")

# 设置页面配置
st.set_page_config(**PAGE_CONFIG)

def main():
    st.title("供电服务智能问答系统")
    
    # 初始化session state
    init_session_state()
    
    # 显示配置界面
    if not config_ui():
        st.warning("请先完成API配置")
        return
    
    # 初始化LLM和知识库
    config = get_config()
    llm = init_llm(config)
    qa_chain = load_knowledge_base(llm)
    if qa_chain is None:
        return
    
    # 文件上传
    uploaded_file = st.file_uploader("上传音频文件", type=['mp3', 'wav', 'm4a'])
    
    if uploaded_file is not None:
        st.audio(uploaded_file)
        
        if st.button("开始分析"):
            try:
                with st.spinner("正在处理音频..."):
                    # 处理音频文件
                    transcript_text = process_audio(uploaded_file)
                    if transcript_text is None:
                        return
                        
                    st.subheader("通话记录")
                    st.write(transcript_text)
                    
                    # 分析对话
                    st.subheader("通话记录结构化分析")
                    analysis = analyze_conversation(transcript_text, llm)
                    st.markdown(analysis)
                    
                    # 生成解决方案
                    st.subheader("解决方案")
                    solution = generate_solution(transcript_text, llm)
                    st.markdown(solution)
            except Exception as e:
                st.error(f"处理过程中发生错误：{str(e)}")

if __name__ == "__main__":
    main() 