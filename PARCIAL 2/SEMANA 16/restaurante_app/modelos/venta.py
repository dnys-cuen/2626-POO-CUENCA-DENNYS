from dataclasses import dataclass


@dataclass
class Venta:
    id: int
    username: str
    producto_id: int
    fecha: str
    cantidad: int = 1

    def __str__(self):
        return f"{self.id}: {self.username} vendió {self.cantidad} unidad(es) del producto {self.producto_id} en {self.fecha}"
