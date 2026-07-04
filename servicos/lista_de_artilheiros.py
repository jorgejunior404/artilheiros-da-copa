class ListaArtilheiros:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.jogadores = []  # lista em memória

    def carregar_do_arquivo(self):
        """Carrega os jogadores salvos, se existirem."""
        self.jogadores = self.repositorio.carregar()
            
    def adicionar(self, jogador):
        """Adiciona um jogador novo à lista."""
        self.jogadores.append(jogador)

    def atualizar_jogador(self, jogador_novo):
        """Se o jogador (mesmo id_api) já existe, atualiza os gols/jogos.
        Se não existe, adiciona como novo."""
        encontrado = False

        for jogador_existente in self.jogadores:
            if jogador_existente.id_api == jogador_novo.id_api:
                jogador_existente.atualizar_estatisticas(gols=jogador_novo.gols, jogos=jogador_novo.jogos)
                encontrado = True
                break

        if not encontrado:
            self.adicionar(jogador_novo)




    def ordenar_por_gols(self):
        """Ordena a lista em memória do maior artilheiro pro menor."""
        self.jogadores.sort(key= lambda jogador: jogador.gols,reverse=True)

    def top(self, n: int) -> list:
        """Devolve os n maiores artilheiros."""
        self.ordenar_por_gols()
        return self.jogadores[:n]
    def salvar(self):
        """Persiste a lista atual usando o repositório."""
        self.repositorio.salvar(self.jogadores)