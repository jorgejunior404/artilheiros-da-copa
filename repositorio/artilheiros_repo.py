import json
from modelos.jogador import Jogador


class RepositorioArtilheiros:
    def __init__(self, caminho_arquivo: str = "dados/artilheiros.json"):
        self.caminho_arquivo = caminho_arquivo

    def salvar(self, jogadores: list) -> None:
        """Salva a lista de jogadores no arquivo JSON."""

        listas_dict = [jogador.to_dict() for jogador in jogadores]

        with open(self.caminho_arquivo,"w",encoding="utf-8") as arquivo:
            json.dump(listas_dict,arquivo, indent=4, ensure_ascii=False)

    def carregar(self) -> list:
        """Carrega a lista de jogadores do arquivo JSON."""

        with open(self.caminho_arquivo, "r", encoding="utf-8") as arquivo:
            listas_dict = json.load(arquivo)

        jogadores = [Jogador.from_dict(dado) for dado in listas_dict]
        return jogadores    