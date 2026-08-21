"""
Módulo de servicio del restaurante.
Administra la lógica de negocio para productos y usuarios.
Coordina con el servicio de archivo para persistencia.
"""

from typing import List, Optional
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:
    """
    Servicio principal que administra las colecciones y operaciones del restaurante.
    Responsable de registrar, buscar, actualizar, eliminar y listar productos y usuarios.

    Attributes:
        productos (List[Producto]): Lista de productos registrados.
        usuarios (List[Usuario]): Lista de usuarios registrados (sin persistencia en esta semana).
        archivo_servicio (ArchivoServicio): Gestor de persistencia JSON.
    """

    def __init__(self) -> None:
        """
        Inicializa una instancia del servicio Restaurante.
        Crea las colecciones vacías y el gestor de archivos.
        """
        self.productos: List[Producto] = []
        self.usuarios: List[Usuario] = []
        self.archivo_servicio = ArchivoServicio()

    # ==================== Métodos de Producto ====================

    def registrar_producto(self, producto: Producto) -> bool:
        """
        Registra un nuevo producto en la colección del restaurante.
        Valida que no exista un producto con el mismo código.
        Guarda automáticamente en JSON después del registro exitoso.

        Args:
            producto (Producto): Instancia de Producto a registrar.

        Returns:
            bool: True si el registro fue exitoso, False si el código ya existe.
        """
        if self._codigo_producto_existe(producto.codigo):
            return False

        self.productos.append(producto)
        self.archivo_servicio.guardar_productos(self.productos)
        return True

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        """
        Busca un producto por su código único.

        Args:
            codigo (str): Código del producto a buscar.

        Returns:
            Optional[Producto]: El producto encontrado, o None si no existe.
        """
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(self, codigo: str, nuevo_nombre: str = None,
                           nueva_categoria: str = None, nuevo_precio: float = None) -> bool:
        """
        Actualiza los datos de un producto existente.
        Guarda automáticamente en JSON después de la actualización exitosa.

        Args:
            codigo (str): Código del producto a actualizar.
            nuevo_nombre (str, optional): Nuevo nombre del producto.
            nueva_categoria (str, optional): Nueva categoría del producto.
            nuevo_precio (float, optional): Nuevo precio del producto.

        Returns:
            bool: True si la actualización fue exitosa, False si el producto no existe.

        Raises:
            ValueError: Si el nuevo precio es negativo.
        """
        producto = self.buscar_producto_por_codigo(codigo)
        if not producto:
            return False

        # Validar nuevo precio si se proporciona
        if nuevo_precio is not None:
            if nuevo_precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            producto.precio = nuevo_precio

        # Actualizar otros atributos si se proporcionan
        if nuevo_nombre is not None:
            producto.nombre = nuevo_nombre
        if nueva_categoria is not None:
            producto.categoria = nueva_categoria

        self.archivo_servicio.guardar_productos(self.productos)
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """
        Elimina un producto de la colección del restaurante.
        Guarda automáticamente en JSON después de la eliminación exitosa.

        Args:
            codigo (str): Código del producto a eliminar.

        Returns:
            bool: True si la eliminación fue exitosa, False si el producto no existe.
        """
        producto = self.buscar_producto_por_codigo(codigo)
        if not producto:
            return False

        self.productos.remove(producto)
        self.archivo_servicio.guardar_productos(self.productos)
        return True

    def listar_productos(self) -> List[str]:
        """
        Retorna la información formateada de todos los productos registrados.

        Returns:
            List[str]: Lista de cadenas con la información de cada producto.
        """
        return [producto.mostrar_informacion() for producto in self.productos]

    def _codigo_producto_existe(self, codigo: str) -> bool:
        """
        Valida si ya existe un producto con el código especificado.

        Args:
            codigo (str): Código a verificar.

        Returns:
            bool: True si existe, False en caso contrario.
        """
        return any(producto.codigo == codigo for producto in self.productos)

    def obtener_cantidad_productos(self) -> int:
        """
        Retorna la cantidad total de productos registrados.

        Returns:
            int: Cantidad de productos.
        """
        return len(self.productos)

    # ==================== Métodos de Usuario ====================

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """
        Registra un nuevo usuario en la colección del restaurante.
        Los usuarios se mantienen únicamente en memoria durante esta semana.
        Valida que no exista un usuario con la misma identificación.

        Args:
            usuario (Usuario): Instancia de Usuario a registrar.

        Returns:
            bool: True si el registro fue exitoso, False si la identificación ya existe.
        """
        if self._identificacion_usuario_existe(usuario.identificacion):
            return False

        self.usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> List[str]:
        """
        Retorna la información formateada de todos los usuarios registrados.

        Returns:
            List[str]: Lista de cadenas con la información de cada usuario.
        """
        return [usuario.mostrar_informacion() for usuario in self.usuarios]

    def _identificacion_usuario_existe(self, identificacion: str) -> bool:
        """
        Valida si ya existe un usuario con la identificación especificada.

        Args:
            identificacion (str): Identificación a verificar.

        Returns:
            bool: True si existe, False en caso contrario.
        """
        return any(usuario.identificacion == identificacion for usuario in self.usuarios)

    def obtener_cantidad_usuarios(self) -> int:
        """
        Retorna la cantidad total de usuarios registrados.

        Returns:
            int: Cantidad de usuarios.
        """
        return len(self.usuarios)

    # ==================== Métodos de Persistencia ====================

    def cargar_productos_desde_archivo(self) -> bool:
        """
        Carga los productos almacenados en el archivo JSON.
        Reemplaza la colección actual de productos.

        Returns:
            bool: True si la carga fue exitosa, False en caso contrario.
        """
        try:
            self.productos = self.archivo_servicio.cargar_productos()
            return True
        except Exception as error:
            print(f"Error al cargar productos desde archivo: {error}")
            return False

    def guardar_productos_a_archivo(self) -> bool:
        """
        Guarda los productos actuales en el archivo JSON.

        Returns:
            bool: True si el guardado fue exitoso, False en caso contrario.
        """
        try:
            return self.archivo_servicio.guardar_productos(self.productos)
        except Exception as error:
            print(f"Error al guardar productos en archivo: {error}")
            return False

