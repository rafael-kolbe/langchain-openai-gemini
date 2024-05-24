import os

from flask import Flask, request, jsonify
from data import df
import openai_config
import gemini_config

app = Flask(__name__)


@app.route("/ask", methods=["POST"])
def perguntar():
    dados = request.json
    pergunta = dados.get("pergunta")
    llm = dados.get("llm")

    try:
        if llm == "openai":
            resposta = openai_config.obter_resposta(pergunta, df)
        elif llm == "gemini":
            resposta = gemini_config.obter_resposta(pergunta, df)
        else:
            resposta = df.to_string(index=False)

        return jsonify({"resposta": resposta})
    except Exception as e:
        print(e)


if __name__ == "__main__":
    port = int(os.getenv("FLASK_PORT", 8080))
    app.run(debug=True, port=port)
