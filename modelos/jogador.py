from dataclasses import dataclass, field

@dataclass
class Jogador:
    """
    representa um jogador na Copa do Mundo
    """
    id_api: int
    nome : str
    selecao : str
    gols: int = 0
    jogos: int = 0
    posicao: str = ""

    def media_gols(self) -> float:
        """
        calcula a média de gols do jogador
        """
        if self.jogos == 0:
            return 0.0
        return round(self.gols / self.jogos, 2)

    def atualizar_estatisticas(self,gols:int,jogos:int):
        """
        atualiza as estatísticas do jogador
        """
        self.gols = gols
        self.jogos = jogos

    def to_dict(self) -> dict:
        """Converte o jogador em dicionário, pra salvar em JSON."""
        return {
            "id_api": self.id_api,
            "nome": self.nome,
            "selecao": self.selecao,
            "gols": self.gols,
            "jogos": self.jogos,
            "posicao": self.posicao,
        }

    @classmethod

    def from_dict(cls, data: dict) -> "Jogador":
        """Cria um jogador a partir de um dicionário."""
        return cls(
            id_api=data["id_api"],
            nome=data["nome"],
            selecao=data["selecao"],
            gols=data.get("gols", 0),
            jogos=data.get("jogos", 0),
            posicao=data.get("posicao", ""),
        )

    def __str__(self) -> str:
        return f"{self.nome} ({self.selecao}) - {self.gols} gols"
        