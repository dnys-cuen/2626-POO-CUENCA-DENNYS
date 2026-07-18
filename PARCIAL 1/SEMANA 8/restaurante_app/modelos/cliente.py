"""
Módulo de la clase Cliente.
Representa un cliente registrado en el restaurante con responsabilidad única.
"""


class Cliente:
    """
    Clase que representa un cliente del restaurante.

    Attributes:
        identificacion (str): Número de identificación única del cliente.
        nombre (str): Nombre completo del cliente.
        correo (str): Correo electrónico del cliente.
    """

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        """
        Inicializa una instancia de la clase Cliente.

        Args:
            identificacion (str): Número de identificación del cliente.
            nombre (str): Nombre del cliente.
            correo (str): Correo electrónico del cliente.
        """
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def mostrar_informacion(self) -> str:
        """
        Retorna la información del cliente de manera formateada.

        Returns:
            str: Cadena con la información del cliente.
        """
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )

