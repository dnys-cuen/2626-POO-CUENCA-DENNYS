"""
Módulo que define la clase Cliente.
Representa un cliente registrado en el sistema del restaurante.
"""


class Cliente:
    """
    Clase que representa un cliente del restaurante.
    
    Atributos:
        numero_cliente (int): Número identificador del cliente
        nombre_cliente (str): Nombre completo del cliente
        correo_cliente (str): Correo electrónico del cliente
        telefono_cliente (str): Número de teléfono del cliente
        cliente_activo (bool): Indica si el cliente está activo en el sistema
    """
    
    def __init__(
        self,
        numero_cliente: int,
        nombre_cliente: str,
        correo_cliente: str,
        telefono_cliente: str,
        cliente_activo: bool
    ) -> None:
        """
        Inicializa un objeto Cliente.
        
        Args:
            numero_cliente: Número único del cliente
            nombre_cliente: Nombre del cliente
            correo_cliente: Correo del cliente
            telefono_cliente: Teléfono del cliente
            cliente_activo: Si el cliente está activo
        """
        self.numero_cliente = numero_cliente
        self.nombre_cliente = nombre_cliente
        self.correo_cliente = correo_cliente
        self.telefono_cliente = telefono_cliente
        self.cliente_activo = cliente_activo
    
    def __str__(self) -> str:
        """Retorna una representación en texto del cliente."""
        estado = "Activo" if self.cliente_activo else "Inactivo"
        return (
            f"Cliente: {self.nombre_cliente}\n"
            f"  Número: {self.numero_cliente}\n"
            f"  Correo: {self.correo_cliente}\n"
            f"  Teléfono: {self.telefono_cliente}\n"
            f"  Estado: {estado}"
        )
    
    def cambiar_estado(self, nuevo_estado: bool) -> None:
        """
        Cambia el estado de actividad del cliente.
        
        Args:
            nuevo_estado: Nuevo estado del cliente
        """
        self.cliente_activo = nuevo_estado
    
    def actualizar_contacto(self, nuevo_correo: str, nuevo_telefono: str) -> None:
        """
        Actualiza la información de contacto del cliente.
        
        Args:
            nuevo_correo: Nuevo correo electrónico
            nuevo_telefono: Nuevo teléfono
        """
        self.correo_cliente = nuevo_correo
        self.telefono_cliente = nuevo_telefono

