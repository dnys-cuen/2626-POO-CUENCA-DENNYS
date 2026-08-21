"""
Módulo principal de la aplicación restaurante.
Punto de entrada del programa y coordinador de la interacción con el usuario.
Proporciona un menú interactivo para administrar productos y usuarios.
"""

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


def mostrar_menu_principal() -> None:
    """
    Muestra el menú principal de opciones disponibles.
    """
    print("\n" + "=" * 60)
    print(" " * 15 + "SISTEMA DE RESTAURANTE - SEMANA 10")
    print("=" * 60)
    print("GESTIÓN DE PRODUCTOS")
    print("  1. Registrar producto")
    print("  2. Listar productos")
    print("  3. Buscar producto por código")
    print("  4. Actualizar producto")
    print("  5. Eliminar producto")
    print("-" * 60)
    print("GESTIÓN DE USUARIOS")
    print("  6. Registrar usuario")
    print("  7. Listar usuarios")
    print("-" * 60)
    print("PERSISTENCIA")
    print("  8. Cargar productos desde archivo JSON")
    print("-" * 60)
    print("  9. Salir")
    print("=" * 60)


def registrar_producto(restaurante: Restaurante) -> None:
    """
    Solicita los datos de un producto y lo registra en el restaurante.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    try:
        print("\n--- Registrar Nuevo Producto ---")

        codigo = input("Ingrese el código del producto: ").strip()
        if not codigo:
            print("✗ Error: El código no puede estar vacío.")
            return

        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre:
            print("✗ Error: El nombre no puede estar vacío.")
            return

        categoria = input("Ingrese la categoría del producto: ").strip()
        if not categoria:
            print("✗ Error: La categoría no puede estar vacía.")
            return

        try:
            precio = float(input("Ingrese el precio del producto: "))
        except ValueError:
            print("✗ Error: El precio debe ser un número válido.")
            return

        try:
            producto = Producto(codigo, nombre, categoria, precio)
        except ValueError as error:
            print(f"✗ Error: {error}")
            return

        if restaurante.registrar_producto(producto):
            print(f"✓ Producto '{nombre}' registrado exitosamente.")
            print("  (Guardado automáticamente en JSON)")
        else:
            print(f"✗ Error: Ya existe un producto con el código '{codigo}'.")

    except Exception as error:
        print(f"✗ Error inesperado: {error}")


def listar_productos(restaurante: Restaurante) -> None:
    """
    Lista todos los productos registrados en el restaurante.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    productos = restaurante.listar_productos()

    if not productos:
        print("\n℘ No hay productos registrados.")
    else:
        print(f"\n{'=' * 100}")
        print(f"{'LISTADO DE PRODUCTOS':^100}")
        print(f"{'=' * 100}")
        for indice, informacion in enumerate(productos, 1):
            print(f"{indice}. {informacion}")
        print(f"{'=' * 100}")
        print(f"Total de productos: {restaurante.obtener_cantidad_productos()}")


def buscar_producto(restaurante: Restaurante) -> None:
    """
    Busca un producto por su código.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    try:
        codigo = input("\nIngrese el código del producto a buscar: ").strip()
        if not codigo:
            print("✗ Error: El código no puede estar vacío.")
            return

        producto = restaurante.buscar_producto_por_codigo(codigo)

        if producto:
            print(f"\n✓ Producto encontrado:")
            print(f"  {producto.mostrar_informacion()}")
        else:
            print(f"\n✗ No se encontró producto con código '{codigo}'.")

    except Exception as error:
        print(f"✗ Error inesperado: {error}")


def actualizar_producto(restaurante: Restaurante) -> None:
    """
    Actualiza los datos de un producto existente.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    try:
        print("\n--- Actualizar Producto ---")

        codigo = input("Ingrese el código del producto a actualizar: ").strip()
        if not codigo:
            print("✗ Error: El código no puede estar vacío.")
            return

        producto = restaurante.buscar_producto_por_codigo(codigo)
        if not producto:
            print(f"✗ Error: No existe producto con código '{codigo}'.")
            return

        print(f"\nProducto actual: {producto.mostrar_informacion()}")
        print("(Presione Enter para mantener el valor actual)")

        nuevo_nombre = input("Nuevo nombre [Enter para mantener]: ").strip()
        nueva_categoria = input("Nueva categoría [Enter para mantener]: ").strip()

        nuevo_precio_input = input("Nuevo precio [Enter para mantener]: ").strip()
        nuevo_precio = None
        if nuevo_precio_input:
            try:
                nuevo_precio = float(nuevo_precio_input)
            except ValueError:
                print("✗ Error: El precio debe ser un número válido.")
                return

        try:
            if restaurante.actualizar_producto(
                codigo,
                nuevo_nombre if nuevo_nombre else None,
                nueva_categoria if nueva_categoria else None,
                nuevo_precio
            ):
                print("\n✓ Producto actualizado exitosamente.")
                print(f"  {restaurante.buscar_producto_por_codigo(codigo).mostrar_informacion()}")
                print("  (Cambios guardados automáticamente en JSON)")
            else:
                print(f"✗ Error: No se pudo actualizar el producto.")
        except ValueError as error:
            print(f"✗ Error: {error}")

    except Exception as error:
        print(f"✗ Error inesperado: {error}")


