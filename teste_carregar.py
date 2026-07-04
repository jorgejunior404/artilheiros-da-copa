from repositorio.artilheiros_repo import RepositorioArtilheiros

repositorio = RepositorioArtilheiros()
artilheiros = repositorio.carregar()

print(f"{len(artilheiros)} jogadores carregados:\n")
for jogador in artilheiros[:5]:
    print(jogador)
