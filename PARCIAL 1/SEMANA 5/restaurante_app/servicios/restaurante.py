"""
Módulo que define la clase Restaurante.
Gestiona listas de productos y clientes del sistema de restaurante.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase que administra el restaurante.
    
    Gestiona listas de productos y clientes registrados en el sistema.
    
    Atributos:
        nombre_restaurante (str): Nombre del restaurante
        ubicacion_restaurante (str): Ubicación del restaurante
        lista_productos (list): Lista de objetos Producto
        lista_clientes (list): Lista de objetos Cliente
    """
    
    def __init__(
        self,
        nombre_restaurante: str,
        ubicacion_restaurante: str
    ) -> None:
        """
        Inicializa un objeto Restaurante.
        
        Args:
            nombre_restaurante: Nombre del restaurante
            ubicacion_restaurante: Ubicación del restaurante
        """
        self.nombre_restaurante = nombre_restaurante
        self.ubicacion_restaurante = ubicacion_restaurante
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []
    
    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un producto a la lista del restaurante.
        
        Args:
            producto: Objeto Producto a agregar
        """
        self.lista_productos.append(producto)
        print(f"✓ Producto '{producto.nombre_producto}' agregado al sistema")
    
    def agregar_cliente(self, cliente: Cliente) -> None:
        """
        Agrega un cliente a la lista del restaurante.
        
        Args:
            cliente: Objeto Cliente a agregar
        """
        self.lista_clientes.append(cliente)
        print(f"✓ Cliente '{cliente.nombre_cliente}' registrado en el sistema")
    
    def obtener_productos(self) -> list[Producto]:
        """Retorna la lista de productos del restaurante."""
        return self.lista_productos
    
    def obtener_clientes(self) -> list[Cliente]:
        """Retorna la lista de clientes del restaurante."""
        return self.lista_clientes
    
    def contar_productos(self) -> int:
        """Retorna la cantidad de productos registrados."""
        return len(self.lista_productos)
    
    def contar_clientes(self) -> int:
        """Retorna la cantidad de clientes registrados."""
        return len(self.lista_clientes)
    
    def mostrar_informacion_restaurante(self) -> None:
        """Muestra la información general del restaurante."""
        print("\n" + "=" * 60)
        print(f"RESTAURANTE: {self.nombre_restaurante}")
        print(f"UBICACIÓN: {self.ubicacion_restaurante}")
        print(f"Total de productos: {self.contar_productos()}")
        print(f"Total de clientes: {self.contar_clientes()}")
        print("=" * 60 + "\n")
    
    def mostrar_productos(self) -> None:
        """Muestra todos los productos registrados en el restaurante."""
        print("\n" + "-" * 60)
        print("LISTA DE PRODUCTOS")
        print("-" * 60)
        
        if len(self.lista_productos) == 0:
            print("No hay productos registrados.")
        else:
            for i, producto in enumerate(self.lista_productos, 1):
                print(f"\n{i}. {producto}")
        
        print("-" * 60 + "\n")
    
    def mostrar_clientes(self) -> None:
        """Muestra todos los clientes registrados en el restaurante."""
        print("\n" + "-" * 60)
        print("LISTA DE CLIENTES")
        print("-" * 60)
        
        if len(self.lista_clientes) == 0:
            print("No hay clientes registrados.")
        else:
            for i, cliente in enumerate(self.lista_clientes, 1):
                print(f"\n{i}. {cliente}")
        
        print("-" * 60 + "\n")
    
    def buscar_producto_por_nombre(self, nombre_busqueda: str) -> Producto:
        """
        Busca un producto por su nombre.
        
        Args:
            nombre_busqueda: Nombre del producto a buscar
            
        Returns:
            El objeto Producto si existe, None si no
        """
        for producto in self.lista_productos:
            if producto.nombre_producto.lower() == nombre_busqueda.lower():
                return producto
        return None
    
    def buscar_cliente_por_nombre(self, nombre_busqueda: str) -> Cliente:
        """
        Busca un cliente por su nombre.
        
        Args:
            nombre_busqueda: Nombre del cliente a buscar
            
        Returns:
            El objeto Cliente si existe, None si no
        """
        for cliente in self.lista_clientes:
            if cliente.nombre_cliente.lower() == nombre_busqueda.lower():
                return cliente
        return None

