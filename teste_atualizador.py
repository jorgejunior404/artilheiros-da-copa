from servicos.atualizador import Atualizador

atualizador = Atualizador()
artilheiros = atualizador.atualizar()

for jogador in artilheiros[:5]:
    print(jogador)
