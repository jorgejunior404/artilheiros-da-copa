import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.football-data.org/v4")

if not API_KEY:
    raise ValueError(
        "API_KEY não encontrada. Verifique se o arquivo .env existe e está configurado. "
        "Crie uma chave grátis em https://www.football-data.org/client/register"
    )