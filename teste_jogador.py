from modelos.jogador import Jogador


def main():
    messi = Jogador(id_api=1, nome="Lionel Messi", selecao="Argentina", gols=6, jogos=4)
    print(messi)
    print("Média de gols:", messi.media_gols())

    messi.atualizar_estatisticas(gols=8, jogos=5)
    print(messi)

    dados = messi.to_dict()
    print(dados)

    messi_reconstruido = Jogador.from_dict(dados)
    print(messi_reconstruido)

    novato = Jogador(id_api=2, nome="Jogador Reserva", selecao="Brasil")
    print("Média sem jogos:", novato.media_gols())


if __name__ == "__main__":
    main()
