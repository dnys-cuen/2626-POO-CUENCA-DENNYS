import tkinter as tk
from tkinter import ttk

from modelos.producto import Producto


class MainView(ttk.Frame):
    def __init__(self, master, servicio, on_logout, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.servicio = servicio
        self.on_logout = on_logout
        self._build()
        self.mostrar_usuarios()
        self.mostrar_productos()

    def _build(self):
        self.configure(padding=10)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        nav = ttk.Frame(self, padding=12)
        nav.grid(row=0, column=0, sticky="ns")
        nav.columnconfigure(0, weight=1)

        ttk.Label(nav, text="Navegación", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 10))

        self.btn_usuarios = ttk.Button(nav, text="Usuarios", command=self.mostrar_usuarios)
        self.btn_usuarios.grid(row=1, column=0, sticky="ew", pady=5)

        self.btn_productos = ttk.Button(nav, text="Productos", command=self.mostrar_productos)
        self.btn_productos.grid(row=2, column=0, sticky="ew", pady=5)

        self.btn_logout = ttk.Button(nav, text="Cerrar sesión", command=self.on_logout)
        self.btn_logout.grid(row=3, column=0, sticky="ew", pady=(20, 0))

        content = ttk.Frame(self)
        content.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)

        self.usuarios_frame = ttk.Frame(content, padding=10)
        self.usuarios_frame.grid(row=0, column=0, sticky="nsew")
        self.usuarios_frame.columnconfigure(0, weight=1)
        self.usuarios_frame.rowconfigure(1, weight=1)

        ttk.Label(self.usuarios_frame, text="Consulta de usuarios", font=("Segoe UI", 12, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 8))
        self.usuarios_tree = ttk.Treeview(self.usuarios_frame, columns=("username", "nombre"), show="headings", height=12)
        self.usuarios_tree.heading("username", text="Usuario")
        self.usuarios_tree.heading("nombre", text="Nombre")
        self.usuarios_tree.column("username", width=200, anchor="center")
        self.usuarios_tree.column("nombre", width=250, anchor="center")
        self.usuarios_tree.grid(row=1, column=0, sticky="nsew")

        self.productos_frame = ttk.Frame(content, padding=10)
        self.productos_frame.grid(row=0, column=0, sticky="nsew")
        self.productos_frame.columnconfigure(0, weight=1)
        self.productos_frame.rowconfigure(2, weight=1)

        ttk.Label(self.productos_frame, text="Gestión de productos", font=("Segoe UI", 12, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 12))

        form = ttk.Frame(self.productos_frame)
        form.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        form.columnconfigure(1, weight=1)

        ttk.Label(form, text="ID:").grid(row=0, column=0, sticky="e", padx=(0, 8), pady=4)
        self.id_var = tk.StringVar()
        self.entry_id = ttk.Entry(form, textvariable=self.id_var, width=18)
        self.entry_id.grid(row=0, column=1, sticky="w", pady=4)

        ttk.Label(form, text="Nombre:").grid(row=1, column=0, sticky="e", padx=(0, 8), pady=4)
        self.nombre_var = tk.StringVar()
        self.entry_nombre = ttk.Entry(form, textvariable=self.nombre_var, width=30)
        self.entry_nombre.grid(row=1, column=1, sticky="w", pady=4)

        ttk.Label(form, text="Precio:").grid(row=2, column=0, sticky="e", padx=(0, 8), pady=4)
        self.precio_var = tk.StringVar()
        self.entry_precio = ttk.Entry(form, textvariable=self.precio_var, width=20)
        self.entry_precio.grid(row=2, column=1, sticky="w", pady=4)

        ttk.Label(form, text="Cantidad:").grid(row=3, column=0, sticky="e", padx=(0, 8), pady=4)
        self.cantidad_var = tk.StringVar()
        self.entry_cantidad = ttk.Entry(form, textvariable=self.cantidad_var, width=20)
        self.entry_cantidad.grid(row=3, column=1, sticky="w", pady=4)

        buttons = ttk.Frame(self.productos_frame)
        buttons.grid(row=2, column=0, sticky="ew", pady=(0, 10))
        for i in range(5):
            buttons.columnconfigure(i, weight=1)

        ttk.Button(buttons, text="Registrar", command=self.registrar_producto).grid(row=0, column=0, padx=4, sticky="ew")
        ttk.Button(buttons, text="Consultar", command=self.consultar_producto).grid(row=0, column=1, padx=4, sticky="ew")
        ttk.Button(buttons, text="Actualizar", command=self.actualizar_producto).grid(row=0, column=2, padx=4, sticky="ew")
        ttk.Button(buttons, text="Eliminar", command=self.eliminar_producto).grid(row=0, column=3, padx=4, sticky="ew")
        ttk.Button(buttons, text="Limpiar", command=self.limpiar_formulario).grid(row=0, column=4, padx=4, sticky="ew")

        self.mensaje = ttk.Label(self.productos_frame, text="", foreground="darkgreen")
        self.mensaje.grid(row=3, column=0, sticky="w", pady=(0, 8))

        self.productos_tree = ttk.Treeview(self.productos_frame, columns=("id", "nombre", "precio", "cantidad"), show="headings", height=12)
        self.productos_tree.heading("id", text="ID")
        self.productos_tree.heading("nombre", text="Nombre")
        self.productos_tree.heading("precio", text="Precio")
        self.productos_tree.heading("cantidad", text="Stock")
        self.productos_tree.column("id", width=60, anchor="center")
        self.productos_tree.column("nombre", width=220, anchor="center")
        self.productos_tree.column("precio", width=120, anchor="center")
        self.productos_tree.column("cantidad", width=120, anchor="center")
        self.productos_tree.grid(row=4, column=0, sticky="nsew")

        self.usuarios_frame.grid_forget()
        self.productos_frame.grid(row=0, column=0, sticky="nsew")

    def mostrar_usuarios(self):
        self.productos_frame.grid_forget()
        self.usuarios_frame.grid(row=0, column=0, sticky="nsew")
        self.usuarios_tree.delete(*self.usuarios_tree.get_children())
        for usuario in self.servicio.listar_usuarios():
            self.usuarios_tree.insert("", tk.END, values=(usuario.username, usuario.nombre))

    def mostrar_productos(self):
        self.usuarios_frame.grid_forget()
        self.productos_frame.grid(row=0, column=0, sticky="nsew")
        self.actualizar_tabla_productos()

    def limpiar_formulario(self):
        self.id_var.set("")
        self.nombre_var.set("")
        self.precio_var.set("")
        self.cantidad_var.set("")
        self.mensaje.config(text="")
        self.entry_id.focus_set()

    def actualizar_tabla_productos(self):
        self.productos_tree.delete(*self.productos_tree.get_children())
        for producto in self.servicio.listar_productos():
            self.productos_tree.insert("", tk.END, values=(producto.id, producto.nombre, f"${producto.precio:.2f}", producto.cantidad))

    def _obtener_datos_formulario(self):
        try:
            producto_id = int(self.id_var.get().strip())
        except ValueError:
            return None, "El ID debe ser un número entero."

        nombre = self.nombre_var.get().strip()
        try:
            precio = float(self.precio_var.get().strip())
        except ValueError:
            return None, "El precio debe ser un número válido."

        try:
            cantidad = int(self.cantidad_var.get().strip())
        except ValueError:
            return None, "La cantidad debe ser un número entero."

        return {"id": producto_id, "nombre": nombre, "precio": precio, "cantidad": cantidad}, ""

    def registrar_producto(self):
        datos, error = self._obtener_datos_formulario()
        if error:
            self.mensaje.config(text=error, foreground="darkred")
            return

        producto = self.servicio.obtener_producto(datos["id"])
        if producto:
            self.mensaje.config(text=f"El producto {datos['id']} ya existe. Use Actualizar.", foreground="darkred")
            return

        producto_nuevo = Producto(**datos)
        ok, mensaje = self.servicio.registrar_producto(producto_nuevo)
        self.mensaje.config(text=mensaje, foreground="darkgreen" if ok else "darkred")
        if ok:
            self.actualizar_tabla_productos()
            self.limpiar_formulario()

    def consultar_producto(self):
        try:
            producto_id = int(self.id_var.get().strip())
        except ValueError:
            self.mensaje.config(text="Ingrese un ID válido", foreground="darkred")
            return

        producto = self.servicio.obtener_producto(producto_id)
        if not producto:
            self.mensaje.config(text="Producto no encontrado.", foreground="darkred")
            return

        self.nombre_var.set(producto.nombre)
        self.precio_var.set(str(producto.precio))
        self.cantidad_var.set(str(producto.cantidad))
        self.mensaje.config(text=f"Producto {producto_id} cargado.", foreground="darkgreen")

    def actualizar_producto(self):
        datos, error = self._obtener_datos_formulario()
        if error:
            self.mensaje.config(text=error, foreground="darkred")
            return

        ok, mensaje = self.servicio.actualizar_producto(
            datos["id"], datos["nombre"], datos["precio"], datos["cantidad"]
        )
        self.mensaje.config(text=mensaje, foreground="darkgreen" if ok else "darkred")
        if ok:
            self.actualizar_tabla_productos()
            self.limpiar_formulario()

    def eliminar_producto(self):
        try:
            producto_id = int(self.id_var.get().strip())
        except ValueError:
            self.mensaje.config(text="Ingrese un ID válido para eliminar.", foreground="darkred")
            return

        ok, mensaje = self.servicio.eliminar_producto(producto_id)
        self.mensaje.config(text=mensaje, foreground="darkgreen" if ok else "darkred")
        if ok:
            self.actualizar_tabla_productos()
            self.limpiar_formulario()
