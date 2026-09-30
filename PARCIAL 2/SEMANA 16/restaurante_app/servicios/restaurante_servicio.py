from datetime import datetime

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class RestauranteServicio:
    def __init__(self, archivo_servicio):
        self.archivo = archivo_servicio
        self._usuarios = []
        self._productos = []
        self._ventas = []
        self.cargar_datos()

    def cargar_datos(self):
        usuarios = self.archivo.leer("usuarios.json")
        productos = self.archivo.leer("productos.json")
        ventas = self.archivo.leer("ventas.json")

        datos_usuarios = []
        for index, usuario in enumerate(usuarios, start=1):
            data = dict(usuario)
            data.setdefault("id", index)
            data.setdefault("rol", "Cliente")
            if not data.get("nombre"):
                data["nombre"] = data.get("username", "")
            datos_usuarios.append(data)
        self._usuarios = [Usuario(**u) for u in datos_usuarios]

        self._productos = [Producto(**p) for p in productos]
        self._ventas = [Venta(**v) for v in ventas]

    def _siguiente_id_usuario(self):
        if not self._usuarios:
            return 1
        return max((usuario.id or 0) for usuario in self._usuarios) + 1

    def validar_usuario(self, username: str, password: str) -> bool:
        for usuario in self._usuarios:
            if usuario.username == username and usuario.password == password:
                return True
        return False

    def listar_usuarios(self):
        return sorted(self._usuarios, key=lambda u: (u.id is None, u.id or 0))

    def listar_productos(self):
        return list(self._productos)

    def listar_ventas(self):
        return list(self._ventas)

    def obtener_producto(self, producto_id: int):
        for producto in self._productos:
            if producto.id == producto_id:
                return producto
        return None

    def obtener_usuario(self, username: str):
        for usuario in self._usuarios:
            if usuario.username == username:
                return usuario
        return None

    def obtener_usuario_por_id(self, usuario_id: int):
        for usuario in self._usuarios:
            if usuario.id == usuario_id:
                return usuario
        return None

    def guardar_usuarios(self):
        datos = [
            {
                "id": u.id,
                "username": u.username,
                "password": u.password,
                "nombre": u.nombre,
                "rol": u.rol,
            }
            for u in self._usuarios
        ]
        self.archivo.guardar("usuarios.json", datos)

    def registrar_usuario(self, usuario: Usuario):
        username = (usuario.username or "").strip()
        password = (usuario.password or "").strip()
        nombre = (usuario.nombre or "").strip()
        rol = (usuario.rol or "Cliente").strip()

        if not username:
            return False, "El nombre de usuario es obligatorio."
        if not password:
            return False, "La contraseña es obligatoria."
        if len(password) < 4:
            return False, "La contraseña debe tener al menos 4 caracteres."
        if not nombre:
            return False, "El nombre completo es obligatorio."
        if rol not in {"Administrador", "Empleado", "Cliente"}:
            return False, "El rol seleccionado no es válido."
        if self.obtener_usuario(username):
            return False, f"El usuario '{username}' ya existe."

        usuario.username = username
        usuario.password = password
        usuario.nombre = nombre
        usuario.rol = rol
        usuario.id = usuario.id if usuario.id is not None and usuario.id > 0 else self._siguiente_id_usuario()

        self._usuarios.append(usuario)
        self.guardar_usuarios()
        return True, "Usuario registrado correctamente."

    def actualizar_usuario(self, usuario_id: int, nombre: str, username: str, password: str, rol: str):
        usuario = self.obtener_usuario_por_id(usuario_id)
        if not usuario:
            return False, "El usuario no existe."

        nuevo_nombre = (nombre or "").strip()
        nuevo_username = (username or "").strip()
        nueva_password = (password or "").strip()
        nuevo_rol = (rol or "Cliente").strip()

        if not nuevo_nombre:
            return False, "El nombre completo es obligatorio."
        if not nuevo_username:
            return False, "El nombre de usuario es obligatorio."
        if len(nueva_password) < 4:
            return False, "La contraseña debe tener al menos 4 caracteres."
        if nuevo_rol not in {"Administrador", "Empleado", "Cliente"}:
            return False, "El rol seleccionado no es válido."

        usuario_encontrado = self.obtener_usuario(nuevo_username)
        if usuario_encontrado and usuario_encontrado.id != usuario_id:
            return False, f"El usuario '{nuevo_username}' ya existe."

        usuario.nombre = nuevo_nombre
        usuario.username = nuevo_username
        usuario.password = nueva_password
        usuario.rol = nuevo_rol
        self.guardar_usuarios()
        return True, "Usuario actualizado correctamente."

    def eliminar_usuario(self, usuario_id: int):
        usuario = self.obtener_usuario_por_id(usuario_id)
        if not usuario:
            return False, "El usuario no existe."

        self._usuarios = [u for u in self._usuarios if u.id != usuario_id]
        self.guardar_usuarios()
        return True, "Usuario eliminado correctamente."

    def guardar_productos(self):
        datos = [
            {
                "id": p.id,
                "nombre": p.nombre,
                "precio": p.precio,
                "cantidad": p.cantidad,
            }
            for p in self._productos
        ]
        self.archivo.guardar("productos.json", datos)

    def guardar_ventas(self):
        datos = [
            {
                "id": v.id,
                "username": v.username,
                "producto_id": v.producto_id,
                "fecha": v.fecha,
                "cantidad": v.cantidad,
            }
            for v in self._ventas
        ]
        self.archivo.guardar("ventas.json", datos)

    def registrar_venta(self, username: str, producto_id: int, cantidad: int = 1):
        usuario = self.obtener_usuario(username)
        if not usuario:
            return False, "Usuario no encontrado."

        producto = self.obtener_producto(producto_id)
        if not producto:
            return False, "Producto no encontrado."

        try:
            cantidad = int(cantidad)
        except (TypeError, ValueError):
            return False, "La cantidad debe ser un número entero."

        if cantidad <= 0:
            return False, "La cantidad debe ser mayor a cero."
        if cantidad > producto.cantidad:
            return False, f"No hay stock suficiente. Disponible: {producto.cantidad}."

        if self._ventas:
            next_id = max(v.id for v in self._ventas) + 1
        else:
            next_id = 1

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        producto.cantidad -= cantidad
        venta = Venta(id=next_id, username=usuario.username, producto_id=producto.id, fecha=fecha, cantidad=cantidad)
        self._ventas.append(venta)
        self.guardar_productos()
        self.guardar_ventas()
        return True, "Venta registrada correctamente."
