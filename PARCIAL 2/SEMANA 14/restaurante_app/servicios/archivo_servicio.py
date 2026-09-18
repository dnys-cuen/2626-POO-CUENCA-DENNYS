import json
from pathlib import Path


class ArchivoServicio:
    """Maneja lectura y escritura de datos en archivos JSON."""

    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def leer(self, nombre_archivo):
        ruta = self.base_path / nombre_archivo
        if not ruta.exists():
            return []
        with open(ruta, "r", encoding="utf-8") as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return []

    def guardar(self, nombre_archivo, datos):
        ruta = self.base_path / nombre_archivo
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)
            archivo.write("\n")
