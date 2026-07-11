from config import API_KEY, API_BASE_URL
from servicos.api_client import FootballDataClient
from servicos.lista_de_artilheiros import ListaArtilheiros
from modelos.jogador import Jogador


class Atualizador:
    def __init__(self, lista_artilheiros: ListaArtilheiros):
        self.client = FootballDataClient(api_key=API_KEY, base_url=API_BASE_URL)
        self.lista_artilheiros = lista_artilheiros

    def _converter_jogador(self, dado_bruto: dict, competicao: str) -> Jogador:
        info = dado_bruto['player']

        return Jogador(
            id_api=info['id'],
            nome=info['name'],
            selecao=dado_bruto['team']['name'],
            competicao=competicao,
            gols=dado_bruto.get('goals') or 0,
            jogos=dado_bruto.get('playedMatches') or 0,
        )

    def atualizar_tudo(self, competicao: str, temporada: int = None):

        dados_brutos = self.client.buscar_artilheiros(competicao=competicao, temporada=temporada)
        for dado in dados_brutos:
            jogador = self._converter_jogador(dado, competicao=competicao)
            self.lista_artilheiros.atualizar_jogador(jogador)

        self.lista_artilheiros.salvar()