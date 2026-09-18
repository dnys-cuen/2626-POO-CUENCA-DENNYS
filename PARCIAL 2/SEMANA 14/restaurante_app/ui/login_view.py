import tkinter as tk
from tkinter import ttk


class LoginView(ttk.Frame):
    def __init__(self, master, servicio, on_login_success, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.servicio = servicio
        self.on_login_success = on_login_success
        self._build()

    def _build(self):
        self.configure(padding=20)
        self.columnconfigure(0, weight=1)

        title = ttk.Label(self, text="Acceso - Restaurante App", font=("Segoe UI", 16, "bold"))
        title.grid(row=0, column=0, pady=(0, 15))

        card = ttk.Frame(self, padding=20)
        card.grid(row=1, column=0, sticky="nsew")
        card.columnconfigure(1, weight=1)

        ttk.Label(card, text="Usuario:").grid(row=0, column=0, sticky="e", padx=(0, 10), pady=5)
        self.usuario = ttk.Entry(card, width=30)
        self.usuario.grid(row=0, column=1, sticky="ew", pady=5)

        ttk.Label(card, text="Contraseña:").grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5)
        self.password = ttk.Entry(card, show="*", width=30)
        self.password.grid(row=1, column=1, sticky="ew", pady=5)

        self.msg = ttk.Label(card, text="", foreground="red")
        self.msg.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        btn = ttk.Button(card, text="Ingresar", command=self._on_ingresar)
        btn.grid(row=3, column=0, columnspan=2, pady=(15, 0), sticky="ew")

        self.usuario.focus_set()

    def _on_ingresar(self):
        user = self.usuario.get().strip()
        pwd = self.password.get().strip()

        if not user or not pwd:
            self.msg.config(text="Ingrese usuario y contraseña")
            return

        if not self.servicio.validar_usuario(user, pwd):
            self.msg.config(text="Credenciales inválidas")
            return

        self.usuario.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.msg.config(text="")
        self.on_login_success()
