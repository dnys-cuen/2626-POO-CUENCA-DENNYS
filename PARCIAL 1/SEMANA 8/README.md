# Sistema de Gestión de Restaurante

**Estudiante:** Dennys Silvano Cuenca Japón

## Descripción del Sistema

El Sistema de Gestión de Restaurante es una aplicación de consola desarrollada en Python que demuestra la aplicación de **Programación Orientada a Objetos (POO)** y los principios **SOLID**. El sistema permite registrar y listar productos, bebidas y clientes mediante un menú interactivo intuitivo.

La aplicación evidencia cómo un proyecto bien estructurado mantiene la cohesión entre clases, implementa relaciones de herencia correctas y utiliza polimorfismo para tratar objetos de diferentes tipos de manera uniforme, sin necesidad de condicionales discriminatorios.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py          # Inicializador del paquete modelos
│   ├── producto.py          # Clase base Producto
│   ├── bebida.py            # Clase Bebida (hereda de Producto)
│   └── cliente.py           # Clase Cliente
├── servicios/
│   ├── __init__.py          # Inicializador del paquete servicios
│   └── restaurante.py       # Clase Restaurante (servicio principal)
└── main.py                  # Punto de entrada de la aplicación
```

## Responsabilidad de Cada Clase

### `modelos/producto.py` - Clase Producto
**Responsabilidad:** Representar un producto general del restaurante con su información básica.

- **Atributos:**
  - `codigo`: Identificador único del producto
  - `nombre`: Nombre descriptivo del producto
  - `categoria`: Clasificación del producto
  - `precio`: Precio en unidades monetarias

- **Métodos:**
  - `mostrar_informacion()`: Retorna la información formateada del producto

### `modelos/bebida.py` - Clase Bebida
**Responsabilidad:** Representar una bebida del restaurante extendiendo la funcionalidad de Producto.

- **Herencia:** Extiende de `Producto`
- **Atributos adicionales:**
  - `tamaño`: Tamaño de la bebida (pequeño, mediano, grande)
  - `tipo_envase`: Tipo de contenedor (vaso, botella, lata)

- **Métodos:**
  - `mostrar_informacion()`: Sobrescribe el método de Producto para incluir información específica de bebidas

### `modelos/cliente.py` - Clase Cliente
**Responsabilidad:** Representar un cliente registrado en el sistema.

- **Atributos:**
  - `identificacion`: Número de identificación único del cliente
  - `nombre`: Nombre completo del cliente
  - `correo`: Correo electrónico del cliente

- **Métodos:**
  - `mostrar_informacion()`: Retorna la información formateada del cliente

### `servicios/restaurante.py` - Clase Restaurante
**Responsabilidad:** Administrar las colecciones de productos y clientes, validando registros duplicados.

- **Atributos:**
  - `productos`: Lista de objetos `Producto` (incluyendo `Bebida`)
  - `clientes`: Lista de objetos `Cliente`

- **Métodos principales:**
  - `registrar_producto()`: Agrega un producto o bebida validando código único
  - `registrar_cliente()`: Agrega un cliente validando identificación única
  - `listar_productos()`: Retorna lista de información de todos los productos
  - `listar_clientes()`: Retorna lista de información de todos los clientes
  - `_codigo_producto_existe()`: Valida unicidad de código
  - `_identificacion_cliente_existe()`: Valida unicidad de identificación

### `main.py` - Módulo Principal
**Responsabilidad:** Coordinar la interfaz de usuario y el flujo de la aplicación.

- **Funciones:**
  - `mostrar_menu()`: Presenta el menú de opciones
  - `registrar_producto()`: Solicita datos y crea objeto Producto
  - `registrar_bebida()`: Solicita datos y crea objeto Bebida
  - `registrar_cliente()`: Solicita datos y crea objeto Cliente
  - `listar_productos()`: Muestra todos los productos registrados
  - `listar_clientes()`: Muestra todos los clientes registrados
  - `main()`: Controla el flujo general de la aplicación

## Relación entre Producto y Bebida

La relación entre `Producto` y `Bebida` demuestra una correcta implementación de herencia:

- **Producto** es la clase base que define los atributos y métodos comunes a todos los productos
- **Bebida** es una clase especializada que hereda de `Producto` y agrega atributos específicos
- Ambas clases pueden almacenarse en una **única lista** de productos sin necesidad de listas separadas
- Durante el listado, se utiliza **polimorfismo** para llamar `mostrar_informacion()` en cada objeto
- Cada objeto responde con su propia implementación del método, sin condicionales discriminatorios

Este diseño permite **agregar nuevas clases hijas en el futuro** (como `Postre`, `Entrada`, etc.) sin modificar la lógica del servicio.

## Principios SOLID Aplicados

### 1. S - Responsabilidad Única (Single Responsibility Principle)

Cada clase tiene una única responsabilidad bien definida:

- `Producto`: Representa datos comunes de un producto
- `Bebida`: Extiende Producto con información específica de bebidas
- `Cliente`: Representa datos de un cliente
- `Restaurante`: Administra colecciones y validaciones
- `main.py`: Coordina la interfaz de usuario

### 2. O - Abierto/Cerrado (Open/Closed Principle)

El sistema está abierto para extensión pero cerrado para modificación:

- La clase `Bebida` extiende `Producto` sin modificar su código
- Se pueden crear nuevas clases hijas (ej. `Postre`, `Entrada`) sin cambiar el servicio
- El método `registrar_producto()` acepta cualquier instancia de `Producto` o sus subclases
- La clase `Restaurante` no necesita cambios para soportar nuevos tipos de productos

### 3. L - Sustitución de Liskov (Liskov Substitution Principle)

Los objetos `Bebida` pueden ser utilizados en lugar de objetos `Producto` sin causar problemas:

- `registrar_producto()` acepta tanto `Producto` como `Bebida`
- `listar_productos()` itera sobre productos de cualquier tipo usando el método común `mostrar_informacion()`
- No hay condicionales `isinstance()` que discriminen el tipo de objeto
- El comportamiento es consistente y predecible

### 4. I - Segregación de Interfaz (Interface Segregation Principle)

*Aplicado de forma conceptual:*
- Las clases exponen solo los métodos relevantes para su contexto
- No hay métodos innecesarios o fuera de lugar en ninguna clase

### 5. D - Inversión de Dependencias (Dependency Inversion Principle)

*Aplicado de forma conceptual:*
- Las dependencias se inyectan naturalmente a través de los parámetros
- El módulo `main.py` trabaja con abstracciones (clases base) más que con implementaciones concretas

## Instrucciones de Ejecución

### Requisitos
- Python 3.7 o superior

### Pasos para ejecutar

1. **Navegar a la carpeta del proyecto:**
   ```bash
   cd restaurante_app
   ```

2. **Ejecutar el programa:**
   ```bash
   python main.py
   ```

3. **Interactuar con el menú:**
   - Seleccione opciones del 1 al 6
   - Ingrese los datos solicitados
   - El sistema validará y registrará la información
   - Seleccione 6 para salir

### Ejemplo de uso

```
==================================================
        SISTEMA DE RESTAURANTE
==================================================
1. Registrar producto
2. Registrar bebida
3. Registrar cliente
--------------------------------------------------
4. Listar productos
5. Listar clientes
--------------------------------------------------
6. Salir
==================================================
Seleccione una opción: 1
Ingrese el código del producto: P001
Ingrese el nombre del producto: Hamburguesa
Ingrese la categoría del producto: Comida Rápida
Ingrese el precio del producto: 8.99

✓ Producto 'Hamburguesa' registrado exitosamente.
```

## Reflexión sobre Diseño Mantenible

### ¿Por qué es importante diseñar proyectos mantenibles?

1. **Escalabilidad:** Un proyecto bien estructurado permite agregar nuevas funcionalidades sin refactorizar código existente.

2. **Reutilización:** Cuando cada clase tiene responsabilidad única, es fácil reutilizar componentes en otros proyectos.

3. **Testabilidad:** Clases independientes con responsabilidades claras son más fáciles de probar unitariamente.

4. **Colaboración:** En equipos de trabajo, un código bien organizado permite que múltiples desarrolladores trabajen simultáneamente sin conflictos.

5. **Debugging:** Cuando un error ocurre, es más fácil localizarlo si cada componente tiene una tarea específica.

6. **Mantenimiento a largo plazo:** Futuros desarrolladores comprenderán rápidamente la estructura sin necesidad de documentación extensiva.

### Aplicación en este proyecto

En el Sistema de Gestión de Restaurante:

- Es trivial agregar una nueva categoría de producto (ej. `Postre` que hereda de `Producto`)
- El método `listar_productos()` funcionará automáticamente con nuevas clases sin cambios
- Cada desarrollador puede trabajar en una clase específica sin afectar a otras
- Los errores de validación están centralizados en la clase `Restaurante`
- Las solicitudes de usuario están aisladas en funciones específicas dentro de `main.py`

## Conclusión

Este proyecto demuestra que la Programación Orientada a Objetos, cuando se aplica correctamente con los principios SOLID, produce código que es:

- **Mantenible:** Fácil de entender y modificar
- **Extensible:** Preparado para crecer sin grandes refactorizaciones
- **Robusto:** Con validaciones en el lugar adecuado
- **Profesional:** Seguidor de estándares y convenciones

El resultado es un sistema que no solo funciona, sino que proporciona una base sólida para futuros desarrollos.

---

**Fecha:** Semana 8 - 2026  
**Asignatura:** Programación Orientada a Objetos  
**Docente:** Universidad de la Especialización Académica

