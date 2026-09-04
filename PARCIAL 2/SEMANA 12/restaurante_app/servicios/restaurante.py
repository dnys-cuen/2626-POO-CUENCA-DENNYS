"""
Módulo de servicio del restaurante.
Administra la lógica de negocio para productos, usuarios y ventas.
Coordina con el servicio de archivo para persistencia.
"""

from typing import List, Optional, Dict
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:
    """
    Servicio principal que administra las colecciones y operaciones del restaurante.
    Responsable de registrar, buscar, actualizar, eliminar, listar productos y usuarios.
    Además, administra las ventas que relacionan usuarios con productos.

    Utiliza índices en diccionarios para optimizar búsquedas frecuentes por clave única:
    - Índice de productos por código (dict)
    - Índice de usuarios por identificación (dict)
    - Índice de ventas por usuario (dict con listas de ventas por usuario_id)

    Attributes:
        productos (List[Producto]): Lista principal de productos registrados.
        usuarios (List[Usuario]): Lista principal de usuarios registrados.
        ventas (List[Venta]): Lista principal de ventas realizadas.
        indice_productos (Dict): Índice de productos por código para búsquedas O(1).
        indice_usuarios (Dict): Índice de usuarios por identificación para búsquedas O(1).
        indice_ventas_usuario (Dict): Índice de ventas agrupadas por usuario_id.
        archivo_servicio (ArchivoServicio): Gestor de persistencia JSON.
    """

    def __init__(self) -> None:
        """
        Inicializa una instancia del servicio Restaurante.
        Crea las colecciones vacías, los índices y el gestor de archivos.
        """
        self.productos: List[Producto] = []
        self.usuarios: List[Usuario] = []
        self.ventas: List[Venta] = []

        # Índices para búsquedas optimizadas
        self.indice_productos: Dict[str, Producto] = {}  # {codigo: Producto}
        self.indice_usuarios: Dict[str, Usuario] = {}  # {identificacion: Usuario}
        self.indice_ventas_usuario: Dict[str, List[Venta]] = {}  # {usuario_id: [Venta]}

        self.archivo_servicio = ArchivoServicio()

    # ==================== Métodos de Producto ====================

    def registrar_producto(self, producto: Producto) -> bool:
        """
        Registra un nuevo producto en la colección del restaurante.
        Valida que no exista un producto con el mismo código.
        Actualiza el índice de productos.
        Guarda automáticamente en JSON después del registro exitoso.

        Args:
            producto (Producto): Instancia de Producto a registrar.

        Returns:
            bool: True si el registro fue exitoso, False si el código ya existe.
        """
        if self._codigo_producto_existe(producto.codigo):
            return False

        self.productos.append(producto)
        self.indice_productos[producto.codigo] = producto  # Actualizar índice
        self.archivo_servicio.guardar_productos(self.productos)
        return True

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        """
        Busca un producto por su código único.
        Utiliza el índice de productos para búsqueda O(1).

        Args:
            codigo (str): Código del producto a buscar.

        Returns:
            Optional[Producto]: El producto encontrado, o None si no existe.
        """
        return self.indice_productos.get(codigo)

    def actualizar_producto(self, codigo: str, nuevo_nombre: str = None,
                           nueva_categoria: str = None, nuevo_precio: float = None,
                           nuevo_stock: int = None) -> bool:
        """
        Actualiza los datos de un producto existente.
        Guarda automáticamente en JSON después de la actualización exitosa.

        Args:
            codigo (str): Código del producto a actualizar.
            nuevo_nombre (str, optional): Nuevo nombre del producto.
            nueva_categoria (str, optional): Nueva categoría del producto.
            nuevo_precio (float, optional): Nuevo precio del producto.
            nuevo_stock (int, optional): Nuevo stock del producto.

        Returns:
            bool: True si la actualización fue exitosa, False si el producto no existe.

        Raises:
            ValueError: Si los nuevos valores son inválidos.
        """
        producto = self.buscar_producto_por_codigo(codigo)
        if not producto:
            return False

        if nuevo_precio is not None:
            if nuevo_precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            producto.precio = nuevo_precio

        if nuevo_stock is not None:
            if nuevo_stock < 0:
                raise ValueError("El stock no puede ser negativo.")
            producto.stock = nuevo_stock

        if nuevo_nombre is not None:
            producto.nombre = nuevo_nombre
        if nueva_categoria is not None:
            producto.categoria = nueva_categoria

        self.archivo_servicio.guardar_productos(self.productos)
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """
        Elimina un producto de la colección del restaurante.
        Actualiza el índice de productos.
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
        del self.indice_productos[codigo]  # Eliminar del índice
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
        Utiliza el índice para verificación O(1).

        Args:
            codigo (str): Código a verificar.

        Returns:
            bool: True si existe, False en caso contrario.
        """
        return codigo in self.indice_productos

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
        Valida que no exista un usuario con la misma identificación.
        Actualiza el índice de usuarios.
        Guarda automáticamente en JSON después del registro exitoso.

        Args:
            usuario (Usuario): Instancia de Usuario a registrar.

        Returns:
            bool: True si el registro fue exitoso, False si la identificación ya existe.
        """
        if self._identificacion_usuario_existe(usuario.identificacion):
            return False

        self.usuarios.append(usuario)
        self.indice_usuarios[usuario.identificacion] = usuario  # Actualizar índice
        self.archivo_servicio.guardar_usuarios(self.usuarios)
        return True

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        """
        Busca un usuario por su identificación única.
        Utiliza el índice de usuarios para búsqueda O(1).

        Args:
            identificacion (str): Identificación del usuario a buscar.

        Returns:
            Optional[Usuario]: El usuario encontrado, o None si no existe.
        """
        return self.indice_usuarios.get(identificacion)

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
        Utiliza el índice para verificación O(1).

        Args:
            identificacion (str): Identificación a verificar.

        Returns:
            bool: True si existe, False en caso contrario.
        """
        return identificacion in self.indice_usuarios

    def obtener_cantidad_usuarios(self) -> int:
        """
        Retorna la cantidad total de usuarios registrados.

        Returns:
            int: Cantidad de usuarios.
        """
        return len(self.usuarios)

    # ==================== Métodos de Venta ====================

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        """
        Registra una venta de un producto a un usuario.
        Valida que el usuario y producto existan, que haya stock suficiente,
        y que la cantidad sea válida.
        Actualiza el índice de ventas por usuario.
        Guarda automáticamente productos y ventas en JSON después de una venta exitosa.

        Args:
            codigo_producto (str): Código del producto a vender.
            identificacion_usuario (str): Identificación del usuario que compra.
            cantidad (int): Cantidad a vender.

        Returns:
            bool: True si la venta fue exitosa, False en caso contrario.

        Raises:
            ValueError: Si la cantidad es inválida.
        """
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto_por_codigo(codigo_producto)

        # Validar que usuario y producto existan
        if usuario is None or producto is None:
            return False

        # Validar cantidad
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        # Validar stock
        if producto.stock < cantidad:
            return False

        # Crear la venta
        venta = Venta(usuario.identificacion, producto.codigo, cantidad)

        # Agregar venta a la colección
        self.ventas.append(venta)

        # Actualizar índice de ventas por usuario
        if identificacion_usuario not in self.indice_ventas_usuario:
            self.indice_ventas_usuario[identificacion_usuario] = []
        self.indice_ventas_usuario[identificacion_usuario].append(venta)

        # Disminuir stock del producto
        producto.stock -= cantidad

        # Guardar en JSON
        self.archivo_servicio.guardar_ventas(self.ventas)
        self.archivo_servicio.guardar_productos(self.productos)

        return True

    def obtener_ventas_usuario(self, identificacion_usuario: str) -> List[Venta]:
        """
        Obtiene todas las ventas realizadas por un usuario específico.
        Utiliza el índice de ventas por usuario para búsqueda O(1).

        Args:
            identificacion_usuario (str): Identificación del usuario.

        Returns:
            List[Venta]: Lista de ventas del usuario, lista vacía si el usuario no tiene ventas.
        """
        return self.indice_ventas_usuario.get(identificacion_usuario, [])

    def listar_ventas(self) -> List[str]:
        """
        Retorna la información formateada de todas las ventas registradas.

        Returns:
            List[str]: Lista de cadenas con la información de cada venta.
        """
        return [venta.mostrar_informacion() for venta in self.ventas]

    def obtener_cantidad_ventas(self) -> int:
        """
        Retorna la cantidad total de ventas registradas.

        Returns:
            int: Cantidad de ventas.
        """
        return len(self.ventas)

    # ==================== Métodos de Persistencia ====================

    def cargar_datos_desde_archivo(self) -> bool:
        """
        Carga productos, usuarios y ventas desde los archivos JSON.
        Reemplaza las colecciones actuales y reconstruye los índices en memoria.

        Returns:
            bool: True si la carga fue exitosa, False en caso contrario.
        """
        try:
            self.productos = self.archivo_servicio.cargar_productos()
            self.usuarios = self.archivo_servicio.cargar_usuarios()
            self.ventas = self.archivo_servicio.cargar_ventas()

            # Reconstruir índices
            self._reconstruir_indices()

            return True
        except Exception as error:
            print(f"Error al cargar datos desde archivo: {error}")
            return False

    def _reconstruir_indices(self) -> None:
        """
        Reconstruye los índices en memoria a partir de las colecciones principales.
        Se ejecuta después de cargar datos desde JSON o en situaciones de sincronización.
        """
        # Reconstruir índice de productos
        self.indice_productos.clear()
        for producto in self.productos:
            self.indice_productos[producto.codigo] = producto

        # Reconstruir índice de usuarios
        self.indice_usuarios.clear()
        for usuario in self.usuarios:
            self.indice_usuarios[usuario.identificacion] = usuario

        # Reconstruir índice de ventas por usuario
        self.indice_ventas_usuario.clear()
        for venta in self.ventas:
            if venta.usuario_id not in self.indice_ventas_usuario:
                self.indice_ventas_usuario[venta.usuario_id] = []
            self.indice_ventas_usuario[venta.usuario_id].append(venta)

    def guardar_datos_a_archivo(self) -> bool:
        """
        Guarda productos, usuarios y ventas en los archivos JSON.

        Returns:
            bool: True si el guardado fue exitoso, False en caso contrario.
        """
        try:
            result = True
            result = self.archivo_servicio.guardar_productos(self.productos) and result
            result = self.archivo_servicio.guardar_usuarios(self.usuarios) and result
            result = self.archivo_servicio.guardar_ventas(self.ventas) and result
            return result
        except Exception as error:
            print(f"Error al guardar datos en archivo: {error}")
            return False

