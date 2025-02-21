import os
from openai import OpenAI
import streamlit as st

def process_audio(audio_file):
    """处理音频文件"""
    temp_audio_path = None
    try:
        temp_audio_path = f"temp_audio.{audio_file.name.split('.')[-1]}"
        
        with open(temp_audio_path, "wb") as f:
            f.write(audio_file.getvalue())
        
        client = OpenAI(
            api_key=st.session_state.api_key,
            base_url=st.session_state.api_base
        )
        
        with open(temp_audio_path, "rb") as audio:
            response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio
            )
            
        return response.text
    except Exception as e:
        st.error(f"音频处理失败：{str(e)}")
        return None
    finally:
        if temp_audio_path and os.path.exists(temp_audio_path):
            os.remove(temp_audio_path) 