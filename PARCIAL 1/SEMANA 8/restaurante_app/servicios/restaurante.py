"""
Módulo de servicios del restaurante.
Contiene la clase Restaurante que administra productos, bebidas y clientes.
"""

from typing import List
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase de servicio que administra las colecciones y operaciones del restaurante.
    Responsable de registrar, validar y listar productos y clientes.

    Attributes:
        productos (List[Producto]): Lista de productos (incluye bebidas por herencia).
        clientes (List[Cliente]): Lista de clientes registrados.
    """

    def __init__(self) -> None:
        """
        Inicializa una instancia del servicio Restaurante.
        Crea las colecciones vacías para productos y clientes.
        """
        self.productos: List[Producto] = []
        self.clientes: List[Cliente] = []

    def registrar_producto(self, producto: Producto) -> bool:
        """
        Registra un nuevo producto (puede ser Producto o Bebida por polimorfismo).
        Valida que no exista un producto con el mismo código.

        Args:
            producto (Producto): Instancia de Producto o Bebida a registrar.

        Returns:
            bool: True si el registro fue exitoso, False si el código ya existe.
        """
        if self._codigo_producto_existe(producto.codigo):
            return False

        self.productos.append(producto)
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        """
        Registra un nuevo cliente.
        Valida que no exista un cliente con la misma identificación.

        Args:
            cliente (Cliente): Instancia de Cliente a registrar.

        Returns:
            bool: True si el registro fue exitoso, False si la identificación ya existe.
        """
        if self._identificacion_cliente_existe(cliente.identificacion):
            return False

        self.clientes.append(cliente)
        return True

    def listar_productos(self) -> List[str]:
        """
        Retorna la información de todos los productos registrados.
        Utiliza polimorfismo para llamar al método mostrar_informacion()
        de cada producto (Producto o Bebida).

        Returns:
            List[str]: Lista de cadenas con la información de cada producto.
        """
        return [producto.mostrar_informacion() for producto in self.productos]

    def listar_clientes(self) -> List[str]:
        """
        Retorna la información de todos los clientes registrados.

        Returns:
            List[str]: Lista de cadenas con la información de cada cliente.
        """
        return [cliente.mostrar_informacion() for cliente in self.clientes]

    def _codigo_producto_existe(self, codigo: str) -> bool:
        """
        Valida si ya existe un producto con el código especificado.

        Args:
            codigo (str): Código a verificar.

        Returns:
            bool: True si existe, False en caso contrario.
        """
        return any(producto.codigo == codigo for producto in self.productos)

    def _identificacion_cliente_existe(self, identificacion: str) -> bool:
        """
        Valida si ya existe un cliente con la identificación especificada.

        Args:
            identificacion (str): Identificación a verificar.

        Returns:
            bool: True si existe, False en caso contrario.
        """
        return any(cliente.identificacion == identificacion for cliente in self.clientes)

    def obtener_cantidad_productos(self) -> int:
        """
        Retorna la cantidad total de productos registrados.

        Returns:
            int: Cantidad de productos.
        """
        return len(self.productos)

    def obtener_cantidad_clientes(self) -> int:
        """
        Retorna la cantidad total de clientes registrados.

        Returns:
            int: Cantidad de clientes.
        """
        return len(self.clientes)

