# archivo: main.py
# Crea objetos de la clase Mascota y demuestra el uso de métodos

from mascota import Mascota


def main():
    # Crear al menos dos objetos de Mascota
    mascota1 = Mascota("Firulais", "Perro", 4)
    mascota2 = Mascota("Misu", "Gato", 3)

    # Mostrar información y ejecutar el sonido de cada mascota
    mascotas = [mascota1, mascota2]

    print("\n== DEMOSTRACIÓN: Programación Orientada a Objetos ==\n")
    for i, m in enumerate(mascotas, 1):
        print(f"Mascota #{i}")
        m.mostrar_informacion()
        m.hacer_sonido()


if __name__ == "__main__":
    main()

