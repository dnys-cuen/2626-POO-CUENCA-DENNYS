# Restaurante App

**Autor**: Dennys Cuenca

## Descripción del Sistema
El sistema `restaurante_app` es una aplicación desarrollada en Python utilizando el paradigma de Programación Orientada a Objetos (POO). Su propósito es modelar y administrar los productos de un restaurante, clasificándolos en comidas (platillos) y bebidas.

## Estructura del Proyecto
El proyecto está estructurado de manera modular para separar responsabilidades:
- `modelos/`: Contiene las clases que representan las entidades del negocio (Producto, Platillo, Bebida).
- `servicios/`: Contiene la lógica de administración y agrupación de los productos (Restaurante).
- `main.py`: Punto de entrada del programa donde se instancian los objetos y se ejecutan las funcionalidades.

## Principios de POO Aplicados
1. **Herencia**: La relación de herencia se aplica entre la clase padre `Producto` y las clases hijas `Platillo` y `Bebida`. Ambas clases hijas reutilizan los atributos comunes (`nombre`, `precio`, `disponibilidad`) y métodos a través de la función `super()`.
2. **Encapsulación**: El atributo `precio` de la clase `Producto` ha sido encapsulado utilizando un doble guion bajo (`__precio`). Se crearon los métodos `obtener_precio()` y `cambiar_precio()` para acceder y modificar su valor, incluyendo una validación para evitar que el precio sea negativo o cero.
3. **Polimorfismo**: Se implementa en el método `mostrar_informacion()`. Mientras que la clase padre lo define genéricamente, las clases hijas lo sobrescriben para mostrar detalles específicos (calorías para platillos y volumen para bebidas). Al recorrer la lista de productos en el menú, Python sabe automáticamente qué versión del método ejecutar dependiendo del tipo de objeto.

## Reflexión sobre la POO en proyectos modulares
Aplicar principios de POO en proyectos Python modulares es fundamental porque mejora el mantenimiento y la escalabilidad del código. La herencia evita la duplicación de código; la encapsulación protege la integridad de los datos evitando modificaciones indebidas desde el exterior; y el polimorfismo permite diseñar sistemas flexibles donde un mismo llamado a un método se adapta al tipo de objeto que lo recibe. Esta organización modular prepara las bases para aplicaciones más grandes y complejas.
