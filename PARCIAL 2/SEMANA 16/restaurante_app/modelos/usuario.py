from dataclasses import dataclass


@dataclass
class Usuario:
    username: str
    password: str
    nombre: str = ""
    rol: str = "Cliente"
    id: int | None = None

    def __str__(self):
        return f"{self.id or '-'} | {self.username} ({self.nombre}) | {self.rol}"
