import requests

class ApiFootballClient():
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def buscar_artilheiros(self,league_id: int, season: int) -> list:
        """
        busca os artilheiros de uma competição (ex: Copa do Mundo) 
        """

        url = f"{self.base_url}/players/topscorers"
        headers = {
            "x-apisports-key": self.api_key,
            "Content-Type": "application/json",
        }
        params = {"league": league_id, "season": season}

        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("response", [])
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar artilheiros: {e}")
            return []
    