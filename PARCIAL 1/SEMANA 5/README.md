# Sistema de Gestión de Restaurante - SEMANA 5

## 📌 Descripción de la Tarea

Esta tarea consiste en desarrollar un **sistema básico de gestión de restaurante** utilizando **Programación Orientada a Objetos (POO)** en Python. El objetivo principal es demostrar la comprensión e implementación de conceptos fundamentales como:

- **Identificadores descriptivos** en clases, variables, métodos y archivos
- **Tipos de datos básicos** y su aplicación correcta
- **Estructuras compuestas** como listas
- **Clases y objetos**
- **Importaciones entre módulos** en un proyecto estructurado

El sistema representa elementos clave de un restaurante: productos (platos, bebidas, etc.) y clientes registrados, gestionados a través de una clase principal que actúa como administrador del sistema.

---

## 🎯 Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py          # Clase Producto
│   └── cliente.py           # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py       # Clase Restaurante (gestor)
└── main.py                  # Punto de entrada del programa
```

---

## 💾 Tipos de Datos Básicos en Python

### ¿Qué son los tipos de datos?

Los **tipos de datos** definen el tipo de valor que puede almacenar una variable. Python es un lenguaje **dinámicamente tipado**, lo que significa que no necesitas declarar explícitamente el tipo, pero es recomendable usar **anotaciones de tipo** para mayor claridad y mantenibilidad del código.

En este proyecto utilizamos 4 tipos de datos básicos principales:

---

### 1️⃣ **Tipo `str` (String - Cadena de Texto)**

**Definición:** Almacena cadenas de caracteres (texto).

**Características:**
- Se define entre comillas simples `'` o dobles `"`
- Inmutable (no se puede modificar directamente)
- Puede contener números, letras, espacios y caracteres especiales

**Ejemplos en el Proyecto:**

```python
# En la clase Producto
nombre_producto: str = "Hornado"
descripcion_producto: str = "Cerdo asado con papas y maíz"

# En la clase Cliente
nombre_cliente: str = "Juan García"
correo_cliente: str = "juan.garcia@email.com"
telefono_cliente: str = "0987654321"

# En la clase Restaurante
nombre_restaurante: str = "Restaurante El Sabor"
ubicacion_restaurante: str = "Calle Principal 123, Cuenca"
```

**Operaciones comunes con strings:**
```python
# Concatenación
mensaje = nombre_cliente + " es un cliente valioso"

# Convertir a minúsculas
nombre_minuscula = nombre_cliente.lower()

# Longitud
cantidad_caracteres = len(nombre_cliente)

# Búsqueda (case-insensitive)
if nombre_cliente.lower() == "juan garcía":
    print("Cliente encontrado")
```

---

### 2️⃣ **Tipo `int` (Integer - Número Entero)**

**Definición:** Almacena números enteros sin decimales.

**Características:**
- Pueden ser positivos o negativos
- Se usan para contar, identificar o enumerar
- Ocupan menos memoria que otros tipos numéricos

**Ejemplos en el Proyecto:**

```python
# En la clase Producto
identificador_producto: int = 1

# En la clase Cliente
numero_cliente: int = 101

# Contadores en el Restaurante
total_productos: int = 4
total_clientes: int = 3
```

**Operaciones comunes con int:**
```python
# Aritmética básica
suma = numero_cliente + 10
resta = numero_cliente - 5
multiplicacion = identificador_producto * 2

# Comparaciones
if numero_cliente > 100:
    print("Cliente registrado")

# Incremento/Decremento
numero_cliente += 1
```

---

### 3️⃣ **Tipo `float` (Número Decimal)**

**Definición:** Almacena números decimales (con punto flotante).

**Características:**
- Exactitud limitada (pueden tener pequeños errores de precisión)
- Se usan para precios, medidas, porcentajes
- Se define con punto decimal `.`

**Ejemplos en el Proyecto:**

```python
# En la clase Producto
precio_producto: float = 18.50  # Precio en pesos
# Otros ejemplos:
precio_producto: float = 22.75
precio_producto: float = 4.50
precio_producto: float = 6.00
```

**Operaciones comunes con float:**
```python
# Aritmética con decimales
precio_total = precio_producto * cantidad
descuento = precio_producto * 0.10

# Redondeo
precio_formateado = round(precio_producto, 2)

# Formateo para mostrar
print(f"Precio: ${precio_producto:.2f}")  # Muestra: Precio: $18.50

# Comparaciones
if precio_producto > 15.00:
    print("Producto caro")
```

