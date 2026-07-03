class Restaurante:
    """Clase de servicio encargada de administrar los productos del restaurante."""

    def __init__(self):
        # Lista que almacena los productos registrados
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un nuevo producto a la lista."""
        self.productos.append(producto)
        print(f"[{producto.nombre}] agregado exitosamente al restaurante.")

    def mostrar_menu(self):
        """Recorre la lista de productos y muestra la información (Polimorfismo)."""
        print("\n=== MENÚ DEL RESTAURANTE ===")
        if not self.productos:
            print("No hay productos registrados en el menú.")
        else:
            for producto in self.productos:
                # Aquí se demuestra el polimorfismo
                # Cada objeto (Platillo o Bebida) responde de forma diferente a mostrar_informacion()
                print(producto.mostrar_informacion())
        print("============================\n")
