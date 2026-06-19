# Sistema de Gestión de Restaurante

## Descripción General

Este es un sistema básico de gestión de restaurante desarrollado con **Programación Orientada a Objetos (POO)** en Python. El objetivo del proyecto es demostrar:

- Organización de proyectos en módulos
- Separación de responsabilidades entre clases
- Comunicación entre archivos mediante importaciones
- Aplicación de conceptos fundamentales de POO

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py      # Clase que representa platos y bebidas
│   └── cliente.py       # Clase que representa clientes del restaurante
├── servicios/
│   ├── __init__.py
│   └── restaurante.py   # Clase que gestiona el restaurante
└── main.py              # Punto de arranque del programa
```

## Clases del Sistema

### 1. **Clase Producto** (`modelos/producto.py`)

Representa un plato, bebida o producto disponible en el restaurante.

**Atributos:**
- `id` (int): Identificador único del producto
- `nombre` (str): Nombre del producto
- `categoria` (str): Categoría (Plato Fuerte, Entrada, Bebida, Postre, etc.)
- `precio` (float): Precio del producto
- `disponible` (bool): Estado de disponibilidad del producto

**Métodos:**
- `obtener_precio_formateado()`: Retorna el precio con formato de currency
- `cambiar_disponibilidad(disponible)`: Modifica el estado disponible
- `__str__()`: Imprime representación formateada del producto

### 2. **Clase Cliente** (`modelos/cliente.py`)

Representa un cliente que realiza pedidos en el restaurante.

**Atributos:**
- `id` (int): Identificador único del cliente
- `nombre` (str): Nombre completo del cliente
- `email` (str): Correo electrónico del cliente
- `telefono` (str): Número de teléfono del cliente
- `pedidos_realizados` (list): Historial de pedidos del cliente

**Métodos:**
- `registrar_pedido(id_pedido, total)`: Registra un nuevo pedido
- `obtener_total_gastado()`: Calcula el gasto total del cliente
- `obtener_cantidad_pedidos()`: Retorna la cantidad de pedidos realizados
- `__str__()`: Imprime información completa del cliente

### 3. **Clase Restaurante** (`servicios/restaurante.py`)

Gestiona las operaciones principales del sistema de restaurante.

**Atributos:**
- `nombre` (str): Nombre del restaurante
- `ubicacion` (str): Ubicación del restaurante
- `productos` (list): Lista de productos disponibles
- `clientes` (list): Lista de clientes registrados
- `pedidos` (list): Historial de todos los pedidos
- `contador_pedidos` (int): Contador para generar IDs únicos

**Métodos principales:**
- `agregar_producto(producto)`: Agrega un producto al menú
- `registrar_cliente(cliente)`: Registra un nuevo cliente
- `realizar_pedido(id_cliente, ids_productos)`: Procesa un pedido
- `buscar_producto_por_id(id_producto)`: Busca un producto
- `buscar_cliente_por_id(id_cliente)`: Busca un cliente
- `mostrar_menu()`: Muestra el menú disponible
- `mostrar_clientes()`: Muestra todos los clientes
- `mostrar_historial_pedidos()`: Muestra el historial de pedidos
- `obtener_total_ventas()`: Calcula el total de ventas
- `obtener_resumen()`: Retorna un resumen del restaurante
- `__str__()`: Imprime información básica del restaurante

## Cómo Ejecutar el Programa

1. **Navegar a la carpeta del proyecto:**
   ```bash
   cd restaurante_app
   ```

2. **Ejecutar el archivo principal:**
   ```bash
   python main.py
   ```

## Demostración del Funcionamiento

El archivo `main.py` ejecuta una demostración completa que incluye:

1. **Creación del restaurante** - Instancia la clase Restaurante
2. **Agregación de productos** - Crea y agrega 5 productos al menú
3. **Registro de clientes** - Crea y registra 3 clientes
4. **Mostrar menú** - Muestra todos los productos disponibles
5. **Procesamiento de pedidos** - Realiza 4 pedidos de diferentes clientes
6. **Información de clientes** - Muestra datos de cada cliente registrado
7. **Historial de pedidos** - Muestra todos los pedidos realizados
8. **Resumen del sistema** - Muestra estadísticas generales
9. **Búsquedas específicas** - Busca un cliente y un producto por ID

## Conceptos de POO Aplicados

✓ **Clases y Objetos**: Se crean objetos de cada clase
✓ **Constructores (__init__)**: Inicialización de atributos
✓ **Atributos**: Variables que almacenan el estado de los objetos
✓ **Métodos**: Funciones que realizan operaciones sobre los objetos
✓ **Encapsulación**: Datos protegidos dentro de las clases
✓ **Método __str__()**: Representación en texto de los objetos
✓ **Importaciones Between Modules**: Comunicación entre archivos
✓ **Responsabilidad Única**: Cada clase tiene un propósito específico

## Ejemplos de Uso

### Crear un producto
```python
from modelos.producto import Producto

hamburguesa = Producto(101, "Hamburguesa", "Plato Fuerte", 12.50)
print(hamburguesa)  # [101] Hamburguesa (Plato Fuerte) - $12.50 - Disponible
```

### Crear un cliente
```python
from modelos.cliente import Cliente

cliente = Cliente(1001, "Juan Pérez", "juan@email.com", "555-1234")
print(cliente)  # [1001] Juan Pérez | Email: juan@email.com | ...
```

### Gestionar el restaurante
```python
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

restaurante = Restaurante("Mi Restaurante", "Calle Principal")
restaurante.agregar_producto(hamburguesa)
restaurante.registrar_cliente(cliente)
restaurante.realizar_pedido(1001, [101])
restaurante.mostrar_menu()
```

## Extensiones Futuras

El sistema puede extenderse con:
- Clase `Pedido` para representar pedidos individuales
- Sistema de calificaciones y comentarios
- Métodos de pago
- Inventario de ingredientes
- Reportes y estadísticas más detalladas
- Base de datos persistente

---

**Nota**: Este proyecto es una demostración educativa de conceptos básicos de POO. No es una aplicación de producción completa.

