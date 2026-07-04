from config import API_KEY, API_BASE_URL
from servicos.api_client import ApiFootballClient
from servicos.lista_de_artilheiros import ListaArtilheiros
from modelos.jogador import Jogador


class Atualizador:
    def __init__(self, lista_artilheiros: ListaArtilheiros):
        self.client = ApiFootballClient(api_key=API_KEY, base_url=API_BASE_URL)
        self.lista_artilheiros = lista_artilheiros

    def _converter_jogador(self, dado_bruto: dict) -> Jogador:
        info = dado_bruto['player']
        estatisticas = dado_bruto['statistics'][0]

        return Jogador(
            id_api=info['id'],
            nome=info['name'],
            selecao=estatisticas['team']['name'],
            gols=estatisticas['goals']['total'] or 0,
            jogos=estatisticas['games']['appearences'] or 0,
        )

    def atualizar_tudo(self):
        """Busca os artilheiros na API, atualiza a lista e salva no arquivo."""
        dados_brutos = self.client.buscar_artilheiros(league_id=1, season=2022)

        for dado in dados_brutos:
            jogador = self._converter_jogador(dado)
            self.lista_artilheiros.atualizar_jogador(jogador)

        self.lista_artilheiros.salvar()