import tkinter as tk
from tkinter import ttk

class LoginView(ttk.Frame):
    def __init__(self, master, servicio, on_login_success, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.servicio = servicio
        self.on_login_success = on_login_success
        self._build()

    def _build(self):
        self.columnconfigure(0, weight=1)
        lbl = ttk.Label(self, text="Acceso - Restaurante App", font=(None, 14))
        lbl.grid(row=0, column=0, pady=10)

        frm = ttk.Frame(self)
        frm.grid(row=1, column=0, pady=5)

        ttk.Label(frm, text="Usuario:").grid(row=0, column=0, sticky="e")
        self.usuario = ttk.Entry(frm)
        self.usuario.grid(row=0, column=1)

        ttk.Label(frm, text="Contraseña:").grid(row=1, column=0, sticky="e")
        self.password = ttk.Entry(frm, show="*")
        self.password.grid(row=1, column=1)

        self.msg = ttk.Label(self, text="", foreground="red")
        self.msg.grid(row=2, column=0, pady=5)

        btn = ttk.Button(self, text="Ingresar", command=self._on_ingresar)
        btn.grid(row=3, column=0, pady=5)

    def _on_ingresar(self):
        user = self.usuario.get().strip()
        pwd = self.password.get().strip()
        if not user or not pwd:
            self.msg.config(text="Ingrese usuario y contraseña")
            return
        ok = self.servicio.validar_usuario(user, pwd)
        if not ok:
            self.msg.config(text="Credenciales inválidas")
            return
        # limpiar campos y mensaje
        self.usuario.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.msg.config(text="")
        self.on_login_success()
