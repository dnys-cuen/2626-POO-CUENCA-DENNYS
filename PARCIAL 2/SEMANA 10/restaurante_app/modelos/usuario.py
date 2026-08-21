"""
Módulo de la clase Usuario.
Representa un usuario general del restaurante.
En esta semana, los usuarios se mantienen en memoria y no se persisten en JSON.
"""


class Usuario:
    """
    Clase que representa un usuario general del restaurante.

    Attributes:
        identificacion (str): Número de identificación única del usuario.
        nombre (str): Nombre completo del usuario.
        correo (str): Correo electrónico del usuario.
    """

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        """
        Inicializa una instancia de la clase Usuario.

        Args:
            identificacion (str): Número de identificación del usuario.
            nombre (str): Nombre del usuario.
            correo (str): Correo electrónico del usuario.
        """
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def mostrar_informacion(self) -> str:
        """
        Retorna la información del usuario de manera formateada.

        Returns:
            str: Cadena con la información del usuario.
        """
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )

