import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL", "https://v3.football.api-sports.io")

if not API_KEY:
    raise ValueError("API_KEY não encontrada. Verifique se o arquivo .env existe e está configurado.")
