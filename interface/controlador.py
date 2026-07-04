from repositorio.artilheiros_repo import RepositorioArtilheiros
from servicos.lista_de_artilheiros import ListaArtilheiros
from servicos.atualizador import Atualizador


class Controlador:
    def __init__(self):
        self.repositorio = RepositorioArtilheiros()
        self.lista = ListaArtilheiros(self.repositorio)
        self.lista.carregar_do_arquivo()
        self.atualizador = Atualizador(self.lista)

    def buscar_top(self, n: int) -> list:
        """Devolve os top N artilheiros já carregados."""
        return self.lista.top(n)

    def atualizar_da_api(self, league_id: int, season: int):
        self.atualizador.atualizar_tudo(league_id=league_id, season=season)
