"""
Modelo Cliente
Utiliza @dataclass para representar clientes del restaurante.
"""

from dataclasses import dataclass


@dataclass
class Cliente:
    """Representa un cliente del restaurante.

    Atributos:
        nombre: str - nombre completo del cliente
        correo: str - correo electrónico
        id_cliente: str - identificador único (puede ser número o texto)
    """

    nombre: str
    correo: str
    id_cliente: str

    def __repr__(self) -> str:
        return f"Cliente(id={self.id_cliente!r}, nombre={self.nombre!r}, correo={self.correo!r})"

