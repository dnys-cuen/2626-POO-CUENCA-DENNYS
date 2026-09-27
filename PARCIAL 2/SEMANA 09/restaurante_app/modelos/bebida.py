"""
Módulo de la clase Bebida.
Representa una bebida del restaurante, extendiendo la clase Producto mediante herencia.
Demuestra el principio de sustitución de Liskov.
"""

from modelos.producto import Producto


class Bebida(Producto):
    """
    Clase que representa una bebida del restaurante.
    Hereda de Producto e incorpora atributos específicos de bebidas.

    Attributes:
        codigo (str): Código único de la bebida.
        nombre (str): Nombre de la bebida.
        categoria (str): Categoría de la bebida.
        precio (float): Precio de la bebida.
        tamaño (str): Tamaño de la bebida (pequeño, mediano, grande).
        tipo_envase (str): Tipo de envase (vaso, botella, lata).
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamaño: str,
        tipo_envase: str
    ) -> None:
        """
        Inicializa una instancia de la clase Bebida.

        Args:
            codigo (str): Código único de la bebida.
            nombre (str): Nombre de la bebida.
            categoria (str): Categoría de la bebida.
            precio (float): Precio de la bebida.
            tamaño (str): Tamaño de la bebida.
            tipo_envase (str): Tipo de envase de la bebida.
        """
        super().__init__(codigo, nombre, categoria, precio)
        self.tamaño = tamaño
        self.tipo_envase = tipo_envase

    def mostrar_informacion(self) -> str:
        """
        Retorna la información de la bebida de manera formateada.
        Sobrescribe el método de la clase padre para incluir atributos específicos.

        Returns:
            str: Cadena con la información de la bebida.
        """
        información_base = super().mostrar_informacion()
        return (
            f"{información_base} | "
            f"Tamaño: {self.tamaño} | "
            f"Envase: {self.tipo_envase}"
        )

