"""
Servicio Restaurante
Contiene la clase Restaurante que administra productos y clientes.
"""

from typing import List, Optional
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Servicio que administra listas de productos y clientes."""

    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    # Métodos para productos
    def registrar_producto(self, producto: Producto) -> None:
        """Registra un objeto Producto en la lista."""
        if not isinstance(producto, Producto):
            raise TypeError("Se debe registrar una instancia de Producto.")
        self._productos.append(producto)

    def listar_productos(self) -> List[Producto]:
        """Retorna la lista de productos registrados."""
        return list(self._productos)

    def buscar_producto_por_nombre(self, nombre: str) -> List[Producto]:
        """Busca productos cuyo nombre contenga la cadena (insensible a mayúsculas)."""
        nombre = (nombre or "").strip().lower()
        return [p for p in self._productos if nombre in p.nombre.lower()]

    # Métodos para clientes
    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra un objeto Cliente en la lista."""
        if not isinstance(cliente, Cliente):
            raise TypeError("Se debe registrar una instancia de Cliente.")
        # Evitar IDs duplicados
        if any(c.id_cliente == cliente.id_cliente for c in self._clientes):
            raise ValueError(f"Ya existe un cliente con id {cliente.id_cliente}.")
        self._clientes.append(cliente)

    def listar_clientes(self) -> List[Cliente]:
        return list(self._clientes)

    def buscar_cliente_por_id(self, id_cliente: str) -> Optional[Cliente]:
        id_cliente = (id_cliente or "").strip()
        for c in self._clientes:
            if c.id_cliente == id_cliente:
                return c
        return None

