import openai
import os
from langchain_openai import OpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Configuração da API Key do OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")


# Configuração do modelo OpenAI GPT-3.5 Turbo
chatgpt = OpenAI(api_key=openai.api_key, model="gpt-3.5-turbo", temperature=0)


# Template de prompt
prompt_template = ChatPromptTemplate.from_template(
    """Responda a pergunta abaixo com base nos dados fornecidos.
    
    Dados: {dataframe}
    
    Pergunta: {question}"""
)


# Função para obter resposta do modelo com base no dataframe
def obter_resposta(pergunta, df):
    dataframe_str = df.to_string(index=False)
    prompt = prompt_template.format(question=pergunta, dataframe=dataframe_str)

    try:
        resposta = chatgpt.invoke(prompt)
        print(resposta)
        return resposta["choices"][0]["text"]
    except Exception as e:
        print(f"Erro ao obter resposta: {e}")
        return None
