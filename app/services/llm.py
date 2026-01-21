from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def extract_keywords(question: str) -> str:
    """
    Extrae palabras clave usando el nuevo SDK de Gemini
    """
    prompt = f"""Extrae solo las palabras clave más relevantes de la siguiente pregunta para buscar en una base de conocimientos técnica.
Pregunta: {question}
Responde únicamente con las palabras clave separadas por espacio, sin comas ni explicaciones.
Ejemplo: zabbix agente monitoreo caído
"""
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text.strip() # type: ignore
    except Exception as e:
        print(f"Error al extraer keywords: {e}")
        return question


# def synthesize_wiki_response(query: str, wiki_results: list) -> str:
#     """
#     Sintetiza resultados del Wiki usando Gemini
#     """
#     model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
#     # Construir contexto con los resultados
#     context = "\n\n".join([
#         f"## {result.get('title', 'Sin título')}\n{result.get('content', '')[:800]}"
#         for result in wiki_results[:5]  # Máximo 5 documentos
#     ])
    
#     prompt = f"""Eres un asistente técnico experto. Basándote en la siguiente información de nuestro Wiki interno, responde a la consulta del usuario.

# CONSULTA DEL USUARIO:
# {query}

# INFORMACIÓN DISPONIBLE EN EL WIKI:
# {context}

# INSTRUCCIONES:
# 1. Proporciona una respuesta clara y práctica en 2-3 párrafos
# 2. Si hay pasos a seguir, enuméralos claramente
# 3. Sé específico y técnico cuando sea necesario
# 4. Termina mencionando que hay documentación adicional disponible si necesita profundizar
# 5. Responde en español

# RESPUESTA:"""

#     try:
#         response = model.generate_content(
#             prompt,
#             generation_config=genai.GenerationConfig(
#                 temperature=0.3,  # Más determinista para respuestas técnicas
#                 top_p=0.8,
#                 top_k=40,
#                 max_output_tokens=1024,
#             )
#         )
#         return response.text
#     except Exception as e:
#         return f"Error al generar respuesta: {e}"


# def chat_with_context(messages: list, wiki_context: str = "") -> str:
#     """
#     Chat conversacional con contexto del Wiki
    
#     Args:
#         messages: Lista de mensajes [{"role": "user", "content": "..."}, ...]
#         wiki_context: Contexto adicional del Wiki
#     """
#     model = genai.GenerativeModel(
#         'gemini-2.0-flash-exp',
#         system_instruction=f"""Eres un asistente técnico de soporte interno. 
# Tienes acceso al Wiki de la empresa con información técnica.

# {wiki_context if wiki_context else ""}

# Responde de manera profesional pero amigable, en español."""
#     )
    
#     # Iniciar chat
#     chat = model.start_chat(history=[])
    
#     # Procesar mensajes
#     for msg in messages:
#         if msg["role"] == "user":
#             response = chat.send_message(msg["content"])
    
#     return response.text


# def generate_with_safety(prompt: str, model_name: str = 'gemini-2.0-flash-exp') -> str:
#     """
#     Genera contenido con configuración de seguridad personalizada
#     """
#     from google.generativeai.types import HarmCategory, HarmBlockThreshold
    
#     model = genai.GenerativeModel(
#         model_name,
#         safety_settings={
#             HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
#             HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
#             HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
#             HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
#         }
#     )
    
#     response = model.generate_content(prompt)
#     return response.text


# ============================================
# EJEMPLO DE USO COMPLETO
# ============================================

if __name__ == "__main__":
    question = "¿Qué hago si un agente Zabbix se cae?"
    print("Pregunta:", question)
    print("Palabras clave extraídas:", extract_keywords(question))