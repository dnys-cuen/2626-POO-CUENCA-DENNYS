"""
SISTEMA DE GESTIÓN DE RESTAURANTE
==================================

Archivo principal (main.py) que demuestra el funcionamiento del sistema de
restaurante. Este archivo crea objetos de las diferentes clases y muestra cómo
se comunican mediante importaciones.

Estructura:
- modelos/producto.py: Define la clase Producto
- modelos/cliente.py: Define la clase Cliente
- servicios/restaurante.py: Define la clase Restaurante (gestión principal)
- main.py: Punto de arranque del programa
"""

# Importar las clases del sistema
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    """
    Función principal que ejecuta la demostración del sistema.
    """

    print("\n" + "█"*70)
    print("█" + " "*68 + "█")
    print("█" + "  BIENVENIDO AL SISTEMA DE GESTIÓN DE RESTAURANTE".center(68) + "█")
    print("█" + " "*68 + "█")
    print("█"*70 + "\n")

    # ====================
    # 1. CREAR RESTAURANTE
    # ====================
    print("["*1 + "1. Creando el restaurante..." + "]"*1)
    mi_restaurante = Restaurante("La Buena Mesa", "Centro Histórico")
    print(f"✓ {mi_restaurante}\n")

    # ====================
    # 2. CREAR PRODUCTOS
    # ====================
    print("["*1 + "2. Agregando productos al menú..." + "]"*1)

    # Crear productos
    producto1 = Producto(101, "Hamburguesa Clásica", "Plato Fuerte", 12.50)
    producto2 = Producto(102, "Ensalada César", "Entrada", 8.00)
    producto3 = Producto(103, "Pasta Carbonara", "Plato Fuerte", 14.99)
    producto4 = Producto(104, "Refresco Tropical", "Bebida", 3.50)
    producto5 = Producto(105, "Flan Casero", "Postre", 6.00)

    # Agregar productos al restaurante
    mi_restaurante.agregar_producto(producto1)
    mi_restaurante.agregar_producto(producto2)
    mi_restaurante.agregar_producto(producto3)
    mi_restaurante.agregar_producto(producto4)
    mi_restaurante.agregar_producto(producto5)

    # ====================
    # 3. CREAR CLIENTES
    # ====================
    print("\n["*1 + "3. Registrando clientes..." + "]"*1)

    cliente1 = Cliente(1001, "Juan García", "juan.garcia@email.com", "555-1234")
    cliente2 = Cliente(1002, "María Rodríguez", "maria.rodriguez@email.com", "555-5678")
    cliente3 = Cliente(1003, "Carlos López", "carlos.lopez@email.com", "555-9012")

    mi_restaurante.registrar_cliente(cliente1)
    mi_restaurante.registrar_cliente(cliente2)
    mi_restaurante.registrar_cliente(cliente3)

    # ====================
    # 4. MOSTRAR MENÚ
    # ====================
    print("\n["*1 + "4. Mostrando menú disponible..." + "]"*1)
    mi_restaurante.mostrar_menu()

    # ====================
    # 5. PROCESAR PEDIDOS
    # ====================
    print("\n["*1 + "5. Procesando pedidos de clientes..." + "]"*1)

    # Pedido 1: Juan García pide hamburguesa y refresco
    mi_restaurante.realizar_pedido(1001, [101, 104])

    # Pedido 2: María Rodríguez pide pasta, ensalada y postre
    mi_restaurante.realizar_pedido(1002, [103, 102, 105])

    # Pedido 3: Carlos López pide ensalada y refresco
    mi_restaurante.realizar_pedido(1003, [102, 104])

    # Pedido 4: Juan García realiza otro pedido (para demostrar múltiples pedidos)
    mi_restaurante.realizar_pedido(1001, [103, 105])

    # ====================
    # 6. MOSTRAR CLIENTES
    # ====================
    print("\n["*1 + "6. Información de clientes registrados..." + "]"*1)
    mi_restaurante.mostrar_clientes()

    # ====================
    # 7. MOSTRAR HISTORIAL DE PEDIDOS
    # ====================
    print("\n["*1 + "7. Historial completo de pedidos..." + "]"*1)
    mi_restaurante.mostrar_historial_pedidos()

    # ====================
    # 8. MOSTRAR RESUMEN
    # ====================
    print("\n["*1 + "8. Resumen del sistema..." + "]"*1)
    print(mi_restaurante.obtener_resumen())

    # ====================
    # 9. DEMOSTRACIÓN ADICIONAL
    # ====================
    print("\n["*1 + "9. Demostraciones adicionales..." + "]"*1)

    # Buscar un cliente y mostrar sus detalles
    cliente_buscado = mi_restaurante.buscar_cliente_por_id(1001)
    if cliente_buscado:
        print(f"\nCliente encontrado: {cliente_buscado}")
        print(f"  - Total gastado: ${cliente_buscado.obtener_total_gastado():.2f}")
        print(f"  - Cantidad de pedidos: {cliente_buscado.obtener_cantidad_pedidos()}")

    # Buscar un producto y mostrar su información
    producto_buscado = mi_restaurante.buscar_producto_por_id(103)
    if producto_buscado:
        print(f"\nProducto encontrado: {producto_buscado}")

    print("\n" + "█"*70)
    print("█" + "  FIN DE LA DEMOSTRACIÓN".center(68) + "█")
    print("█"*70 + "\n")


if __name__ == "__main__":
    # Punto de entrada del programa
    main()

