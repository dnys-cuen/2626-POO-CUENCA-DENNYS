import json
from pathlib import Path

class ArchivoServicio:
    """Lee archivos JSON desde una carpeta base proporcionada."""
    def __init__(self, base_path):
        self.base_path = Path(base_path)

    def leer(self, nombre_archivo):
        ruta = self.base_path / nombre_archivo
        if not ruta.exists():
            return []
        with open(ruta, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
