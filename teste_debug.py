import requests
from config import API_KEY, API_BASE_URL

url = f"{API_BASE_URL}/competitions/WC/scorers"
headers = {"X-Auth-Token": API_KEY}

response = requests.get(url, headers=headers, timeout=10)
print("Status code:", response.status_code)
print(response.json())