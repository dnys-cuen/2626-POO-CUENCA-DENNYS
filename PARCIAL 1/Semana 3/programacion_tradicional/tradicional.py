# Programa: Registro de Mascotas - Programación Tradicional
# Este programa registra y muestra información de mascotas sin usar clases ni objetos

# Variable global para almacenar las mascotas
mascotas = []


def registrar_mascota():
    """
    Función para registrar una nueva mascota solicitando datos por teclado.
    """
    print("\n" + "="*50)
    print("REGISTRAR NUEVA MASCOTA")
    print("="*50)

    # Solicitar datos del usuario
    nombre = input("Nombre de la mascota: ").strip()

    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    tipo = input("Tipo de mascota (perro, gato, pájaro, otro): ").strip()
    edad = input("Edad (en años): ").strip()

    # Validar que la edad sea un número
    try:
        edad = int(edad)
    except ValueError:
        print("Error: La edad debe ser un número.")
        return

    raza = input("Raza: ").strip()
    color = input("Color: ").strip()

    # Crear un diccionario con la información de la mascota
    mascota = {
        "nombre": nombre,
        "tipo": tipo,
        "edad": edad,
        "raza": raza,
        "color": color
    }

    # Agregar la mascota a la lista
    mascotas.append(mascota)
    print("\n✓ Mascota registrada exitosamente!")


def mostrar_mascota(index):
    """
    Función para mostrar la información de una mascota específica.

    Args:
        index: Índice de la mascota en la lista
    """
    if index < 0 or index >= len(mascotas):
        print("Error: Índice inválido.")
        return

    mascota = mascotas[index]

    print("\n" + "-"*50)
    print(f"Mascota #{index + 1}")
    print("-"*50)
    print(f"Nombre:     {mascota['nombre']}")
    print(f"Tipo:       {mascota['tipo']}")
    print(f"Edad:       {mascota['edad']} años")
    print(f"Raza:       {mascota['raza']}")
    print(f"Color:      {mascota['color']}")
    print("-"*50)


def mostrar_todas_mascotas():
    """
    Función para mostrar la información de todas las mascotas registradas.
    """
    if len(mascotas) == 0:
        print("\n⚠ No hay mascotas registradas aún.")
        return

    print("\n" + "="*50)
    print("LISTADO DE MASCOTAS REGISTRADAS")
    print("="*50)
    print(f"Total de mascotas: {len(mascotas)}\n")

    for index, mascota in enumerate(mascotas, 1):
        print(f"{index}. {mascota['nombre']}")
        print(f"   Tipo: {mascota['tipo']}")
        print(f"   Edad: {mascota['edad']} años")
        print(f"   Raza: {mascota['raza']}")
        print(f"   Color: {mascota['color']}")
        print()


def buscar_mascota():
    """
    Función para buscar una mascota por nombre.
    """
    nombre_buscar = input("\nIngrese el nombre de la mascota a buscar: ").strip().lower()

    encontradas = []
    for index, mascota in enumerate(mascotas):
        if mascota['nombre'].lower() == nombre_buscar:
            encontradas.append(index)

    if len(encontradas) == 0:
        print(f"\n⚠ No se encontró ninguna mascota con el nombre '{nombre_buscar}'.")
    else:
        print(f"\n✓ Se encontró(aron) {len(encontradas)} mascota(s):")
        for index in encontradas:
            mostrar_mascota(index)


def menu_principal():
    """
    Función para mostrar el menú principal e interactuar con el usuario.
    """
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE REGISTRO DE MASCOTAS")
        print("="*50)
        print("1. Registrar nueva mascota")
        print("2. Ver todas las mascotas")
        print("3. Buscar mascota por nombre")
        print("4. Ver mascota específica")
        print("5. Salir")
        print("="*50)

        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            registrar_mascota()

        elif opcion == "2":
            mostrar_todas_mascotas()

        elif opcion == "3":
            buscar_mascota()

        elif opcion == "4":
            if len(mascotas) == 0:
                print("\n⚠ No hay mascotas registradas aún.")
            else:
                mostrar_todas_mascotas()
                try:
                    numero = int(input("Ingrese el número de la mascota: "))
                    mostrar_mascota(numero - 1)
                except ValueError:
                    print("Error: Ingrese un número válido.")

        elif opcion == "5":
            print("\n¡Gracias por usar el Sistema de Registro de Mascotas!")
            print("="*50)
            break

        else:
            print("\n⚠ Opción inválida. Por favor, intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()

