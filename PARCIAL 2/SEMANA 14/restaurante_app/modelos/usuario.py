from dataclasses import dataclass


@dataclass
class Usuario:
    username: str
    password: str
    nombre: str = ""

    def __str__(self):
        return f"{self.username} ({self.nombre})"
