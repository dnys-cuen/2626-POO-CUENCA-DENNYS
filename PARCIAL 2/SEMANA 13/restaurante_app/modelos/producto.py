from dataclasses import dataclass

@dataclass
class Producto:
    id: int
    nombre: str
    precio: float
    cantidad: int

    def __str__(self):
        return f"{self.id}: {self.nombre} - ${self.precio} (stock: {self.cantidad})"