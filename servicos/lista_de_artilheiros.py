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
        """Se o jogador (mesmo id_api E mesma competição) já existe, atualiza
        os gols/jogos. Se não existe, adiciona como novo.
        Usar (id_api, competicao) como chave evita misturar, por exemplo, os
        gols de um jogador na Copa do Mundo com os gols dele na Premier League."""
        encontrado = False

        for jogador_existente in self.jogadores:
            if (jogador_existente.id_api == jogador_novo.id_api
                    and jogador_existente.competicao == jogador_novo.competicao):
                jogador_existente.atualizar_estatisticas(gols=jogador_novo.gols, jogos=jogador_novo.jogos)
                encontrado = True
                break

        if not encontrado:
            self.adicionar(jogador_novo)

    def ordenar_por_gols(self):
        """Ordena a lista em memória do maior artilheiro pro menor."""
        self.jogadores.sort(key=lambda jogador: jogador.gols, reverse=True)

    def top(self, n: int, competicao: str = None) -> list:
        """Devolve os n maiores artilheiros.
        Se competicao for informada, filtra só os daquela competição."""
        self.ordenar_por_gols()
        if competicao:
            filtrados = [j for j in self.jogadores if j.competicao == competicao]
            return filtrados[:n]
        return self.jogadores[:n]

    def salvar(self):
        """Persiste a lista atual usando o repositório."""
        self.repositorio.salvar(self.jogadores)