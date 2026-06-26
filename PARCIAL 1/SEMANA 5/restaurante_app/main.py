"""
Punto de entrada del sistema de gestión de restaurante.
Crea objetos de Producto, Cliente y Restaurante.
Demuestra el funcionamiento del sistema mediante la creación y gestión de datos.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# ============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================================

def main() -> None:
    """Función principal que ejecuta el sistema de gestión de restaurante."""

    # Crear una instancia del restaurante
    restaurante = Restaurante(
        nombre_restaurante="Restaurante El Sabor",
        ubicacion_restaurante="Calle Principal 123, Cuenca"
    )

    # ========================================================================
    # CREAR PRODUCTOS
    # ========================================================================

    # Primer producto: Plato principal
    producto_1 = Producto(
        identificador_producto=1,
        nombre_producto="Hornado",
        descripcion_producto="Cerdo asado con papas y maíz",
        precio_producto=18.50,
        disponible=True
    )

    # Segundo producto: Aplato principal
    producto_2 = Producto(
        identificador_producto=2,
        nombre_producto="Ceviche",
        descripcion_producto="Ceviche de camarones con aguachile",
        precio_producto=22.75,
        disponible=True
    )

    # Tercer producto: Bebida
    producto_3 = Producto(
        identificador_producto=3,
        nombre_producto="Jugo de Naranja",
        descripcion_producto="Jugo natural recién exprimido",
        precio_producto=4.50,
        disponible=True
    )

    # Cuarto producto: Postre
    producto_4 = Producto(
        identificador_producto=4,
        nombre_producto="Flan Casero",
        descripcion_producto="Flan tradicional con caramelo",
        precio_producto=6.00,
        disponible=False
    )

    # ========================================================================
    # CREAR CLIENTES
    # ========================================================================

    # Primer cliente
    cliente_1 = Cliente(
        numero_cliente=101,
        nombre_cliente="Juan García",
        correo_cliente="juan.garcia@email.com",
        telefono_cliente="0987654321",
        cliente_activo=True
    )

    # Segundo cliente
    cliente_2 = Cliente(
        numero_cliente=102,
        nombre_cliente="María López",
        correo_cliente="maria.lopez@email.com",
        telefono_cliente="0912345678",
        cliente_activo=True
    )

    # Tercer cliente
    cliente_3 = Cliente(
        numero_cliente=103,
        nombre_cliente="Carlos Rodríguez",
        correo_cliente="carlos.rodriguez@email.com",
        telefono_cliente="0998765432",
        cliente_activo=False
    )

    # ========================================================================
    # AGREGAR PRODUCTOS AL RESTAURANTE
    # ========================================================================

    print("\n📋 REGISTRANDO PRODUCTOS EN EL SISTEMA...")
    restaurante.agregar_producto(producto_1)
    restaurante.agregar_producto(producto_2)
    restaurante.agregar_producto(producto_3)
    restaurante.agregar_producto(producto_4)

    # ========================================================================
    # AGREGAR CLIENTES AL RESTAURANTE
    # ========================================================================

    print("\n👥 REGISTRANDO CLIENTES EN EL SISTEMA...")
    restaurante.agregar_cliente(cliente_1)
    restaurante.agregar_cliente(cliente_2)
    restaurante.agregar_cliente(cliente_3)

    # ========================================================================
    # MOSTRAR INFORMACIÓN DEL RESTAURANTE
    # ========================================================================

    restaurante.mostrar_informacion_restaurante()

    # Mostrar todos los productos
    restaurante.mostrar_productos()

    # Mostrar todos los clientes
    restaurante.mostrar_clientes()

    # ========================================================================
    # DEMOSTRAR FUNCIONALIDADES
    # ========================================================================

    print("\n" + "=" * 60)
    print("DEMOSTRANDO FUNCIONALIDADES DEL SISTEMA")
    print("=" * 60)

    # Buscar un producto específico
    print("\n🔍 Buscando producto 'Hornado'...")
    producto_encontrado = restaurante.buscar_producto_por_nombre("Hornado")
    if producto_encontrado:
        print(f"✓ Producto encontrado: {producto_encontrado.nombre_producto}")
        print(f"  Precio: ${producto_encontrado.obtener_precio():.2f}")

    # Buscar un cliente específico
    print("\n🔍 Buscando cliente 'María López'...")
    cliente_encontrado = restaurante.buscar_cliente_por_nombre("María López")
    if cliente_encontrado:
        print(f"✓ Cliente encontrado: {cliente_encontrado.nombre_cliente}")
        print(f"  Email: {cliente_encontrado.correo_cliente}")

    # Actualizar disponibilidad de un producto
    print("\n📝 Actualizando disponibilidad del Flan Casero...")
    producto_4.actualizar_disponibilidad(True)
    print(f"✓ Flan Casero ahora está disponible")

    # Cambiar estado de un cliente
    print("\n📝 Activando cliente 'Carlos Rodríguez'...")
    cliente_3.cambiar_estado(True)
    print(f"✓ {cliente_3.nombre_cliente} ha sido activado")

    # Mostrar resumen final
    print("\n" + "=" * 60)
    print("RESUMEN FINAL DEL SISTEMA")
    print("=" * 60)
    print(f"Total de productos en el restaurante: {restaurante.contar_productos()}")
    print(f"Total de clientes registrados: {restaurante.contar_clientes()}")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()

