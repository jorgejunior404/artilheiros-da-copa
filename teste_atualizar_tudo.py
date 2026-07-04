from repositorio.artilheiros_repo import RepositorioArtilheiros
from servicos.lista_de_artilheiros import ListaArtilheiros
from servicos.atualizador import Atualizador

repositorio = RepositorioArtilheiros()
lista = ListaArtilheiros(repositorio)
lista.carregar_do_arquivo()

atualizador = Atualizador(lista)
atualizador.atualizar_tudo()

print("Top 5 após atualização:")
for jogador in lista.top(5):
    print(jogador)