---

### 4️⃣ **Tipo `bool` (Boolean - Verdadero o Falso)**

**Definición:** Almacena valores lógicos: `True` (verdadero) o `False` (falso).

**Características:**
- Solo tiene dos valores posibles
- Se usa para estados, condiciones y banderas
- En Python: `True` y `False` (con mayúscula inicial)

**Ejemplos en el Proyecto:**

```python
# En la clase Producto
disponible: bool = True   # Producto disponible
disponible: bool = False  # Producto no disponible

# En la clase Cliente
cliente_activo: bool = True   # Cliente activo
cliente_activo: bool = False  # Cliente inactivo
```

**Operaciones comunes con bool:**
```python
# Asignación directa
estado = True
estado = False

# Resultado de comparaciones
es_disponible = precio_producto > 0
es_valido = numero_cliente > 0

# Operadores lógicos
if disponible and cliente_activo:
    print("Puede realizar compra")

if not disponible or not cliente_activo:
    print("No puede comprar")

# Cambiar estado
producto.disponible = not producto.disponible  # Invierte el valor
```

---

## 📦 Listas (Arrays) - Estructuras Compuestas

### ¿Qué es una Lista?

Una **lista** es una estructura de datos que almacena múltiples elementos en una **secuencia ordenada**. Es el tipo de dato compuesto más utilizado en Python.

**Características:**
- Orden: Los elementos mantienen su posición (indexados desde 0)
- Mutabilidad: Pueden modificarse después de la creación
- Heterogeneidad: Pueden contener diferentes tipos de datos
- Sintaxis: Se definen con corchetes `[]`

### Sintaxis Básica

```python
# Lista vacía
lista_vacia = []

# Lista con elementos
numeros = [1, 2, 3, 4, 5]
nombres = ["Juan", "María", "Carlos"]
mixta = [1, "texto", 3.14, True]

# Con anotación de tipo (más recomendado)
lista_productos: list[Producto] = []
lista_clientes: list[Cliente] = []
lista_numeros: list[int] = [1, 2, 3, 4, 5]
```

### Indexación (Acceso a Elementos)

```python
numeros = [10, 20, 30, 40, 50]

# Acceso por índice (comienza en 0)
primer_numero = numeros[0]      # 10
segundo_numero = numeros[1]     # 20
ultimo_numero = numeros[-1]     # 50 (desde el final)

# Acceso a rango
primeros_tres = numeros[0:3]    # [10, 20, 30]
ultimos_dos = numeros[-2:]      # [40, 50]
```

### Operaciones Comunes en Listas

#### **1. Agregar elementos**

```python
# append(): Agrega un elemento al final
lista_productos.append(producto_1)
lista_productos.append(producto_2)

# insert(): Inserta en una posición específica
lista_productos.insert(0, nuevo_producto)  # Al inicio

# extend(): Agrega múltiples elementos
lista_productos.extend([producto_3, producto_4])
```

#### **2. Eliminar elementos**

```python
# remove(): Elimina por valor
lista_productos.remove(producto_1)

# pop(): Elimina por índice
ultimo = lista_productos.pop()      # Elimina y retorna el último
elemento = lista_productos.pop(0)   # Elimina y retorna el primero

# clear(): Vacía la lista
lista_productos.clear()
```

#### **3. Obtener información**

```python
# len(): Cantidad de elementos
cantidad = len(lista_productos)     # 4

# in: Verificar si existe
existe = producto_1 in lista_productos

# index(): Obtener posición
posicion = lista_productos.index(producto_1)

# count(): Contar ocurrencias
cantidad_duplicadas = lista_productos.count(producto_1)
```

#### **4. Recorrer elementos**

```python
# Con for loop (recomendado)
for producto in lista_productos:
    print(producto.nombre_producto)

# Con índice
for i in range(len(lista_productos)):
    print(lista_productos[i].nombre_producto)

# Con enumerate (cuando necesitas índice y valor)
for i, producto in enumerate(lista_productos, 1):
    print(f"{i}. {producto.nombre_producto}")
```

#### **5. Buscar en listas**

