import customtkinter as ctk
from tkinter import messagebox
import requests
from interface.controlador import Controlador

ctk.set_appearance_mode("System")

COMPETICOES = {
    "Copa do Mundo": "WC",
    "Premier League": "PL",
    "La Liga": "PD",
}

TEMPORADAS = ["2026", "2024", "2022"]


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
            self.frame_lista, values=list(COMPETICOES.keys()),
            command=self._ao_trocar_competicao,
        )
        self.combo_competicao.set("Copa do Mundo")
        self.combo_competicao.pack(pady=5)

        # --- Seletor de temporada ---
        self.combo_temporada = ctk.CTkComboBox(
            self.frame_lista, values=TEMPORADAS
        )
        self.combo_temporada.set("2026")
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
        codigo_competicao = COMPETICOES[nome_competicao]
        temporada = int(self.combo_temporada.get())

        self.botao_atualizar.configure(state="disabled", text="Atualizando...")
        self.update()

        try:
            self.controlador.atualizar_da_api(competicao=codigo_competicao, temporada=temporada)
            self._exibir_top(5)
        except requests.exceptions.HTTPError as e:
            if e.response is not None and e.response.status_code == 403:
                messagebox.showerror(
                    "Acesso negado (403)",
                    f"O plano free da football-data.org não libera a temporada {temporada} "
                    f"para {nome_competicao}. Tente a temporada atual (2026)."
                )
            else:
                messagebox.showerror("Erro na API", f"Falha ao atualizar: {e}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro de conexão", f"Não foi possível falar com a API: {e}")
        finally:
            self.botao_atualizar.configure(state="normal", text="Atualizar da API")

    def _ao_trocar_competicao(self, _valor_selecionado=None):
        self._exibir_top(5)

    def _exibir_top(self, n: int):
        nome_competicao = self.combo_competicao.get()
        codigo_competicao = COMPETICOES[nome_competicao]

        self.lista_texto.delete("1.0", "end")
        top_jogadores = self.controlador.buscar_top(n, competicao=codigo_competicao)

        if not top_jogadores:
            self.lista_texto.insert(
                "end", f"Sem dados de {nome_competicao} ainda. Clica em 'Atualizar da API'.\n"
            )
            return

        for jogador in top_jogadores:
            self.lista_texto.insert("end", f"{jogador}\n")