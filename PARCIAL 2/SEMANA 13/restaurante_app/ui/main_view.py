import tkinter as tk
from tkinter import ttk

class MainView(ttk.Frame):
    def __init__(self, master, servicio, on_logout, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.servicio = servicio
        self.on_logout = on_logout
        self._build()

    def _build(self):
        header = ttk.Label(self, text="Panel Principal - Restaurante", font=(None, 14))
        header.grid(row=0, column=0, columnspan=3, pady=8)

        btn_users = ttk.Button(self, text="Usuarios", command=self.mostrar_usuarios)
        btn_users.grid(row=1, column=0, padx=5, sticky="w")

        btn_products = ttk.Button(self, text="Productos", command=self.mostrar_productos)
        btn_products.grid(row=1, column=1, padx=5, sticky="w")

        btn_ventas = ttk.Button(self, text="Ventas (pendiente)")
        btn_ventas.grid(row=1, column=2, padx=5, sticky="w")

        self.listbox = tk.Listbox(self, width=60, height=15)
        self.listbox.grid(row=2, column=0, columnspan=3, pady=10)

        btn_logout = ttk.Button(self, text="Cerrar sesión", command=self.on_logout)
        btn_logout.grid(row=3, column=0, columnspan=3, pady=5)

    def mostrar_usuarios(self):
        self.listbox.delete(0, tk.END)
        usuarios = self.servicio.listar_usuarios()
        for u in usuarios:
            self.listbox.insert(tk.END, f"{u.username} - {u.nombre}")

    def mostrar_productos(self):
        self.listbox.delete(0, tk.END)
        productos = self.servicio.listar_productos()
        for p in productos:
            self.listbox.insert(tk.END, f"{p.id} - {p.nombre} - ${p.precio} (stock: {p.cantidad})")
