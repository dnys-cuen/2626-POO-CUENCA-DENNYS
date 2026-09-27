from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from datetime import datetime


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
        self._usuarios = [Usuario(**u) for u in usuarios]
        self._productos = [Producto(**p) for p in productos]
        self._ventas = [Venta(**v) for v in ventas]

    def validar_usuario(self, username: str, password: str) -> bool:
        for usuario in self._usuarios:
            if usuario.username == username and usuario.password == password:
                return True
        return False

    def listar_usuarios(self):
        return list(self._usuarios)

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

    def registrar_producto(self, producto: Producto):
        if not isinstance(producto.id, int) or producto.id <= 0:
            return False, "El ID del producto debe ser un número entero positivo."
        if not producto.nombre or not producto.nombre.strip():
            return False, "El nombre del producto es obligatorio."
        if producto.precio <= 0:
            return False, "El precio debe ser mayor a cero."
        if producto.cantidad < 0:
            return False, "La cantidad no puede ser negativa."
        if self.obtener_producto(producto.id):
            return False, f"El producto con ID {producto.id} ya existe."

        self._productos.append(producto)
        self.guardar_productos()
        return True, "Producto registrado correctamente."

    def actualizar_producto(self, producto_id: int, nombre: str, precio: float, cantidad: int):
        producto = self.obtener_producto(producto_id)
        if not producto:
            return False, "El producto no existe."
        if not nombre or not nombre.strip():
            return False, "El nombre del producto es obligatorio."
        if precio <= 0:
            return False, "El precio debe ser mayor a cero."
        if cantidad < 0:
            return False, "La cantidad no puede ser negativa."

        producto.nombre = nombre.strip()
        producto.precio = float(precio)
        producto.cantidad = int(cantidad)
        self.guardar_productos()
        return True, "Producto actualizado correctamente."

    def eliminar_producto(self, producto_id: int):
        producto = self.obtener_producto(producto_id)
        if not producto:
            return False, "El producto no existe."

        self._productos = [p for p in self._productos if p.id != producto_id]
        self.guardar_productos()
        return True, "Producto eliminado correctamente."

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
            {"id": v.id, "username": v.username, "producto_id": v.producto_id, "fecha": v.fecha}
            for v in self._ventas
        ]
        self.archivo.guardar("ventas.json", datos)

    def registrar_venta(self, username: str, producto_id: int):
        # Validaciones en el servicio
        usuario = self.obtener_usuario(username)
        if not usuario:
            return False, "Usuario no encontrado."

        producto = self.obtener_producto(producto_id)
        if not producto:
            return False, "Producto no encontrado."

        # Generar ID secuencial para la venta
        if self._ventas:
            next_id = max(v.id for v in self._ventas) + 1
        else:
            next_id = 1

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        venta = Venta(id=next_id, username=usuario.username, producto_id=producto.id, fecha=fecha)
        self._ventas.append(venta)
        self.guardar_ventas()
        return True, "Venta registrada correctamente."
