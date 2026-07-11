from repositorio.artilheiros_repo import RepositorioArtilheiros
from servicos.lista_de_artilheiros import ListaArtilheiros
from servicos.atualizador import Atualizador


class Controlador:
    def __init__(self):
        self.repositorio = RepositorioArtilheiros()
        self.lista = ListaArtilheiros(self.repositorio)
        self.lista.carregar_do_arquivo()
        self.atualizador = Atualizador(self.lista)

    def buscar_top(self, n: int, competicao: str = None) -> list:
        """Devolve os top N artilheiros já carregados, opcionalmente filtrados por competição."""
        return self.lista.top(n, competicao=competicao)

    def atualizar_da_api(self, competicao: str, temporada: int = None):
        self.atualizador.atualizar_tudo(competicao=competicao, temporada=temporada)