def eliminar_producto(restaurante: Restaurante) -> None:
    """
    Elimina un producto del restaurante.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    try:
        codigo = input("\n--- Eliminar Producto ---\nIngrese el código del producto a eliminar: ").strip()
        if not codigo:
            print("✗ Error: El código no puede estar vacío.")
            return

        producto = restaurante.buscar_producto_por_codigo(codigo)
        if not producto:
            print(f"✗ Error: No existe producto con código '{codigo}'.")
            return

        print(f"\nProducto a eliminar: {producto.mostrar_informacion()}")
        confirmacion = input("¿Está seguro de que desea eliminarlo? (s/n): ").strip().lower()

        if confirmacion == 's':
            if restaurante.eliminar_producto(codigo):
                print(f"\n✓ Producto '{codigo}' eliminado exitosamente.")
                print("  (Cambio guardado automáticamente en JSON)")
            else:
                print(f"✗ Error: No se pudo eliminar el producto.")
        else:
            print("✗ Eliminación cancelada.")

    except Exception as error:
        print(f"✗ Error inesperado: {error}")


def registrar_usuario(restaurante: Restaurante) -> None:
    """
    Solicita los datos de un usuario y lo registra en el restaurante.
    Los usuarios se mantienen únicamente en memoria durante esta semana.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    try:
        print("\n--- Registrar Nuevo Usuario ---")
        print("(Los usuarios se almacenan en memoria, no se persisten en esta semana)")

        identificacion = input("Ingrese la identificación del usuario: ").strip()
        if not identificacion:
            print("✗ Error: La identificación no puede estar vacía.")
            return

        nombre = input("Ingrese el nombre del usuario: ").strip()
        if not nombre:
            print("✗ Error: El nombre no puede estar vacío.")
            return

        correo = input("Ingrese el correo del usuario: ").strip()
        if not correo:
            print("✗ Error: El correo no puede estar vacío.")
            return

        usuario = Usuario(identificacion, nombre, correo)

        if restaurante.registrar_usuario(usuario):
            print(f"\n✓ Usuario '{nombre}' registrado exitosamente.")
        else:
            print(f"✗ Error: Ya existe un usuario con la identificación '{identificacion}'.")

    except Exception as error:
        print(f"✗ Error inesperado: {error}")


def listar_usuarios(restaurante: Restaurante) -> None:
    """
    Lista todos los usuarios registrados en el restaurante.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("\n℘ No hay usuarios registrados.")
    else:
        print(f"\n{'=' * 90}")
        print(f"{'LISTADO DE USUARIOS':^90}")
        print(f"{'=' * 90}")
        for indice, informacion in enumerate(usuarios, 1):
            print(f"{indice}. {informacion}")
        print(f"{'=' * 90}")
        print(f"Total de usuarios: {restaurante.obtener_cantidad_usuarios()}")


def cargar_productos_json(restaurante: Restaurante) -> None:
    """
    Carga los productos desde el archivo JSON.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    try:
        if restaurante.cargar_productos_desde_archivo():
            cantidad = restaurante.obtener_cantidad_productos()
            print(f"\n✓ Productos cargados exitosamente desde archivo JSON.")
            print(f"  Total de productos cargados: {cantidad}")
        else:
            print("\n✗ Error: No se pudieron cargar los productos.")
    except Exception as error:
        print(f"✗ Error inesperado al cargar: {error}")


def main() -> None:
    """
    Función principal que controla el flujo de la aplicación.
    Presenta el menú y ejecuta las operaciones solicitadas por el usuario.
    Carga automáticamente los productos del archivo al iniciar.
    """
    restaurante = Restaurante()

    print("\n" + "=" * 60)
    print(" " * 10 + "¡Bienvenido al Sistema de Restaurante!")
    print(" " * 15 + "Semana 10 - Persistencia de Productos")
    print("=" * 60)
    print("Cargando productos desde archivo...")

    if restaurante.cargar_productos_desde_archivo():
        cantidad = restaurante.obtener_cantidad_productos()
        if cantidad > 0:
            print(f"✓ Se cargaron {cantidad} producto(s) desde el archivo JSON.")
        else:
            print("℘ No se encontraron productos previos. Comenzando con colección vacía.")
    else:
        print("℘ No se encontró archivo de productos. Comenzando con colección vacía.")

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-9): ").strip()

        if opcion == "1":
            registrar_producto(restaurante)

        elif opcion == "2":
            listar_productos(restaurante)

        elif opcion == "3":
            buscar_producto(restaurante)

        elif opcion == "4":
            actualizar_producto(restaurante)

        elif opcion == "5":
            eliminar_producto(restaurante)

        elif opcion == "6":
            registrar_usuario(restaurante)

        elif opcion == "7":
            listar_usuarios(restaurante)

        elif opcion == "8":
            cargar_productos_json(restaurante)

        elif opcion == "9":
            print("\n¡Gracias por usar el Sistema de Restaurante! Hasta luego.")
            break

        else:
            print("✗ Error: Opción no válida. Por favor, seleccione una opción del 1 al 9.")


if __name__ == "__main__":
    main()

