import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

from modelos.producto import Producto
from modelos.usuario import Usuario


class MainView(ttk.Frame):
    def __init__(self, master, servicio, on_logout, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.servicio = servicio
        self.on_logout = on_logout
        self.usuario_actual = None
        self._build()
        self.mostrar_productos()

    def set_usuario_actual(self, username):
        self.usuario_actual = username
        self._configurar_permisos()

    def _es_administrador(self):
        if not self.usuario_actual:
            return False
        usuario = self.servicio.obtener_usuario(self.usuario_actual)
        return bool(usuario and usuario.rol == "Administrador")

    def _configurar_permisos(self):
        if hasattr(self, "btn_usuarios"):
            if self._es_administrador():
                self.btn_usuarios.configure(state="normal")
                self.btn_usuarios.grid()
            else:
                self.btn_usuarios.configure(state="disabled")
                self.btn_usuarios.grid_remove()

    def _build(self):
        self.configure(padding=10)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        nav = ttk.Frame(self, padding=12)
        nav.grid(row=0, column=0, sticky="ns")
        nav.columnconfigure(0, weight=1)

        ttk.Label(nav, text="Navegación", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 10))

        assets_dir = Path(__file__).resolve().parent.parent / "assets"

        def _load_image(name):
            p = assets_dir / name
            try:
                if p.exists():
                    return tk.PhotoImage(file=str(p))
            except Exception:
                return None
            return None

        self.icon_users = _load_image("icon_users.png")
        self.icon_products = _load_image("icon_products.png")
        self.icon_sales = _load_image("icon_sales.png")
        self.icon_logout = _load_image("icon_logout.png")
        self.banner_img = _load_image("banner.png")

        if self.banner_img:
            lbl_banner = ttk.Label(self, image=self.banner_img)
            lbl_banner.image = self.banner_img
            lbl_banner.grid(row=0, column=1, sticky="ew", padx=(10, 0), pady=(6, 0))

        if self.icon_users:
            self.btn_usuarios = ttk.Button(nav, text="Usuarios", image=self.icon_users, compound="left", command=self.mostrar_usuarios)
        else:
            self.btn_usuarios = ttk.Button(nav, text="Usuarios", command=self.mostrar_usuarios)
        self.btn_usuarios.grid(row=1, column=0, sticky="ew", pady=5)

        if self.icon_products:
            self.btn_productos = ttk.Button(nav, text="Productos", image=self.icon_products, compound="left", command=self.mostrar_productos)
        else:
            self.btn_productos = ttk.Button(nav, text="Productos", command=self.mostrar_productos)
        self.btn_productos.grid(row=2, column=0, sticky="ew", pady=5)

        if self.icon_sales:
            self.btn_ventas = ttk.Button(nav, text="Ventas", image=self.icon_sales, compound="left", command=self.mostrar_ventas)
        else:
            self.btn_ventas = ttk.Button(nav, text="Ventas", command=self.mostrar_ventas)
        self.btn_ventas.grid(row=3, column=0, sticky="ew", pady=5)

        if self.icon_logout:
            self.btn_logout = ttk.Button(nav, text="Cerrar sesión", image=self.icon_logout, compound="left", command=self.on_logout)
        else:
            self.btn_logout = ttk.Button(nav, text="Cerrar sesión", command=self.on_logout)
        self.btn_logout.grid(row=4, column=0, sticky="ew", pady=(20, 0))

        content = ttk.Frame(self)
        content.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)

        self.usuarios_frame = ttk.Frame(content, padding=10)
        self.usuarios_frame.grid(row=0, column=0, sticky="nsew")
        self.usuarios_frame.columnconfigure(0, weight=1)
        self.usuarios_frame.rowconfigure(4, weight=1)

        ttk.Label(self.usuarios_frame, text="Gestión de usuarios", font=("Segoe UI", 12, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 8))

        form = ttk.Frame(self.usuarios_frame)
        form.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        form.columnconfigure(1, weight=1)

        ttk.Label(form, text="ID:").grid(row=0, column=0, sticky="e", padx=(0, 8), pady=4)
        self.usuario_id_var = tk.StringVar()
        self.entry_usuario_id = ttk.Entry(form, textvariable=self.usuario_id_var, width=12)
        self.entry_usuario_id.grid(row=0, column=1, sticky="w", pady=4)

        ttk.Label(form, text="Nombre:").grid(row=1, column=0, sticky="e", padx=(0, 8), pady=4)
        self.usuario_nombre_var = tk.StringVar()
        self.entry_usuario_nombre = ttk.Entry(form, textvariable=self.usuario_nombre_var, width=30)
        self.entry_usuario_nombre.grid(row=1, column=1, sticky="w", pady=4)

        ttk.Label(form, text="Usuario:").grid(row=2, column=0, sticky="e", padx=(0, 8), pady=4)
        self.usuario_username_var = tk.StringVar()
        self.entry_usuario_username = ttk.Entry(form, textvariable=self.usuario_username_var, width=25)
        self.entry_usuario_username.grid(row=2, column=1, sticky="w", pady=4)

        ttk.Label(form, text="Contraseña:").grid(row=3, column=0, sticky="e", padx=(0, 8), pady=4)
        self.usuario_password_var = tk.StringVar()
        self.entry_usuario_password = ttk.Entry(form, textvariable=self.usuario_password_var, show="*", width=25)
        self.entry_usuario_password.grid(row=3, column=1, sticky="w", pady=4)

        ttk.Label(form, text="Rol:").grid(row=4, column=0, sticky="e", padx=(0, 8), pady=4)
        self.usuario_rol_var = tk.StringVar(value="Cliente")
        self.usuario_rol_combo = ttk.Combobox(form, textvariable=self.usuario_rol_var, state="readonly", values=["Administrador", "Empleado", "Cliente"], width=20)
        self.usuario_rol_combo.grid(row=4, column=1, sticky="w", pady=4)

        buttons = ttk.Frame(self.usuarios_frame)
        buttons.grid(row=2, column=0, sticky="ew", pady=(0, 10))
        for i in range(4):
            buttons.columnconfigure(i, weight=1)

        ttk.Button(buttons, text="Registrar", command=self.registrar_usuario).grid(row=0, column=0, padx=4, sticky="ew")
        ttk.Button(buttons, text="Actualizar", command=self.actualizar_usuario).grid(row=0, column=1, padx=4, sticky="ew")
        ttk.Button(buttons, text="Eliminar", command=self.eliminar_usuario).grid(row=0, column=2, padx=4, sticky="ew")
        ttk.Button(buttons, text="Limpiar", command=self.limpiar_formulario_usuario).grid(row=0, column=3, padx=4, sticky="ew")

        self.mensaje_usuarios = ttk.Label(self.usuarios_frame, text="", foreground="darkgreen")
        self.mensaje_usuarios.grid(row=3, column=0, sticky="w", pady=(0, 8))

        self.usuarios_tree = ttk.Treeview(self.usuarios_frame, columns=("id", "nombre", "username", "rol"), show="headings", height=12)
        self.usuarios_tree.heading("id", text="ID")
        self.usuarios_tree.heading("nombre", text="Nombre")
        self.usuarios_tree.heading("username", text="Usuario")
        self.usuarios_tree.heading("rol", text="Rol")
        self.usuarios_tree.column("id", width=60, anchor="center")
        self.usuarios_tree.column("nombre", width=220, anchor="center")
        self.usuarios_tree.column("username", width=180, anchor="center")
        self.usuarios_tree.column("rol", width=150, anchor="center")
        vusuarios = ttk.Scrollbar(self.usuarios_frame, orient="vertical", command=self.usuarios_tree.yview)
        self.usuarios_tree.configure(yscrollcommand=vusuarios.set)
        self.usuarios_tree.grid(row=4, column=0, sticky="nsew")
        vusuarios.grid(row=4, column=1, sticky="ns", padx=(4, 0))
        self.usuarios_tree.bind("<<TreeviewSelect>>", self._on_usuario_seleccionado)
        self.usuario_rol_combo.bind("<<ComboboxSelected>>", self._on_role_selected)

        for widget in [
            self.entry_usuario_id,
            self.entry_usuario_nombre,
            self.entry_usuario_username,
            self.entry_usuario_password,
            self.usuario_rol_combo,
        ]:
            widget.bind("<Return>", self._on_return_usuario)

        self.usuarios_frame.bind("<Escape>", self._on_escape_usuario)

        self.productos_frame = ttk.Frame(content, padding=10)
        self.productos_frame.grid(row=0, column=0, sticky="nsew")
        self.productos_frame.columnconfigure(0, weight=1)
        self.productos_frame.rowconfigure(2, weight=1)

        ttk.Label(self.productos_frame, text="Gestión de productos", font=("Segoe UI", 12, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 12))

        form_producto = ttk.Frame(self.productos_frame)
        form_producto.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        form_producto.columnconfigure(1, weight=1)

        ttk.Label(form_producto, text="ID:").grid(row=0, column=0, sticky="e", padx=(0, 8), pady=4)
        self.id_var = tk.StringVar()
        self.entry_id = ttk.Entry(form_producto, textvariable=self.id_var, width=18)
        self.entry_id.grid(row=0, column=1, sticky="w", pady=4)

        ttk.Label(form_producto, text="Nombre:").grid(row=1, column=0, sticky="e", padx=(0, 8), pady=4)
        self.nombre_var = tk.StringVar()
        self.entry_nombre = ttk.Entry(form_producto, textvariable=self.nombre_var, width=30)
        self.entry_nombre.grid(row=1, column=1, sticky="w", pady=4)

        ttk.Label(form_producto, text="Precio:").grid(row=2, column=0, sticky="e", padx=(0, 8), pady=4)
        self.precio_var = tk.StringVar()
        self.entry_precio = ttk.Entry(form_producto, textvariable=self.precio_var, width=20)
        self.entry_precio.grid(row=2, column=1, sticky="w", pady=4)

        ttk.Label(form_producto, text="Cantidad:").grid(row=3, column=0, sticky="e", padx=(0, 8), pady=4)
        self.cantidad_var = tk.StringVar()
        self.entry_cantidad = ttk.Entry(form_producto, textvariable=self.cantidad_var, width=20)
        self.entry_cantidad.grid(row=3, column=1, sticky="w", pady=4)

        buttons_producto = ttk.Frame(self.productos_frame)
        buttons_producto.grid(row=2, column=0, sticky="ew", pady=(0, 10))
        for i in range(5):
            buttons_producto.columnconfigure(i, weight=1)

        ttk.Button(buttons_producto, text="Registrar", command=self.registrar_producto).grid(row=0, column=0, padx=4, sticky="ew")
        ttk.Button(buttons_producto, text="Consultar", command=self.consultar_producto).grid(row=0, column=1, padx=4, sticky="ew")
        ttk.Button(buttons_producto, text="Actualizar", command=self.actualizar_producto).grid(row=0, column=2, padx=4, sticky="ew")
        ttk.Button(buttons_producto, text="Eliminar", command=self.eliminar_producto).grid(row=0, column=3, padx=4, sticky="ew")
        ttk.Button(buttons_producto, text="Limpiar", command=self.limpiar_formulario).grid(row=0, column=4, padx=4, sticky="ew")

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
        vprod = ttk.Scrollbar(self.productos_frame, orient="vertical", command=self.productos_tree.yview)
        self.productos_tree.configure(yscrollcommand=vprod.set)
        self.productos_tree.grid(row=4, column=0, sticky="nsew")
        vprod.grid(row=4, column=1, sticky="ns", padx=(4, 0))
        self.productos_frame.columnconfigure(0, weight=1)
        self.productos_frame.columnconfigure(1, weight=0)

        self.ventas_frame = ttk.Frame(content, padding=10)
        self.ventas_frame.grid(row=0, column=0, sticky="nsew")
        self.ventas_frame.columnconfigure(0, weight=1)
        self.ventas_frame.rowconfigure(2, weight=1)

        ttk.Label(self.ventas_frame, text="Registro de ventas", font=("Segoe UI", 12, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 12))

        ventas_form = ttk.Frame(self.ventas_frame)
        ventas_form.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        ventas_form.columnconfigure(1, weight=1)

        ttk.Label(ventas_form, text="Usuario:").grid(row=0, column=0, sticky="e", padx=(0, 8), pady=4)
        self.usuario_var = tk.StringVar()
        self.usuario_combo = ttk.Combobox(ventas_form, textvariable=self.usuario_var, state="readonly")
        self.usuario_combo.grid(row=0, column=1, sticky="w", pady=4)

        ttk.Label(ventas_form, text="Producto (ID):").grid(row=1, column=0, sticky="e", padx=(0, 8), pady=4)
        self.producto_var = tk.StringVar()
        self.producto_combo = ttk.Combobox(ventas_form, textvariable=self.producto_var, state="readonly")
        self.producto_combo.grid(row=1, column=1, sticky="w", pady=4)

        ttk.Label(ventas_form, text="Cantidad:").grid(row=2, column=0, sticky="e", padx=(0, 8), pady=4)
        self.cantidad_venta_var = tk.StringVar(value="1")
        self.cantidad_venta_entry = ttk.Entry(ventas_form, textvariable=self.cantidad_venta_var, width=8)
        self.cantidad_venta_entry.grid(row=2, column=1, sticky="w", pady=4)

        ventas_btn_frame = ttk.Frame(self.ventas_frame)
        ventas_btn_frame.grid(row=2, column=0, sticky="ew", pady=(0, 10))
        ventas_btn_frame.columnconfigure(0, weight=1)

        ttk.Button(ventas_btn_frame, text="Registrar venta", command=self.registrar_venta).grid(row=0, column=0, padx=4, sticky="ew")

        self.mensaje_ventas = ttk.Label(self.ventas_frame, text="", foreground="darkgreen")
        self.mensaje_ventas.grid(row=3, column=0, sticky="w", pady=(0, 8))

        self.ventas_tree = ttk.Treeview(self.ventas_frame, columns=("id", "usuario", "producto", "cantidad", "fecha"), show="headings", height=12)
        self.ventas_tree.heading("id", text="ID")
        self.ventas_tree.heading("usuario", text="Usuario")
        self.ventas_tree.heading("producto", text="Producto ID")
        self.ventas_tree.heading("cantidad", text="Cantidad")
        self.ventas_tree.heading("fecha", text="Fecha")
        self.ventas_tree.column("id", width=60, anchor="center")
        self.ventas_tree.column("usuario", width=140, anchor="center")
        self.ventas_tree.column("producto", width=100, anchor="center")
        self.ventas_tree.column("cantidad", width=90, anchor="center")
        self.ventas_tree.column("fecha", width=200, anchor="center")
        vventas = ttk.Scrollbar(self.ventas_frame, orient="vertical", command=self.ventas_tree.yview)
        self.ventas_tree.configure(yscrollcommand=vventas.set)
        self.ventas_tree.grid(row=4, column=0, sticky="nsew")
        vventas.grid(row=4, column=1, sticky="ns", padx=(4, 0))
        self.ventas_frame.columnconfigure(0, weight=1)
        self.ventas_frame.columnconfigure(1, weight=0)

        self._configurar_permisos()

    def mostrar_usuarios(self):
        if not self._es_administrador():
            self.usuarios_frame.grid(row=0, column=0, sticky="nsew")
            self.mensaje_usuarios.config(text="Acceso restringido: solo el administrador puede gestionar usuarios.", foreground="darkred")
            self.productos_frame.grid_forget()
            self.ventas_frame.grid_forget()
            return

        self.productos_frame.grid_forget()
        self.ventas_frame.grid_forget()
        self.usuarios_frame.grid(row=0, column=0, sticky="nsew")
        self.actualizar_tabla_usuarios()

    def mostrar_productos(self):
        self.usuarios_frame.grid_forget()
        self.ventas_frame.grid_forget()
        self.productos_frame.grid(row=0, column=0, sticky="nsew")
        self.actualizar_tabla_productos()

    def mostrar_ventas(self):
        self.productos_frame.grid_forget()
        self.usuarios_frame.grid_forget()
        self.ventas_frame.grid(row=0, column=0, sticky="nsew")

        usuarios = [u.username for u in self.servicio.listar_usuarios()]
        productos = [str(p.id) for p in self.servicio.listar_productos()]
        self.usuario_combo["values"] = usuarios
        self.producto_combo["values"] = productos
        self.actualizar_tabla_ventas()

    def limpiar_formulario(self):
        self.id_var.set("")
        self.nombre_var.set("")
        self.precio_var.set("")
        self.cantidad_var.set("")
        self.mensaje.config(text="")
        self.entry_id.focus_set()

    def _on_escape_usuario(self, event=None):
        self.limpiar_formulario_usuario(event)

    def _on_return_usuario(self, event=None):
        self.registrar_usuario()

    def _on_role_selected(self, event=None):
        self.mensaje_usuarios.config(text=f"Rol seleccionado: {self.usuario_rol_var.get()}", foreground="darkblue")

    def _on_usuario_seleccionado(self, event=None):
        seleccion = self.usuarios_tree.selection()
        if not seleccion:
            return

        item = self.usuarios_tree.item(seleccion[0], "values")
        if not item:
            return

        usuario_id = int(item[0])
        usuario = self.servicio.obtener_usuario_por_id(usuario_id)
        if not usuario:
            return

        self.usuario_id_var.set(str(usuario.id))
        self.usuario_nombre_var.set(usuario.nombre)
        self.usuario_username_var.set(usuario.username)
        self.usuario_password_var.set(usuario.password)
        self.usuario_rol_var.set(usuario.rol)
        self.mensaje_usuarios.config(text=f"Usuario {usuario.username} cargado en el formulario.", foreground="darkgreen")

    def limpiar_formulario_usuario(self, event=None):
        self.usuario_id_var.set("")
        self.usuario_nombre_var.set("")
        self.usuario_username_var.set("")
        self.usuario_password_var.set("")
        self.usuario_rol_var.set("Cliente")
        self.mensaje_usuarios.config(text="Formulario limpiado.", foreground="darkgreen")
        self.usuarios_tree.selection_remove(*self.usuarios_tree.selection())
        self.entry_usuario_nombre.focus_set()

    def actualizar_tabla_usuarios(self):
        self.usuarios_tree.delete(*self.usuarios_tree.get_children())
        for usuario in self.servicio.listar_usuarios():
            self.usuarios_tree.insert("", tk.END, values=(usuario.id, usuario.nombre, usuario.username, usuario.rol))

    def _obtener_datos_formulario_usuario(self):
        nombre = self.usuario_nombre_var.get().strip()
        username = self.usuario_username_var.get().strip()
        password = self.usuario_password_var.get().strip()
        rol = self.usuario_rol_var.get().strip() or "Cliente"

        id_str = self.usuario_id_var.get().strip()
        usuario_id = None
        if id_str:
            try:
                usuario_id = int(id_str)
            except ValueError:
                return None, "El ID debe ser un número entero."

        if not nombre:
            return None, "El nombre es obligatorio."
        if not username:
            return None, "El nombre de usuario es obligatorio."
        if not password:
            return None, "La contraseña es obligatoria."
        if rol not in {"Administrador", "Empleado", "Cliente"}:
            return None, "Seleccione un rol válido."

        return {"id": usuario_id, "nombre": nombre, "username": username, "password": password, "rol": rol}, ""

    def registrar_usuario(self):
        if not self._es_administrador():
            self.mensaje_usuarios.config(text="Solo el administrador puede registrar usuarios.", foreground="darkred")
            return

        datos, error = self._obtener_datos_formulario_usuario()
        if error:
            self.mensaje_usuarios.config(text=error, foreground="darkred")
            return

        if datos["id"] is not None and self.servicio.obtener_usuario_por_id(datos["id"]):
            self.actualizar_usuario()
            return

        usuario = Usuario(**datos)
        ok, mensaje = self.servicio.registrar_usuario(usuario)
        self.mensaje_usuarios.config(text=mensaje, foreground="darkgreen" if ok else "darkred")
        if ok:
            self.actualizar_tabla_usuarios()
            self.limpiar_formulario_usuario()

    def actualizar_usuario(self):
        if not self._es_administrador():
            self.mensaje_usuarios.config(text="Solo el administrador puede actualizar usuarios.", foreground="darkred")
            return

        datos, error = self._obtener_datos_formulario_usuario()
        if error:
            self.mensaje_usuarios.config(text=error, foreground="darkred")
            return

        usuario_id = datos["id"]
        if usuario_id is None:
            self.mensaje_usuarios.config(text="Seleccione un usuario para actualizar o registre uno nuevo.", foreground="darkred")
            return

        ok, mensaje = self.servicio.actualizar_usuario(
            usuario_id,
            datos["nombre"],
            datos["username"],
            datos["password"],
            datos["rol"],
        )
        self.mensaje_usuarios.config(text=mensaje, foreground="darkgreen" if ok else "darkred")
        if ok:
            self.actualizar_tabla_usuarios()
            self.limpiar_formulario_usuario()

    def eliminar_usuario(self):
        if not self._es_administrador():
            self.mensaje_usuarios.config(text="Solo el administrador puede eliminar usuarios.", foreground="darkred")
            return

        id_str = self.usuario_id_var.get().strip()
        if not id_str:
            self.mensaje_usuarios.config(text="Seleccione un usuario para eliminar.", foreground="darkred")
            return

        try:
            usuario_id = int(id_str)
        except ValueError:
            self.mensaje_usuarios.config(text="El ID del usuario es inválido.", foreground="darkred")
            return

        usuario = self.servicio.obtener_usuario_por_id(usuario_id)
        if not usuario:
            self.mensaje_usuarios.config(text="El usuario seleccionado no existe.", foreground="darkred")
            return

        usuario_actual = self.servicio.obtener_usuario(self.usuario_actual) if self.usuario_actual else None
        if usuario_actual and usuario_actual.id == usuario_id:
            self.mensaje_usuarios.config(text="No puedes eliminar la cuenta administrativa autenticada.", foreground="darkred")
            return

        confirmacion = messagebox.askyesno("Confirmación", f"¿Deseas eliminar al usuario '{usuario.username}'?")
        if not confirmacion:
            self.mensaje_usuarios.config(text="Eliminación cancelada.", foreground="darkblue")
            return

        ok, mensaje = self.servicio.eliminar_usuario(usuario_id)
        self.mensaje_usuarios.config(text=mensaje, foreground="darkgreen" if ok else "darkred")
        if ok:
            self.actualizar_tabla_usuarios()
            self.limpiar_formulario_usuario()

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

    def actualizar_tabla_ventas(self):
        self.ventas_tree.delete(*self.ventas_tree.get_children())
        for venta in self.servicio.listar_ventas():
            self.ventas_tree.insert("", tk.END, values=(venta.id, venta.username, venta.producto_id, venta.cantidad, venta.fecha))

    def registrar_venta(self):
        username = self.usuario_var.get().strip()
        producto_id_str = self.producto_var.get().strip()
        cantidad_str = self.cantidad_venta_var.get().strip()

        if not username:
            self.mensaje_ventas.config(text="Seleccione un usuario.", foreground="darkred")
            return
        if not producto_id_str:
            self.mensaje_ventas.config(text="Seleccione un producto.", foreground="darkred")
            return
        if not cantidad_str:
            self.mensaje_ventas.config(text="Ingrese una cantidad válida.", foreground="darkred")
            return
        try:
            producto_id = int(producto_id_str)
            cantidad = int(cantidad_str)
        except ValueError:
            self.mensaje_ventas.config(text="Producto o cantidad inválidos.", foreground="darkred")
            return

        ok, mensaje = self.servicio.registrar_venta(username, producto_id, cantidad)
        self.mensaje_ventas.config(text=mensaje, foreground="darkgreen" if ok else "darkred")
        if ok:
            self.actualizar_tabla_ventas()
            self.usuario_var.set("")
            self.producto_var.set("")
            self.cantidad_venta_var.set("1")
