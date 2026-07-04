from config import API_KEY, API_BASE_URL
from servicos.api_client import ApiFootballClient


def main():
    client = ApiFootballClient(api_key=API_KEY, base_url=API_BASE_URL)
    artilheiros = client.buscar_artilheiros(league_id=1, season=2022)

    print(f"Total de artilheiros retornados: {len(artilheiros)}\n")

    for jogador in artilheiros[:5]:
        nome = jogador["player"]["name"]
        gols = jogador["statistics"][0]["goals"]["total"]
        print(f"{nome} - {gols} gols")


if __name__ == "__main__":
    main()
