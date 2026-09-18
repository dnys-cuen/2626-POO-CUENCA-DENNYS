import tkinter as tk
from pathlib import Path

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

BASE_DIR = Path(__file__).resolve().parent


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App - Semana 14")
        self.root.geometry("1100x650")
        self.root.minsize(900, 550)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        archivos = ArchivoServicio(BASE_DIR / "datos")
        self.servicio = RestauranteServicio(archivos)

        self.login_view = LoginView(root, self.servicio, self.mostrar_main)
        self.main_view = MainView(root, self.servicio, self.mostrar_login)

        self.current = None
        self.mostrar_login()

    def mostrar_login(self):
        if self.current:
            self.current.grid_forget()
        self.login_view.grid(row=0, column=0, sticky="nsew")
        self.current = self.login_view

    def mostrar_main(self):
        if self.current:
            self.current.grid_forget()
        self.main_view.grid(row=0, column=0, sticky="nsew")
        self.current = self.main_view


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
