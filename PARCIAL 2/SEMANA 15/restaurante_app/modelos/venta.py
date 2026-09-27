from dataclasses import dataclass


@dataclass
class Venta:
    id: int
    username: str
    producto_id: int
    fecha: str

    def __str__(self):
        return f"{self.id}: {self.username} vendió producto {self.producto_id} en {self.fecha}"
