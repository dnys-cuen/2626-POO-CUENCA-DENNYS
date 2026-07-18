"""
Módulo principal de la aplicación restaurante.
Punto de entrada del programa y coordinador de la interacción por consola.
"""

from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    """
    Muestra el menú principal de opciones disponibles.
    """
    print("\n" + "=" * 50)
    print(" " * 12 + "SISTEMA DE RESTAURANTE")
    print("=" * 50)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-" * 50)
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-" * 50)
    print("6. Salir")
    print("=" * 50)


def registrar_producto(restaurante: Restaurante) -> None:
    """
    Solicita los datos de un producto y lo registra en el restaurante.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    try:
        codigo = input("Ingrese el código del producto: ").strip()
        if not codigo:
            print("Error: El código no puede estar vacío.")
            return

        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            return

        categoria = input("Ingrese la categoría del producto: ").strip()
        if not categoria:
            print("Error: La categoría no puede estar vacía.")
            return

        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("Error: El precio no puede ser negativo.")
                return
        except ValueError:
            print("Error: El precio debe ser un número válido.")
            return

        producto = Producto(codigo, nombre, categoria, precio)

        if restaurante.registrar_producto(producto):
            print(f"\n✓ Producto '{nombre}' registrado exitosamente.")
        else:
            print(f"✗ Error: Ya existe un producto con el código '{codigo}'.")

    except Exception as error:
        print(f"Error inesperado: {error}")


def registrar_bebida(restaurante: Restaurante) -> None:
    """
    Solicita los datos de una bebida y la registra en el restaurante.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    try:
        codigo = input("Ingrese el código de la bebida: ").strip()
        if not codigo:
            print("Error: El código no puede estar vacío.")
            return

        nombre = input("Ingrese el nombre de la bebida: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            return

        categoria = input("Ingrese la categoría de la bebida: ").strip()
        if not categoria:
            print("Error: La categoría no puede estar vacía.")
            return

        try:
            precio = float(input("Ingrese el precio de la bebida: "))
            if precio < 0:
                print("Error: El precio no puede ser negativo.")
                return
        except ValueError:
            print("Error: El precio debe ser un número válido.")
            return

        tamaño = input("Ingrese el tamaño (pequeño, mediano, grande): ").strip()
        if not tamaño:
            print("Error: El tamaño no puede estar vacío.")
            return

        tipo_envase = input("Ingrese el tipo de envase (vaso, botella, lata): ").strip()
        if not tipo_envase:
            print("Error: El tipo de envase no puede estar vacío.")
            return

        bebida = Bebida(codigo, nombre, categoria, precio, tamaño, tipo_envase)

        if restaurante.registrar_producto(bebida):
            print(f"\n✓ Bebida '{nombre}' registrada exitosamente.")
        else:
            print(f"✗ Error: Ya existe un producto con el código '{codigo}'.")

    except Exception as error:
        print(f"Error inesperado: {error}")


def registrar_cliente(restaurante: Restaurante) -> None:
    """
    Solicita los datos de un cliente y lo registra en el restaurante.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    try:
        identificacion = input("Ingrese la identificación del cliente: ").strip()
        if not identificacion:
            print("Error: La identificación no puede estar vacía.")
            return

        nombre = input("Ingrese el nombre del cliente: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            return

        correo = input("Ingrese el correo del cliente: ").strip()
        if not correo:
            print("Error: El correo no puede estar vacío.")
            return

        cliente = Cliente(identificacion, nombre, correo)

        if restaurante.registrar_cliente(cliente):
            print(f"\n✓ Cliente '{nombre}' registrado exitosamente.")
        else:
            print(f"✗ Error: Ya existe un cliente con la identificación '{identificacion}'.")

    except Exception as error:
        print(f"Error inesperado: {error}")


def listar_productos(restaurante: Restaurante) -> None:
    """
    Lista todos los productos registrados en el restaurante.
    Demuestra el uso del polimorfismo con productos y bebidas.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    productos = restaurante.listar_productos()

    if not productos:
        print("\n℘ No hay productos registrados.")
    else:
        print(f"\n{'=' * 90}")
        print(f"{'LISTADO DE PRODUCTOS':^90}")
        print(f"{'=' * 90}")
        for indice, informacion in enumerate(productos, 1):
            print(f"{indice}. {informacion}")
        print(f"{'=' * 90}")
        print(f"Total de productos: {restaurante.obtener_cantidad_productos()}")


def listar_clientes(restaurante: Restaurante) -> None:
    """
    Lista todos los clientes registrados en el restaurante.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    clientes = restaurante.listar_clientes()

    if not clientes:
        print("\n℘ No hay clientes registrados.")
    else:
        print(f"\n{'=' * 80}")
        print(f"{'LISTADO DE CLIENTES':^80}")
        print(f"{'=' * 80}")
        for indice, informacion in enumerate(clientes, 1):
            print(f"{indice}. {informacion}")
        print(f"{'=' * 80}")
        print(f"Total de clientes: {restaurante.obtener_cantidad_clientes()}")


def main() -> None:
    """
    Función principal que controla el flujo de la aplicación.
    Presenta el menú y ejecuta las operaciones solicitadas por el usuario.
    """
    restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto(restaurante)

        elif opcion == "2":
            registrar_bebida(restaurante)

        elif opcion == "3":
            registrar_cliente(restaurante)

        elif opcion == "4":
            listar_productos(restaurante)

        elif opcion == "5":
            listar_clientes(restaurante)

        elif opcion == "6":
            print("\n¡Gracias por usar el Sistema de Restaurante! Hasta luego.")
            break

        else:
            print("✗ Error: Opción no válida. Por favor, seleccione una opción del 1 al 6.")


if __name__ == "__main__":
    main()

