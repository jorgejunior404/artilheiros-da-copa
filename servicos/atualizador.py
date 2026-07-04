from config import API_KEY, API_BASE_URL
from servicos.api_client import ApiFootballClient
from modelos.jogador import Jogador


class Atualizador:
    def __init__(self):
        self.client = ApiFootballClient(api_key=API_KEY, base_url=API_BASE_URL)

    def _converter_jogador(self, dado_bruto: dict) -> Jogador:
        info = dado_bruto['player']
        estatisticas = dado_bruto['statistics'][0]

        return Jogador (
            id_api=info['id'],
            nome= info["name"],
            selecao= estatisticas["team"]["name"],
            gols= estatisticas["goals"]["total"]or 0,
            jogos= estatisticas["games"]["appearences"] or 0
        )

    def atualizar(self) -> list:
        dados_brutos = self.client.buscar_artilheiros(league_id=1, season=2022)
        top_artilheiros = []
        for dado in dados_brutos:
            jogador = self._converter_jogador(dado)
            top_artilheiros.append(jogador)

        return top_artilheiros
        

        
