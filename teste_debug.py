import requests
from config import API_KEY, API_BASE_URL

url = f"{API_BASE_URL}/players/topscorers"
headers = {"x-apisports-key": API_KEY}
params = {"league": 1, "season": 2026}

response = requests.get(url, headers=headers, params=params, timeout=10)
print("Status code:", response.status_code)
print(response.json())
