import requests


class FootballDataClient:
    """
    Cliente para a football-data.org API v4 (https://www.football-data.org).
    Plano free é gratuito pra sempre e cobre a Copa do Mundo (código WC).
    """

    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def buscar_artilheiros(self, competicao: str, temporada: int = None) -> list:
        """
        Busca os artilheiros de uma competição (ex: "WC" = Copa do Mundo).

        competicao: código da competição na football-data.org (WC, PL, PD, etc.)
        temporada: ano da temporada (opcional; se omitido, usa a temporada atual)

        Levanta requests.exceptions.RequestException se a chamada falhar
        (ex: 403 por pedir uma temporada não liberada no plano free).
        """

        url = f"{self.base_url}/competitions/{competicao}/scorers"
        headers = {"X-Auth-Token": self.api_key}
        params = {}
        if temporada:
            params["season"] = temporada

        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("scorers", [])