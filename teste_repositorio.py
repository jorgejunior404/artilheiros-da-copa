from servicos.atualizador import Atualizador
from repositorio.artilheiros_repo import RepositorioArtilheiros

atualizador = Atualizador()
artilheiros = atualizador.atualizar()

repositorio = RepositorioArtilheiros()
repositorio.salvar(artilheiros)

print(f"{len(artilheiros)} jogadores salvos em dados/artilheiros.json")
