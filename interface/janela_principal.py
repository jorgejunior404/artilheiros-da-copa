import customtkinter as ctk
from interface.controlador import Controlador

ctk.set_appearance_mode("System")

COMPETICOES = {
    "Copa do Mundo": 1,
    "Premier League": 39,
    "La Liga": 140,
}

TEMPORADAS = ["2022", "2023", "2024"]


class JanelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.controlador = Controlador()

        self.title("Artilheiros da Copa")
        self.geometry("800x600")

        self._montar_tela_inicial()

    def _montar_tela_inicial(self):
        self.frame_inicial = ctk.CTkFrame(self)
        self.frame_inicial.pack(expand=True, fill="both")

        titulo = ctk.CTkLabel(
            self.frame_inicial, text="Artilheiros da Copa", font=("Arial", 24, "bold")
        )
        titulo.pack(pady=40)

        botao_ver = ctk.CTkButton(
            self.frame_inicial, text="Ver artilheiros", command=self._ir_para_lista
        )
        botao_ver.pack(pady=10)

    def _ir_para_lista(self):
        self.frame_inicial.destroy()
        self._montar_tela_lista()

    def _montar_tela_lista(self):
        self.frame_lista = ctk.CTkFrame(self)
        self.frame_lista.pack(expand=True, fill="both")

        # --- Seletor de competição ---
        self.combo_competicao = ctk.CTkComboBox(
            self.frame_lista, values=list(COMPETICOES.keys())
        )
        self.combo_competicao.set("Copa do Mundo")
        self.combo_competicao.pack(pady=5)

        # --- Seletor de temporada ---
        self.combo_temporada = ctk.CTkComboBox(
            self.frame_lista, values=TEMPORADAS
        )
        self.combo_temporada.set("2022")
        self.combo_temporada.pack(pady=5)

        # --- Botão de atualizar ---
        self.botao_atualizar = ctk.CTkButton(
            self.frame_lista, text="Atualizar da API", command=self._ao_clicar_atualizar
        )
        self.botao_atualizar.pack(pady=10)

        self.lista_texto = ctk.CTkTextbox(self.frame_lista, width=350, height=350)
        self.lista_texto.pack(pady=10)

        self._exibir_top(5)

    def _ao_clicar_atualizar(self):
        nome_competicao = self.combo_competicao.get()
        league_id = COMPETICOES[nome_competicao]
        season = int(self.combo_temporada.get())

        self.controlador.atualizar_da_api(league_id=league_id, season=season)
        self._exibir_top(5)

    def _exibir_top(self, n: int):
        self.lista_texto.delete("1.0", "end")
        top_jogadores = self.controlador.buscar_top(n)
        for jogador in top_jogadores:
            self.lista_texto.insert("end", f"{jogador}\n")