import customtkinter as ctk
from interface.controlador import Controlador

ctk.set_appearance_mode("System")


class JanelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.controlador = Controlador()

        self.title("Artilheiros da Copa")
        self.geometry("600x600")

        self._montar_tela_inicial()

    def _montar_tela_inicial(self):
        """Tela inicial: só o botão pra começar."""
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
        """Troca a tela inicial pela tela de lista."""
        self.frame_inicial.destroy()
        self._montar_tela_lista()

    def _montar_tela_lista(self):
        """Tela com a lista de artilheiros e botão de atualizar."""
        self.frame_lista = ctk.CTkFrame(self)
        self.frame_lista.pack(expand=True, fill="both")

        self.botao_atualizar = ctk.CTkButton(
            self.frame_lista, text="Atualizar da API", command=self._ao_clicar_atualizar
        )
        self.botao_atualizar.pack(pady=10)

        self.lista_texto = ctk.CTkTextbox(self.frame_lista, width=500, height=500)
        self.lista_texto.pack(pady=10)

        self._exibir_top(5)

    def _ao_clicar_atualizar(self):
        self.controlador.atualizar_da_api()
        self._exibir_top(5)

    def _exibir_top(self, n: int):
        self.lista_texto.delete("1.0", "end")
        top_jogadores = self.controlador.buscar_top(n)
        for jogador in top_jogadores:
            self.lista_texto.insert("end", f"{jogador}\n")