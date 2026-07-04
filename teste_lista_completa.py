from servicos.atualizador import Atualizador
from repositorio.artilheiros_repo import RepositorioArtilheiros
from servicos.lista_de_artilheiros import ListaArtilheiros

atualizador = Atualizador()
artilheiros_api = atualizador.atualizar()

repositorio = RepositorioArtilheiros()
lista = ListaArtilheiros(repositorio)

for jogador in artilheiros_api:
    lista.atualizar_jogador(jogador)

lista.salvar()

print("Top 5 artilheiros:")
for jogador in lista.top(5):
    print(jogador)
