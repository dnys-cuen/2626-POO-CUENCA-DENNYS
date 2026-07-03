from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def main():
    # 1. Crear objetos de tipo Platillo
    platillo1 = Platillo("Encebollado Mixto", 4.50, True, 600)
    platillo2 = Platillo("Churrasco Ecuatoriano", 5.50, True, 850)

    # 2. Crear objetos de tipo Bebida
    bebida1 = Bebida("Jugo de Mora", 1.50, True, 400)
    bebida2 = Bebida("Limonada Imperial", 2.00, False, 500)

    # 3. Demostrar encapsulación y validación
    print("--- Demostrando Encapsulación y Validación ---")
    print(f"Precio original de {platillo1.nombre}: ${platillo1.obtener_precio():.2f}")
    
    print("Intentando cambiar precio a -2.50...")
    platillo1.cambiar_precio(-2.50) # Debe fallar por validación
    
    print("Cambiando precio a 4.75...")
    platillo1.cambiar_precio(4.75)  # Debe ser exitoso
    print(f"Nuevo precio de {platillo1.nombre}: ${platillo1.obtener_precio():.2f}\n")

    # 4. Crear clase de servicio Restaurante
    mi_restaurante = Restaurante()

    # 5. Agregar objetos a la lista del servicio
    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)

    # 6. Mostrar información (Demostración de Polimorfismo)
    mi_restaurante.mostrar_menu()

if __name__ == "__main__":
    main()
