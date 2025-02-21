from langchain_openai import ChatOpenAI

def init_llm(config):
    return ChatOpenAI(
        model_name="gpt-4o-mini",
        temperature=0,
        openai_api_key=config['OPENAI_API_KEY'],
        openai_api_base=config['OPENAI_API_BASE']
    ) 