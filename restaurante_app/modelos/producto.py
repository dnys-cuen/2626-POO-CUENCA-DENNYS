"""
Módulo que define la clase Producto.
Los productos representan los platos y bebidas disponibles en el restaurante.
"""


class Producto:
    """
    Clase que representa un producto disponible en el restaurante.

    Atributos:
        id (int): identificador único del producto
        nombre (str): nombre del producto
        categoria (str): categoría del producto (plato fuerte, bebida, postre, etc.)
        precio (float): precio del producto en dinero
        disponible (bool): indica si el producto está disponible
    """

    def __init__(self, id, nombre, categoria, precio):
        """
        Constructor de la clase Producto.

        Args:
            id (int): identificador único del producto
            nombre (str): nombre del producto
            categoria (str): categoría del producto
            precio (float): precio del producto
        """
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = True  # Por defecto, los productos están disponibles

    def obtener_precio_formateado(self):
        """Retorna el precio formateado con 2 decimales."""
        return f"${self.precio:.2f}"

    def cambiar_disponibilidad(self, disponible):
        """Cambia el estado de disponibilidad del producto."""
        self.disponible = disponible

    def __str__(self):
        """Retorna una representación en texto del producto."""
        estado = "Disponible" if self.disponible else "No disponible"
        return f"[{self.id}] {self.nombre} ({self.categoria}) - {self.obtener_precio_formateado()} - {estado}"

