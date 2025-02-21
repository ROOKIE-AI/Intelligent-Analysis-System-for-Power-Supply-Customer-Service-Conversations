import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
import streamlit as st

def load_knowledge_base(llm):
    try:
        pdf_path = os.path.join("data", "供电营业规则.pdf")
        loader = PyPDFLoader(pdf_path)
        pages = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        splits = text_splitter.split_documents(pages)
        
        embeddings = OpenAIEmbeddings(
            openai_api_key=st.session_state.api_key,
            openai_api_base=st.session_state.api_base
        )
        vectorstore = FAISS.from_documents(splits, embeddings)
        
        retriever = vectorstore.as_retriever()
        
        chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever
        )
        
        return chain
    except Exception as e:
        st.error(f"加载知识库时发生错误：{str(e)}")
        return None 