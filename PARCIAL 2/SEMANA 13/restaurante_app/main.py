import tkinter as tk
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView
from pathlib import Path

BASE_DIR = Path(__file__).parent

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App")
        # preparar servicios
        archivos = ArchivoServicio(BASE_DIR / "datos")
        self.servicio = RestauranteServicio(archivos)
        # vistas
        self.login_view = LoginView(root, self.servicio, self.mostrar_main)
        self.main_view = MainView(root, self.servicio, self.mostrar_login)
        # mostrar login inicialmente
        self.current = None
        self.mostrar_login()

    def mostrar_login(self):
        if self.current:
            self.current.grid_forget()
        self.login_view.grid(row=0, column=0, padx=20, pady=20)
        self.current = self.login_view

    def mostrar_main(self):
        if self.current:
            self.current.grid_forget()
        self.main_view.grid(row=0, column=0, padx=20, pady=20)
        self.current = self.main_view

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
