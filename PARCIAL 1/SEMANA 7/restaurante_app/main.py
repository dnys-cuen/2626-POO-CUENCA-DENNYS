"""
Punto de entrada del sistema restaurante_app
Muestra un menú interactivo por consola y permite registrar/listar/buscar
productos y clientes.
"""

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


def cargar_datos_ejemplo(rest: Restaurante) -> None:
    """Carga datos de ejemplo para facilitar la experiencia didáctica."""
    ejemplos_productos = [
        ("Hamburguesa clásica", "Comida", 12.5, True),
        ("Papas fritas", "Acompañamiento", 5.0, True),
        ("Limonada natural", "Bebida", 4.0, True),
        ("Pastel de chocolate", "Postre", 7.0, False),
    ]

    ejemplos_clientes = [
        ("Ana Perez", "ana.perez@example.com", "C001"),
        ("Luis Gómez", "luis.gomez@example.com", "C002"),
    ]

    for nombre, categoria, precio, disponible in ejemplos_productos:
        try:
            p = Producto(nombre, categoria, precio, disponible)
            rest.registrar_producto(p)
        except Exception as e:
            # No detener la carga si hay un dato inválido
            print(f"Error al cargar producto de ejemplo: {e}")

    for nombre, correo, idc in ejemplos_clientes:
        try:
            c = Cliente(nombre=nombre, correo=correo, id_cliente=idc)
            rest.registrar_cliente(c)
        except Exception as e:
            print(f"Error al cargar cliente de ejemplo: {e}")


def mostrar_menu() -> None:
    print("========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("----------------------------------------")
    print("7. Salir")


def solicitar_producto_desde_input() -> Producto:
    """Solicita datos por consola y crea una instancia de Producto.

    Lanza ValueError si los datos no cumplen validaciones.
    """
    nombre = input("Nombre del producto: ").strip()
    categoria = input("Categoría: ").strip()
    precio_raw = input("Precio (ej. 12.50): ").strip()
    disponible_raw = input("Disponible (s/n): ").strip()

    precio = float(precio_raw)
    disponible = disponible_raw.lower() in ("s", "si", "sí", "y", "1", "true")

    return Producto(nombre, categoria, precio, disponible)


def solicitar_cliente_desde_input() -> Cliente:
    nombre = input("Nombre del cliente: ").strip()
    correo = input("Correo electrónico: ").strip()
    id_cliente = input("ID del cliente: ").strip()
    return Cliente(nombre=nombre, correo=correo, id_cliente=id_cliente)


def main() -> None:
    rest = Restaurante()
    cargar_datos_ejemplo(rest)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("-- Registrar producto --")
            try:
                producto = solicitar_producto_desde_input()
                rest.registrar_producto(producto)
                print("Producto registrado correctamente.")
            except Exception as e:
                print(f"No se pudo registrar el producto: {e}")

        elif opcion == "2":
            print("-- Lista de productos --")
            productos = rest.listar_productos()
            if not productos:
                print("No hay productos registrados.")
            else:
                for idx, p in enumerate(productos, start=1):
                    print(f"{idx}. {p.mostrar_informacion()}")

        elif opcion == "3":
            termino = input("Ingrese nombre o parte del nombre a buscar: ").strip()
            resultados = rest.buscar_producto_por_nombre(termino)
            print(f"Se encontraron {len(resultados)} resultados:")
            for p in resultados:
                print(p.mostrar_informacion())

        elif opcion == "4":
            print("-- Registrar cliente --")
            try:
                cliente = solicitar_cliente_desde_input()
                rest.registrar_cliente(cliente)
                print("Cliente registrado correctamente.")
            except Exception as e:
                print(f"No se pudo registrar el cliente: {e}")

        elif opcion == "5":
            print("-- Lista de clientes --")
            clientes = rest.listar_clientes()
            if not clientes:
                print("No hay clientes registrados.")
            else:
                for idx, c in enumerate(clientes, start=1):
                    print(f"{idx}. ID: {c.id_cliente} | Nombre: {c.nombre} | Correo: {c.correo}")

        elif opcion == "6":
            id_buscar = input("Ingrese ID del cliente a buscar: ").strip()
            cliente = rest.buscar_cliente_por_id(id_buscar)
            if cliente:
                print(f"Cliente encontrado: ID: {cliente.id_cliente} | Nombre: {cliente.nombre} | Correo: {cliente.correo}")
            else:
                print("Cliente no encontrado.")

        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

        input("Presione Enter para continuar...")


if __name__ == "__main__":
    main()

