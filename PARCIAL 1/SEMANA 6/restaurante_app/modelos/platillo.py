from modelos.producto import Producto

class Platillo(Producto):
    """Clase hija que representa una comida, hereda de Producto."""

    def __init__(self, nombre, precio, disponibilidad, calorias):
        # Uso de super() para inicializar atributos de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        self.calorias = calorias # Atributo específico de Platillo

    def mostrar_informacion(self):
        """Sobrescribe el método de la clase padre para mostrar info de platillo."""
        estado = "Disponible" if self.disponibilidad else "Agotado"
        return f"Platillo: {self.nombre} | Precio: ${self.obtener_precio():.2f} | {self.calorias} kcal | Estado: {estado}"
