from config import API_KEY, API_BASE_URL
from servicos.api_client import FootballDataClient


def main():
    client = FootballDataClient(api_key=API_KEY, base_url=API_BASE_URL)
    artilheiros = client.buscar_artilheiros(competicao="WC")

    print(f"Total de artilheiros retornados: {len(artilheiros)}\n")

    for jogador in artilheiros[:5]:
        nome = jogador["player"]["name"]
        gols = jogador["goals"]
        jogos = jogador.get("playedMatches")
        print(f"{nome} - {gols} gols em {jogos} jogos")


if __name__ == "__main__":
    main()