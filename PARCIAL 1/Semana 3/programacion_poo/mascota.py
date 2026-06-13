# archivo: mascota.py
# Contiene la clase Mascota para Programación Orientada a Objetos

class Mascota:
    """Clase que representa una mascota.

    Atributos:
        nombre (str): Nombre de la mascota
        especie (str): Especie (por ejemplo: perro, gato, pájaro)
        edad (int): Edad en años

    Métodos:
        mostrar_informacion(): Muestra la información de la mascota de forma organizada
        hacer_sonido(): Imprime un sonido característico según la especie (si aplica)
    """

    def __init__(self, nombre: str, especie: str, edad: int):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self) -> None:
        """Imprime la información de la mascota de forma organizada."""
        print("\n" + "-"*40)
        print(f"Nombre : {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad   : {self.edad} años")
        print("-"*40)

    def hacer_sonido(self) -> None:
        """Imprime un sonido representativo según la especie."""
        especie_key = (self.especie or "").strip().lower()
        sonidos = {
            "perro": "¡Guau!",
            "perrita": "¡Guau!",
            "gato": "¡Miau!",
            "pájaro": "¡Pío!",
            "pajaro": "¡Pío!",
            "ave": "¡Pío!",
            "conejo": "(silencioso)",
            "hámster": "(silencioso)",
            "hamster": "(silencioso)",
            "pez": "(no emite sonido audible)",
        }

        sonido = sonidos.get(especie_key, "(sonido no definido)")
        print(f"{self.nombre} hace: {sonido}")


