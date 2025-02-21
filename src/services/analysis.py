from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser

def analyze_conversation(text, llm):
    prompt_template = """
    请对以下客服通话记录进行结构化梳理,提取以下要点:
    1. 受理时间
    2. 联系人
    3. 联系地址
    4. 受理内容
    5. 后续跟进事项(如果有)

    通话记录:
    {text}
    """
    
    prompt = PromptTemplate(
        input_variables=["text"],
        template=prompt_template
    )
    
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"text": text})

def generate_solution(text, llm):
    question_template = """
    请根据以下通话记录内容，结合供电营业规则知识库，给出专业的解决方案:

    客户通话记录:
    {text}

    请分析客户问题并给出解决方案:
    1. 明确客户的具体诉求是什么
    2. 根据供电营业规则，提供相应的解决方案
    3. 如果涉及具体流程，请列出办理步骤
    4. 给出相关政策依据或条款说明
    """
    
    question_prompt = PromptTemplate(
        input_variables=["text"],
        template=question_template
    )
    
    question_chain = question_prompt | llm | StrOutputParser()
    return question_chain.invoke({"text": text}) 