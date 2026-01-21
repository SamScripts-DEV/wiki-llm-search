from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

print("Modelos disponibles para tu API Key:")
for model in client.models.list():
    print(f" - ID: {model.name}")