from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto
from modelos.usuario import Usuario

class RestauranteServicio:
    def __init__(self, archivo_servicio: ArchivoServicio):
        self.archivo = archivo_servicio
        self._usuarios = []
        self._productos = []
        self.cargar_datos()

    def cargar_datos(self):
        usuarios = self.archivo.leer("usuarios.json")
        productos = self.archivo.leer("productos.json")
        self._usuarios = [Usuario(**u) for u in usuarios]
        self._productos = [Producto(**p) for p in productos]

    def validar_usuario(self, username: str, password: str) -> bool:
        for u in self._usuarios:
            if u.username == username and u.password == password:
                return True
        return False

    def listar_usuarios(self):
        return list(self._usuarios)

    def listar_productos(self):
        return list(self._productos)

    def obtener_cantidad_producto(self, producto_id: int) -> int:
        for p in self._productos:
            if p.id == producto_id:
                return p.cantidad
        return 0
