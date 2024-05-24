import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Configuração da API Key do Google
google_api_key = os.getenv("GOOGLE_GEMINI_API_KEY", None)

# Configuração do modelo Gemini do Google
gemini = ChatGoogleGenerativeAI(
    google_api_key=google_api_key, model="gemini-pro", temperature=0
)


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
        resposta = gemini.invoke(prompt)
        print(resposta)
        return resposta["choices"][0]["text"]
    except Exception as e:
        print(f"Erro ao obter resposta: {e}")
        return None
