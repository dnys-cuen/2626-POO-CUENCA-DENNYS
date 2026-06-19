"""
Módulo que define la clase Cliente.
Los clientes representan las personas que realizan pedidos en el restaurante.
"""


class Cliente:
    """
    Clase que representa un cliente del restaurante.

    Atributos:
        id (int): identificador único del cliente
        nombre (str): nombre del cliente
        email (str): correo electrónico del cliente
        telefono (str): número de teléfono del cliente
        pedidos_realizados (list): historial de pedidos del cliente
    """

    def __init__(self, id, nombre, email, telefono):
        """
        Constructor de la clase Cliente.

        Args:
            id (int): identificador único del cliente
            nombre (str): nombre del cliente
            email (str): correo electrónico del cliente
            telefono (str): número de teléfono del cliente
        """
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.pedidos_realizados = []  # Almacena información sobre pedidos anteriores

    def registrar_pedido(self, id_pedido, total):
        """
        Registra un pedido realizado por el cliente.

        Args:
            id_pedido (int): identificador del pedido
            total (float): monto total del pedido
        """
        pedido_info = {
            'id': id_pedido,
            'total': total
        }
        self.pedidos_realizados.append(pedido_info)

    def obtener_total_gastado(self):
        """Calcula el total gastado por el cliente en todos sus pedidos."""
        return sum(pedido['total'] for pedido in self.pedidos_realizados)

    def obtener_cantidad_pedidos(self):
        """Retorna la cantidad de pedidos realizados."""
        return len(self.pedidos_realizados)

    def __str__(self):
        """Retorna una representación en texto del cliente."""
        total_gastado = self.obtener_total_gastado()
        cantidad_pedidos = self.obtener_cantidad_pedidos()
        return f"[{self.id}] {self.nombre} | Email: {self.email} | Teléfono: {self.telefono} | Pedidos: {cantidad_pedidos} | Total gastado: ${total_gastado:.2f}"

