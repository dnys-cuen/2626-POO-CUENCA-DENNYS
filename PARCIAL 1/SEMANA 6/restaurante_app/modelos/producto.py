class Producto:
    """Clase padre que representa un producto general del restaurante."""

    def __init__(self, nombre, precio, disponibilidad):
        # Atributos comunes
        self.nombre = nombre
        self.__precio = precio  # Atributo encapsulado (privado)
        self.disponibilidad = disponibilidad

    def obtener_precio(self):
        """Método para acceder al precio encapsulado."""
        return self.__precio

    def cambiar_precio(self, nuevo_precio):
        """Método para modificar el precio con validación."""
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio no puede ser negativo ni cero.")

    def mostrar_informacion(self):
        """Método general a ser sobrescrito (Polimorfismo)."""
        pass
