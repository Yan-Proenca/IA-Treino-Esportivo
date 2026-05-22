import os
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from google import genai
from google.genai import types
from dotenv import load_dotenv
from config import CRONOGRAMA_TREINO_SCHEMA, SYSTEM_INSTRUCTION
from flasgger import Swagger

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

app = Flask(__name__)
CORS(app)
swagger = Swagger(app, template_file='openapi.yaml')


def generate_workout_plan(perfil_usuario):
    modalidades_str = ", ".join(perfil_usuario.get("modalidades", []))
    
    conteudo_prompt = f"""
    Crie um cronograma e rotina de treinos altamente personalizada com base nos seguintes dados do usuário:
    - Objetivos principais: {perfil_usuario.get('objetivos')}
    - Nível de experiência: {perfil_usuario.get('nivel_experiencia')}
    - Frequência semanal desejada: {perfil_usuario.get('frequencia_semanal')}
    - Modalidades de interesse: {modalidades_str}
    - Limitações físicas ou observações extras: {perfil_usuario.get('limitacoes', 'Nenhuma informada')}
    """
    
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=conteudo_prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            response_mime_type="application/json",
            response_schema=CRONOGRAMA_TREINO_SCHEMA,
        )
    )
    return response.text

@app.route("/")
def root():
    return jsonify({
        "status": "success",
        "message": "API de Treinos operando de forma independente!",
        "version": "1.0"
    }), 200

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    
    if not data:
        return jsonify({
            "status": "error",
            "message": "Por favor, envie os dados do perfil de treino no formato JSON."
        }), 400
        
    campos_obrigatorios = ["objetivos", "nivel_experiencia", "frequencia_semanal", "modalidades"]
    for campo in campos_obrigatorios:
        if campo not in data:
            return jsonify({
                "status": "error",
                "message": f"O campo '{campo}' é obrigatório."
            }), 400
            
    modalidades = data.get("modalidades", [])
    if not isinstance(modalidades, list) or len(modalidades) == 0:
        return jsonify({
            "status": "error",
            "message": "O campo 'modalidades' deve ser uma lista."
        }), 400
    
    try:
        cronograma_json_string = generate_workout_plan(data)
        cronograma_estruturado = json.loads(cronograma_json_string)
        
        return jsonify({
            "status": "success",
            "cronograma_treino": cronograma_estruturado
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Erro ao gerar o cronograma: {str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(debug=True)