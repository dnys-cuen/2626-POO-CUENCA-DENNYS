"""
Módulo que define la clase Producto.
Representa un producto disponible en el restaurante (platos, bebidas, etc.)
"""


class Producto:
    """
    Clase que representa un producto del restaurante.
    
    Atributos:
        identificador_producto (int): Identificador único del producto
        nombre_producto (str): Nombre del producto
        descripcion_producto (str): Descripción breve del producto
        precio_producto (float): Precio en pesos colombianos
        disponible (bool): Indica si el producto está disponible
    """
    
    def __init__(
        self,
        identificador_producto: int,
        nombre_producto: str,
        descripcion_producto: str,
        precio_producto: float,
        disponible: bool
    ) -> None:
        """
        Inicializa un objeto Producto.
        
        Args:
            identificador_producto: ID único del producto
            nombre_producto: Nombre del producto
            descripcion_producto: Descripción del producto
            precio_producto: Precio del producto
            disponible: Estado de disponibilidad del producto
        """
        self.identificador_producto = identificador_producto
        self.nombre_producto = nombre_producto
        self.descripcion_producto = descripcion_producto
        self.precio_producto = precio_producto
        self.disponible = disponible
    
    def __str__(self) -> str:
        """Retorna una representación en texto del producto."""
        estado = "Disponible" if self.disponible else "No disponible"
        return (
            f"Producto: {self.nombre_producto}\n"
            f"  ID: {self.identificador_producto}\n"
            f"  Descripción: {self.descripcion_producto}\n"
            f"  Precio: ${self.precio_producto:.2f}\n"
            f"  Estado: {estado}"
        )
    
    def actualizar_disponibilidad(self, disponible: bool) -> None:
        """
        Actualiza el estado de disponibilidad del producto.
        
        Args:
            disponible: Nuevo estado de disponibilidad
        """
        self.disponible = disponible
    
    def obtener_precio(self) -> float:
        """Retorna el precio del producto."""
        return self.precio_producto

