"""
Módulo de la clase Producto.
Representa un producto del restaurante con stock.
"""


class Producto:
    """
    Clase que representa un producto del restaurante.
    Incluye información de stock disponible.

    Attributes:
        codigo (str): Código único del producto.
        nombre (str): Nombre descriptivo del producto.
        categoria (str): Categoría a la que pertenece el producto.
        precio (float): Precio del producto en unidades monetarias.
        stock (int): Cantidad disponible del producto.
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0) -> None:
        """
        Inicializa una instancia de la clase Producto.

        Args:
            codigo (str): Código único del producto.
            nombre (str): Nombre del producto.
            categoria (str): Categoría del producto.
            precio (float): Precio del producto.
            stock (int): Cantidad disponible (por defecto 0).

        Raises:
            ValueError: Si el precio es negativo o el stock es negativo.
        """
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int) -> bool:
        """
        Disminuye el stock del producto por una venta.

        Args:
            cantidad (int): Cantidad a vender.

        Returns:
            bool: True si la venta fue exitosa, False si no hay stock suficiente.

        Raises:
            ValueError: Si la cantidad es negativa o cero.
        """
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if self.stock < cantidad:
            return False

        self.stock -= cantidad
        return True

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
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )

    def a_diccionario(self) -> dict:
        """
        Convierte el producto a un diccionario para serialización JSON.

        Returns:
            dict: Diccionario con los datos del producto.
        """
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

