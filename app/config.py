import os
from dotenv import load_dotenv

# Carga variables del archivo .env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
WIKIJS_API_URL = os.getenv("WIKIJS_API_URL")
WIKIJS_API_TOKEN = os.getenv("WIKIJS_API_TOKEN")
BASE_WIKI_URL = os.getenv("BASE_WIKI_URL", "http://localhost/")  # Cambia esto por la URL base de tu Wiki.js