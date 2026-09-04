"""
Módulo principal de la aplicación restaurante.
Punto de entrada del programa y coordinador de la interacción con el usuario.
Proporciona un menú interactivo para administrar productos, usuarios y ventas.
"""

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


def mostrar_menu_principal() -> None:
    """
    Muestra el menú principal de opciones disponibles.
    """
    print("\n" + "=" * 70)
    print(" " * 15 + "SISTEMA DE RESTAURANTE - SEMANA 12")
    print("=" * 70)
    print("GESTIÓN DE PRODUCTOS")
    print("  1. Registrar producto")
    print("  2. Listar productos")
    print("  3. Buscar producto por código")
    print("  4. Actualizar producto")
    print("  5. Eliminar producto")
    print("-" * 70)
    print("GESTIÓN DE USUARIOS")
    print("  6. Registrar usuario")
    print("  7. Listar usuarios")
    print("-" * 70)
    print("GESTIÓN DE VENTAS")
    print("  8. Realizar venta")
    print("  9. Listar todas las ventas")
    print(" 10. Consultar ventas de un usuario")
    print("-" * 70)
    print(" 11. Guardar datos a archivo")
    print(" 12. Cargar datos desde archivo")
    print("-" * 70)
    print(" 13. Salir")
    print("=" * 70)


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
            stock = int(input("Ingrese la cantidad en stock: "))
        except ValueError:
            print("✗ Error: El stock debe ser un número entero válido.")
            return

        try:
            producto = Producto(codigo, nombre, categoria, precio, stock)
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
        print(f"\n{'=' * 110}")
        print(f"{'LISTADO DE PRODUCTOS':^110}")
        print(f"{'=' * 110}")
        for indice, informacion in enumerate(productos, 1):
            print(f"{indice}. {informacion}")
        print(f"{'=' * 110}")
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

        nuevo_stock_input = input("Nuevo stock [Enter para mantener]: ").strip()
        nuevo_stock = None
        if nuevo_stock_input:
            try:
                nuevo_stock = int(nuevo_stock_input)
            except ValueError:
                print("✗ Error: El stock debe ser un número entero válido.")
                return

        try:
            if restaurante.actualizar_producto(
                codigo,
                nuevo_nombre if nuevo_nombre else None,
                nueva_categoria if nueva_categoria else None,
                nuevo_precio,
                nuevo_stock
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

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    try:
        print("\n--- Registrar Nuevo Usuario ---")

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

        try:
            usuario = Usuario(identificacion, nombre, correo)
        except ValueError as error:
            print(f"✗ Error: {error}")
            return

        if restaurante.registrar_usuario(usuario):
            print(f"\n✓ Usuario '{nombre}' registrado exitosamente.")
            print("  (Guardado automáticamente en JSON)")
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
        print(f"\n{'=' * 100}")
        print(f"{'LISTADO DE USUARIOS':^100}")
        print(f"{'=' * 100}")
        for indice, informacion in enumerate(usuarios, 1):
            print(f"{indice}. {informacion}")
        print(f"{'=' * 100}")
        print(f"Total de usuarios: {restaurante.obtener_cantidad_usuarios()}")


def realizar_venta(restaurante: Restaurante) -> None:
    """
    Realiza una venta de un producto a un usuario.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    try:
        print("\n--- Realizar Venta ---")

        identificacion_usuario = input("Ingrese la identificación del usuario: ").strip()
        if not identificacion_usuario:
            print("✗ Error: La identificación del usuario no puede estar vacía.")
            return

        usuario = restaurante.buscar_usuario(identificacion_usuario)
        if not usuario:
            print(f"✗ Error: No existe usuario con identificación '{identificacion_usuario}'.")
            return

        print(f"✓ Usuario encontrado: {usuario.mostrar_informacion()}")

        codigo_producto = input("Ingrese el código del producto: ").strip()
        if not codigo_producto:
            print("✗ Error: El código del producto no puede estar vacío.")
            return

        producto = restaurante.buscar_producto_por_codigo(codigo_producto)
        if not producto:
            print(f"✗ Error: No existe producto con código '{codigo_producto}'.")
            return

        print(f"✓ Producto encontrado: {producto.mostrar_informacion()}")

        try:
            cantidad = int(input("Ingrese la cantidad a vender: "))
        except ValueError:
            print("✗ Error: La cantidad debe ser un número entero válido.")
            return

        if cantidad <= 0:
            print("✗ Error: La cantidad debe ser mayor que cero.")
            return

        if producto.stock < cantidad:
            print(f"✗ Error: Stock insuficiente. Disponible: {producto.stock}, Solicitado: {cantidad}")
            return

        try:
            if restaurante.vender_producto(codigo_producto, identificacion_usuario, cantidad):
                print(f"\n✓ Venta realizada exitosamente.")
                print(f"  Usuario: {usuario.nombre}")
                print(f"  Producto: {producto.nombre}")
                print(f"  Cantidad: {cantidad}")
                print(f"  Precio unitario: ${producto.precio:.2f}")
                print(f"  Total: ${producto.precio * cantidad:.2f}")
                print(f"  Stock restante: {producto.stock}")
                print("  (Venta y stock guardados automáticamente en JSON)")
            else:
                print("✗ Error: No se pudo realizar la venta.")
        except ValueError as error:
            print(f"✗ Error: {error}")

    except Exception as error:
        print(f"✗ Error inesperado: {error}")


def listar_ventas(restaurante: Restaurante) -> None:
    """
    Lista todas las ventas registradas.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    ventas = restaurante.listar_ventas()

    if not ventas:
        print("\n℘ No hay ventas registradas.")
    else:
        print(f"\n{'=' * 100}")
        print(f"{'LISTADO DE TODAS LAS VENTAS':^100}")
        print(f"{'=' * 100}")
        for indice, informacion in enumerate(ventas, 1):
            print(f"{indice}. {informacion}")
        print(f"{'=' * 100}")
        print(f"Total de ventas: {restaurante.obtener_cantidad_ventas()}")


def consultar_ventas_usuario(restaurante: Restaurante) -> None:
    """
    Consulta todas las ventas realizadas por un usuario específico.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    try:
        identificacion = input("\nIngrese la identificación del usuario: ").strip()
        if not identificacion:
            print("✗ Error: La identificación no puede estar vacía.")
            return

        usuario = restaurante.buscar_usuario(identificacion)
        if not usuario:
            print(f"✗ Error: No existe usuario con identificación '{identificacion}'.")
            return

        ventas = restaurante.obtener_ventas_usuario(identificacion)

        if not ventas:
            print(f"\n℘ El usuario '{usuario.nombre}' no tiene ventas registradas.")
        else:
            print(f"\n{'=' * 100}")
            print(f"{'VENTAS DE ' + usuario.nombre.upper():^100}")
            print(f"{'=' * 100}")

            total_cantidad = 0
            total_monto = 0.0

            for indice, venta in enumerate(ventas, 1):
                producto = restaurante.buscar_producto_por_codigo(venta.producto_codigo)
                if producto:
                    monto = producto.precio * venta.cantidad
                    total_cantidad += venta.cantidad
                    total_monto += monto
                    print(f"{indice}. Producto: {producto.nombre} | Cantidad: {venta.cantidad} | "
                          f"Precio unitario: ${producto.precio:.2f} | Total: ${monto:.2f}")
                else:
                    print(f"{indice}. Código: {venta.producto_codigo} | Cantidad: {venta.cantidad} | "
                          f"(Producto no encontrado)")

            print(f"{'=' * 100}")
            print(f"Total de venta(s): {len(ventas)} | Cantidad total: {total_cantidad} | "
                  f"Monto total: ${total_monto:.2f}")

    except Exception as error:
        print(f"✗ Error inesperado: {error}")


def guardar_datos(restaurante: Restaurante) -> None:
    """
    Guarda todos los datos en archivos JSON.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    try:
        if restaurante.guardar_datos_a_archivo():
            print(f"\n✓ Todos los datos fueron guardados exitosamente en JSON.")
        else:
            print("\n✗ Error: No se pudieron guardar los datos.")
    except Exception as error:
        print(f"✗ Error inesperado al guardar: {error}")


def cargar_datos(restaurante: Restaurante) -> None:
    """
    Carga todos los datos desde archivos JSON.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante.
    """
    try:
        if restaurante.cargar_datos_desde_archivo():
            cantidad_productos = restaurante.obtener_cantidad_productos()
            cantidad_usuarios = restaurante.obtener_cantidad_usuarios()
            cantidad_ventas = restaurante.obtener_cantidad_ventas()
            print(f"\n✓ Datos cargados exitosamente desde JSON.")
            print(f"  Productos: {cantidad_productos}")
            print(f"  Usuarios: {cantidad_usuarios}")
            print(f"  Ventas: {cantidad_ventas}")
        else:
            print("\n✗ Error: No se pudieron cargar los datos.")
    except Exception as error:
        print(f"✗ Error inesperado al cargar: {error}")


def main() -> None:
    """
    Función principal que controla el flujo de la aplicación.
    Presenta el menú y ejecuta las operaciones solicitadas por el usuario.
    Carga automáticamente los datos del archivo al iniciar.
    """
    restaurante = Restaurante()

    print("\n" + "=" * 70)
    print(" " * 10 + "¡Bienvenido al Sistema de Restaurante!")
    print(" " * 15 + "Semana 11 - Ventas y Persistencia")
    print("=" * 70)
    print("Cargando datos desde archivos...")

    if restaurante.cargar_datos_desde_archivo():
        cantidad_productos = restaurante.obtener_cantidad_productos()
        cantidad_usuarios = restaurante.obtener_cantidad_usuarios()
        cantidad_ventas = restaurante.obtener_cantidad_ventas()

        mensajes = []
        if cantidad_productos > 0:
            mensajes.append(f"{cantidad_productos} producto(s)")
        if cantidad_usuarios > 0:
            mensajes.append(f"{cantidad_usuarios} usuario(s)")
        if cantidad_ventas > 0:
            mensajes.append(f"{cantidad_ventas} venta(s)")

        if mensajes:
            print(f"✓ Se cargaron: {', '.join(mensajes)}")
        else:
            print("℘ No se encontraron datos previos. Comenzando con colecciones vacías.")
    else:
        print("℘ No se encontraron archivos de datos. Comenzando con colecciones vacías.")

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-13): ").strip()

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
            realizar_venta(restaurante)

        elif opcion == "9":
            listar_ventas(restaurante)

        elif opcion == "10":
            consultar_ventas_usuario(restaurante)

        elif opcion == "11":
            guardar_datos(restaurante)

        elif opcion == "12":
            cargar_datos(restaurante)

        elif opcion == "13":
            print("\n¡Gracias por usar el Sistema de Restaurante! Hasta luego.")
            break

        else:
            print("✗ Error: Opción no válida. Por favor, seleccione una opción del 1 al 13.")


if __name__ == "__main__":
    main()

