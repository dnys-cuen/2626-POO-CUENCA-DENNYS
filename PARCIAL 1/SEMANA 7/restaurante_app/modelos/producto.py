"""
Modelo Producto
Implementa constructor tradicional, propiedades y validaciones básicas.
"""

from typing import Any


class Producto:
    """Representa un producto del restaurante.

    Atributos protegidos (encapsulados): _nombre, _categoria, _precio, _disponible
    Se ofrecen @property y @setter para controlar acceso y validaciones.
    """

    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True) -> None:
        # Validaciones iniciales a través de los setters
        self._nombre = None
        self._categoria = None
        self._precio = None
        self._disponible = None

        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    # Nombre
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    # Categoría
    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = valor.strip()

    # Precio
    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: Any) -> None:
        try:
            precio_f = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número mayor que cero.")
        if precio_f <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = precio_f

    # Disponible
    @property
    def disponible(self) -> bool:
        return bool(self._disponible)

    @disponible.setter
    def disponible(self, valor: Any) -> None:
        # Permitir valores que puedan interpretarse como booleanos
        if isinstance(valor, str):
            v = valor.strip().lower()
            if v in ("true", "1", "si", "sí", "s", "y"):
                self._disponible = True
            elif v in ("false", "0", "n", "no"):
                self._disponible = False
            else:
                raise ValueError("Valor de disponible no reconocido (use True/False).")
        else:
            self._disponible = bool(valor)

    def mostrar_informacion(self) -> str:
        """Retorna una representación legible del producto."""
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Nombre: {self.nombre} | Categoría: {self.categoria} | Precio: S/ {self.precio:.2f} | {estado}"

    def __repr__(self) -> str:
        return f"Producto(nombre={self.nombre!r}, categoria={self.categoria!r}, precio={self.precio!r}, disponible={self.disponible!r})"

