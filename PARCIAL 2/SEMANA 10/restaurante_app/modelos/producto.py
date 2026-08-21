"""
Módulo de la clase Producto.
Representa un producto general del restaurante con responsabilidad única.
"""


class Producto:
    """
    Clase que representa un producto general del restaurante.

    Attributes:
        codigo (str): Código único del producto.
        nombre (str): Nombre descriptivo del producto.
        categoria (str): Categoría a la que pertenece el producto.
        precio (float): Precio del producto en unidades monetarias.
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        """
        Inicializa una instancia de la clase Producto.

        Args:
            codigo (str): Código único del producto.
            nombre (str): Nombre del producto.
            categoria (str): Categoría del producto.
            precio (float): Precio del producto.

        Raises:
            ValueError: Si el precio es negativo.
        """
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self) -> str:
        """
        Retorna la información del producto de manera formateada.

        Returns:
            str: Cadena con la información del producto.
        """
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f}"
        )

    def a_diccionario(self) -> dict:
        """
        Convierte el producto a un diccionario para serialización JSON.

        Returns:
            dict: Diccionario con los datos del producto.
        """
        return {
            "tipo": "Producto",
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }

