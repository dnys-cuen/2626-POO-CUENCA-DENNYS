"""
Módulo de la clase Venta.
Representa una venta que relaciona un usuario con un producto.
"""


class Venta:
    """
    Clase que representa una venta en el restaurante.
    Relaciona un usuario con un producto vendido.

    Attributes:
        usuario_id (str): Identificación del usuario que realiza la compra.
        producto_codigo (str): Código del producto vendido.
        cantidad (int): Cantidad vendida del producto.
    """

    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int) -> None:
        """
        Inicializa una instancia de la clase Venta.

        Args:
            usuario_id (str): Identificación del usuario.
            producto_codigo (str): Código del producto.
            cantidad (int): Cantidad vendida.

        Raises:
            ValueError: Si la cantidad es menor o igual a cero.
        """
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad

    def a_diccionario(self) -> dict:
        """
        Convierte la venta a un diccionario para serialización JSON.

        Returns:
            dict: Diccionario con los datos de la venta.
        """
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    def mostrar_informacion(self) -> str:
        """
        Retorna la información de la venta de manera formateada.

        Returns:
            str: Cadena con la información de la venta.
        """
        return (
            f"Usuario: {self.usuario_id} | "
            f"Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad}"
        )

