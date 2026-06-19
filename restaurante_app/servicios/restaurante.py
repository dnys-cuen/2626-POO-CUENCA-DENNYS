"""
Módulo que define la clase Restaurante.
La clase Restaurante gestiona los productos, clientes y operaciones principales del sistema.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase que representa y gestiona un restaurante.

    Esta clase es responsable de:
    - Almacenar productos disponibles
    - Administrar clientes registrados
    - Gestionar pedidos y transacciones

    Atributos:
        nombre (str): nombre del restaurante
        ubicacion (str): ubicación del restaurante
        productos (list): lista de productos disponibles
        clientes (list): lista de clientes registrados
        pedidos (list): historial de pedidos realizados
    """

    def __init__(self, nombre, ubicacion):
        """
        Constructor de la clase Restaurante.

        Args:
            nombre (str): nombre del restaurante
            ubicacion (str): ubicación del restaurante
        """
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.productos = []
        self.clientes = []
        self.pedidos = []
        self.contador_pedidos = 0  # Para generar IDs de pedidos únicos

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al catálogo del restaurante.

        Args:
            producto (Producto): objeto Producto a registrar
        """
        self.productos.append(producto)
        print(f"✓ Producto '{producto.nombre}' agregado al menú.")

    def registrar_cliente(self, cliente):
        """
        Registra un nuevo cliente en el sistema.

        Args:
            cliente (Cliente): objeto Cliente a registrar
        """
        self.clientes.append(cliente)
        print(f"✓ Cliente '{cliente.nombre}' registrado en el sistema.")

    def buscar_producto_por_id(self, id_producto):
        """
        Busca un producto en el catálogo por su id.

        Args:
            id_producto (int): id del producto a buscar

        Returns:
            Producto: el producto encontrado o None
        """
        for producto in self.productos:
            if producto.id == id_producto:
                return producto
        return None

    def buscar_cliente_por_id(self, id_cliente):
        """
        Busca un cliente en el sistema por su id.

        Args:
            id_cliente (int): id del cliente a buscar

        Returns:
            Cliente: el cliente encontrado o None
        """
        for cliente in self.clientes:
            if cliente.id == id_cliente:
                return cliente
        return None

    def realizar_pedido(self, id_cliente, ids_productos):
        """
        Procesa un pedido de un cliente.

        Args:
            id_cliente (int): id del cliente que realiza el pedido
            ids_productos (list): lista de ids de productos a ordenar

        Returns:
            dict: información del pedido realizado o None si hay error
        """
        cliente = self.buscar_cliente_por_id(id_cliente)

        if cliente is None:
            print(f"✗ Error: Cliente con id {id_cliente} no encontrado.")
            return None

        # Validar y calcular el total
        total = 0
        productos_pedido = []

        for id_prod in ids_productos:
            producto = self.buscar_producto_por_id(id_prod)
            if producto is None:
                print(f"✗ Error: Producto con id {id_prod} no encontrado.")
                return None
            if not producto.disponible:
                print(f"✗ Error: Producto '{producto.nombre}' no está disponible.")
                return None

            productos_pedido.append(producto)
            total += producto.precio

        # Crear el pedido
        self.contador_pedidos += 1
        id_pedido = self.contador_pedidos

        pedido_info = {
            'id': id_pedido,
            'cliente': cliente.nombre,
            'id_cliente': id_cliente,
            'productos': [p.nombre for p in productos_pedido],
            'total': total
        }

        self.pedidos.append(pedido_info)
        cliente.registrar_pedido(id_pedido, total)

        print(f"✓ Pedido #{id_pedido} realizado por {cliente.nombre} - Total: ${total:.2f}")

        return pedido_info

    def mostrar_menu(self):
        """Muestra todos los productos disponibles en el menú."""
        print("\n" + "="*70)
        print(f"MENÚ DE {self.nombre.upper()}")
        print("="*70)

        if not self.productos:
            print("No hay productos disponibles.")
        else:
            for producto in self.productos:
                print(f"  {producto}")

        print("="*70)

    def mostrar_clientes(self):
        """Muestra información de todos los clientes registrados."""
        print("\n" + "="*70)
        print("CLIENTES REGISTRADOS")
        print("="*70)

        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(f"  {cliente}")

        print("="*70)

    def mostrar_historial_pedidos(self):
        """Muestra el historial de todos los pedidos realizados."""
        print("\n" + "="*70)
        print("HISTORIAL DE PEDIDOS")
        print("="*70)

        if not self.pedidos:
            print("No hay pedidos registrados.")
        else:
            for pedido in self.pedidos:
                productos_str = ", ".join(pedido['productos'])
                print(f"  Pedido #{pedido['id']} | Cliente: {pedido['cliente']} | Productos: {productos_str} | Total: ${pedido['total']:.2f}")

        print("="*70)

    def obtener_total_ventas(self):
        """Calcula el total de ventas realizadas."""
        return sum(pedido['total'] for pedido in self.pedidos)

    def obtener_resumen(self):
        """Retorna un resumen general del restaurante."""
        return f"""
╔════════════════════════════════════════════════════════════════╗
║ RESUMEN DEL RESTAURANTE: {self.nombre}
║ Ubicación: {self.ubicacion}
║════════════════════════════════════════════════════════════════║
║ Productos en menú: {len(self.productos)}
║ Clientes registrados: {len(self.clientes)}
║ Pedidos realizados: {len(self.pedidos)}
║ Total de ventas: ${self.obtener_total_ventas():.2f}
╚════════════════════════════════════════════════════════════════╝
"""

    def __str__(self):
        """Retorna información básica del restaurante."""
        return f"Restaurante '{self.nombre}' - {self.ubicacion}"