```python
# Búsqueda simple
for producto in lista_productos:
    if producto.nombre_producto.lower() == "hornado":
        print("Producto encontrado")

# Con función personalizada
def buscar_producto(nombre_busqueda: str) -> Producto:
    for producto in lista_productos:
        if producto.nombre_producto.lower() == nombre_busqueda.lower():
            return producto
    return None
```

### Ejemplos en el Proyecto

```python
# Clase Restaurante
class Restaurante:
    def __init__(self, nombre_restaurante: str, ubicacion_restaurante: str):
        # Listas para almacenar múltiples productos y clientes
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []
    
    # Método para agregar producto a la lista
    def agregar_producto(self, producto: Producto) -> None:
        self.lista_productos.append(producto)
    
    # Método para agregar cliente a la lista
    def agregar_cliente(self, cliente: Cliente) -> None:
        self.lista_clientes.append(cliente)
    
    # Método para obtener productos
    def obtener_productos(self) -> list[Producto]:
        return self.lista_productos
    
    # Método para contar clientes
    def contar_clientes(self) -> int:
        return len(self.lista_clientes)
```

---

## 🔄 Anotaciones de Tipo (Type Hints)

Las **anotaciones de tipo** mejoran la legibilidad y permiten detectar errores tempranamente.

**Ejemplos en el proyecto:**

```python
# Atributos con tipo
nombre_producto: str
precio_producto: float
disponible: bool
numero_cliente: int

# Parámetros de función con tipo
def agregar_producto(self, producto: Producto) -> None:
    self.lista_productos.append(producto)

# Retorno de función con tipo
def obtener_precio(self) -> float:
    return self.precio_producto

# Listas con tipo
lista_productos: list[Producto] = []
numeros: list[int] = [1, 2, 3]
```

---

## 📝 Ejemplo Práctico Integrado

```python
# Crear un producto (usando todos los tipos de datos)
producto = Producto(
    identificador_producto=1,           # int (ID único)
    nombre_producto="Hornado",          # str (nombre)
    descripcion_producto="Cerdo asado", # str (descripción)
    precio_producto=18.50,              # float (precio)
    disponible=True                     # bool (estado)
)

# Crear una lista de clientes
clientes: list[Cliente] = []

# Agregar clientes a la lista
cliente1 = Cliente(
    numero_cliente=101,                 # int
    nombre_cliente="Juan",              # str
    correo_cliente="juan@email.com",    # str
    telefono_cliente="0987654321",      # str
    cliente_activo=True                 # bool
)

clientes.append(cliente1)

# Recorrer la lista y mostrar información
for cliente in clientes:
    print(f"Cliente {cliente.numero_cliente}: {cliente.nombre_cliente}")
```

---

## 🎓 Conceptos Clave Demostrados

| Concepto | Ejemplo |
|----------|---------|
| **Identificadores descriptivos** | `nombre_producto`, `numero_cliente`, `lista_productos` |
| **Tipo str** | Nombres, correos, descripciones |
| **Tipo int** | IDs, números de cliente, contadores |
| **Tipo float** | Precios, montos |
| **Tipo bool** | Estados de disponibilidad y de clientes |
| **Listas** | `lista_productos`, `lista_clientes` |
| **Clases** | `Producto`, `Cliente`, `Restaurante` |
| **Objetos** | Instancias de Producto, Cliente, Restaurante |
| **Métodos** | `agregar_producto()`, `mostrar_clientes()` |
| **Importaciones** | Entre módulos (modelos y servicios) |

---

## ✅ Requisitos Cumplidos

- ✓ Estructura modular del proyecto
- ✓ Uso correcto de 4 tipos de datos (str, int, float, bool)
- ✓ Listas para almacenar múltiples objetos
- ✓ Anotaciones de tipo en atributos y métodos
- ✓ Identificadores descriptivos (PascalCase y snake_case)
- ✓ Clases con constructores `__init__()`
- ✓ Método `__str__()` para representación textual
- ✓ Importaciones correctas entre módulos
- ✓ Demostración de funcionalidades en `main.py`

---

## 🚀 Cómo Ejecutar

```bash
# Posicionarse en la carpeta del proyecto
cd restaurante_app

# Ejecutar el programa principal
python main.py
```

---

**Autor:** Sistema de Gestión de Restaurante - Programación Orientada a Objetos  
**Fecha:** Semana 5 - PARCIAL 1  
**Institución:** Universidad  
**Docente:** Programación POO

