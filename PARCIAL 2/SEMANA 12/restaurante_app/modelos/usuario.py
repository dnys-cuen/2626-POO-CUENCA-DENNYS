"""
Módulo de la clase Usuario.
Representa un usuario del restaurante con persistencia.
"""


class Usuario:
    """
    Clase que representa un usuario del restaurante.

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

        Raises:
            ValueError: Si algún campo está vacío.
        """
        if not identificacion or not nombre or not correo:
            raise ValueError("La identificación, nombre y correo no pueden estar vacíos.")

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

    def a_diccionario(self) -> dict:
        """
        Convierte el usuario a un diccionario para serialización JSON.

        Returns:
            dict: Diccionario con los datos del usuario.
        """
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

