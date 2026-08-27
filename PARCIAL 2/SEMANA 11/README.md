# Sistema de Restaurante - Semana 11

## Descripción General

Este proyecto es una evolución de la aplicación de gestión de restaurante desarrollada en semanas anteriores. La Semana 11 incorpora un nuevo componente fundamental: **la gestión de ventas** que relacionan usuarios con productos, junto con un control de stock y persistencia completa de datos.

El sistema permite:
- Registrar y gestionar productos con control de stock
- Registrar y gestionar usuarios
- Realizar ventas que relacionan un usuario con un producto
- Consultar ventas por usuario
- Persistir productos, usuarios y ventas en archivos JSON

## Estructura del Proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```

## Responsabilidad de Cada Componente

### Modelos

#### `modelos/producto.py`
Representa un producto del restaurante con:
- **Atributos**: código, nombre, categoría, precio, stock
- **Métodos principales**:
  - `vender(cantidad)`: Disminuye el stock si hay disponibilidad
  - `mostrar_informacion()`: Retorna información formateada
  - `a_diccionario()`: Convierte un producto a diccionario para JSON

#### `modelos/usuario.py`
Representa un usuario del restaurante con:
- **Atributos**: identificación, nombre, correo
- **Métodos principales**:
  - `mostrar_informacion()`: Retorna información formateada
  - `a_diccionario()`: Convierte un usuario a diccionario para JSON

#### `modelos/venta.py`
Representa una venta (relación usuario-producto) con:
- **Atributos**: usuario_id, producto_codigo, cantidad
- **Métodos principales**:
  - `a_diccionario()`: Convierte una venta a diccionario para JSON
  - `mostrar_informacion()`: Retorna información formateada

### Servicios

#### `servicios/archivo_servicio.py`
Gestiona la persistencia JSON con métodos para:
- **Guardar**: `guardar_productos()`, `guardar_usuarios()`, `guardar_ventas()`
- **Cargar**: `cargar_productos()`, `cargar_usuarios()`, `cargar_ventas()`
- **Manejo de excepciones**: FileNotFoundError, json.JSONDecodeError, PermissionError, KeyError, ValueError

#### `servicios/restaurante.py`
Administra la lógica de negocio y las colecciones:
- **Gestión de productos**: registrar, buscar, actualizar, eliminar, listar
- **Gestión de usuarios**: registrar, buscar, listar
- **Gestión de ventas**: 
  - `vender_producto()`: Registra una venta validando usuario, producto, cantidad y stock
  - `obtener_ventas_usuario()`: Filtra ventas por usuario
  - `listar_ventas()`: Retorna todas las ventas
- **Persistencia**: cargar y guardar datos desde/hacia JSON

### Punto de Entrada

#### `main.py`
Coordina la interacción con el usuario mediante:
- Menú principal con 13 opciones
- Funciones específicas para cada operación
- Manejo de entrada/salida de datos
- Validación de datos antes de llamar al servicio

## Funcionamiento de Stock y Ventas

### Relación Usuario + Producto → Venta

```
1. Usuario registrado en el sistema
2. Producto existente con stock disponible
3. Usuario solicita compra
4. Sistema valida:
   - Usuario existe
   - Producto existe
   - Cantidad es válida (> 0)
   - Stock es suficiente
5. Si todo es válido:
   - Se crea objeto Venta
   - Se agrega a la colección de ventas
   - Se disminuye el stock del producto
   - Se guardan ventas.json y productos.json
6. Si no es válido:
   - Se rechaza la operación
   - No se modifica ningún dato
```

### Control de Stock

- **Al registrar un producto**: se especifica stock inicial
- **Al realizar una venta**: se valida que exista stock suficiente
- **Después de una venta exitosa**: se disminuye automáticamente
- **Stock nunca es negativo**: se valida antes de restar

### Ejemplo de Venta

```
Antes de vender:
├── Producto: Hamburguesa
├── Stock: 10
├── Usuario: Juan Pérez

Acción: Vender 2 hamburguesas a Juan Pérez

Después de vender:
├── Producto: Hamburguesa
├── Stock: 8
├── Venta registrada: usuario_id=123, producto_codigo=HAMBURGUESA, cantidad=2
```

## Persistencia en JSON

### Estructura de Archivos

#### `datos/productos.json`
```json
[
    {
        "codigo": "HAMBURGUESA",
        "nombre": "Hamburguesa Clásica",
        "categoria": "Platos Principales",
        "precio": 12.50,
        "stock": 8
    }
]
```

#### `datos/usuarios.json`
```json
[
    {
        "identificacion": "123456789",
        "nombre": "Juan Pérez",
        "correo": "juan@email.com"
    }
]
```

#### `datos/ventas.json`
```json
[
    {
        "usuario_id": "123456789",
        "producto_codigo": "HAMBURGUESA",
        "cantidad": 2
    }
]
```

### Proceso de Persistencia

1. **Conversión a diccionarios**: Cada objeto implementa `a_diccionario()`
2. **Serialización JSON**: Se usa `json.dump()` con UTF-8
3. **Lectura desde archivo**: Se usa `json.load()`
4. **Reconstrucción de objetos**: Se crean instancias a partir de diccionarios
5. **Validación**: Se comprueban claves requeridas y tipos de datos
6. **Manejo de errores**: Se controlan excepciones específicas

### Cuándo se Guardan los Datos

- **Productos**: Después de registrar, actualizar o eliminar
- **Usuarios**: Después de registrar
- **Ventas**: Después de realizar una venta exitosa
- **Manual**: Opción de menú para forzar guardado

### Recuperación al Iniciar

Al ejecutar `main.py`, el sistema carga automáticamente:
1. Todos los productos desde `productos.json`
2. Todos los usuarios desde `usuarios.json`
3. Todas las ventas desde `ventas.json`

Si los archivos no existen, comienza con colecciones vacías.

## Manejo de Excepciones

El sistema implementa manejo específico de excepciones:

### En Modelos
- **ValueError**: Para validación de atributos (precio negativo, stock negativo, cantidad inválida)

### En Servicios - Archivo
- **FileNotFoundError**: Cuando un archivo JSON no existe (retorna colección vacía)
- **json.JSONDecodeError**: Cuando el JSON es inválido (maneja y continúa)
- **PermissionError**: Cuando no hay permisos de lectura/escritura (notifica al usuario)
- **KeyError**: Cuando falta una clave esperada en los datos (omite el registro)
- **ValueError**: Durante la reconstrucción de objetos (omite registros inválidos)

### En Servicios - Restaurante
- **ValueError**: Cuando la cantidad de venta es inválida
- **Exception**: Captura general para operaciones de archivo

### En Main
- **ValueError**: Para entrada de números inválida
- **Exception**: Captura general para operaciones no previstas

## Operaciones Principales

### 1. Gestión de Productos

**Registrar producto**
```
Ingrese código, nombre, categoría, precio y stock.
Sistema valida que no exista código duplicado.
Se guarda automáticamente en productos.json.
```

**Listar productos**
```
Muestra todos los productos con información completa incluyendo stock.
```

**Buscar producto**
```
Busca por código y muestra información completa.
```

**Actualizar producto**
```
Permite actualizar nombre, categoría, precio y/o stock.
Se guarda automáticamente en productos.json.
```

**Eliminar producto**
```
Elimina un producto después de confirmación.
Se guarda automáticamente en productos.json.
```

### 2. Gestión de Usuarios

**Registrar usuario**
```
Ingrese identificación, nombre y correo.
Sistema valida que no exista identificación duplicada.
Se guarda automáticamente en usuarios.json.
```

**Listar usuarios**
```
Muestra todos los usuarios con información completa.
```

### 3. Gestión de Ventas

**Realizar venta**
```
1. Ingresa identificación del usuario
2. Sistema valida que usuario existe
3. Ingresa código del producto
4. Sistema valida que producto existe
5. Ingresa cantidad a vender
6. Sistema valida:
   - Cantidad > 0
   - Stock suficiente
7. Si es válido:
   - Crea Venta
   - Agrega a colección
   - Disminuye stock
   - Guarda ventas.json y productos.json
```

**Listar todas las ventas**
```
Muestra todas las ventas registradas con información de usuario,
producto y cantidad.
```

**Consultar ventas de un usuario**
```
1. Ingresa identificación del usuario
2. Sistema muestra todas sus ventas
3. Calcula y muestra:
   - Total de venta(s)
   - Cantidad total
   - Monto total (precio × cantidad)
```

### 4. Persistencia Manual

**Guardar datos**
```
Fuerza el guardado manual de productos, usuarios y ventas en JSON.
```

**Cargar datos**
```
Carga manualmente los datos desde los archivos JSON.
```

## Validaciones del Sistema

### Validaciones en Productos
- Precio no puede ser negativo
- Stock no puede ser negativo
- Código debe ser único
- Al vender: cantidad debe ser > 0 y <= stock disponible

### Validaciones en Usuarios
- Identificación no puede estar vacía
- Nombre no puede estar vacío
- Correo no puede estar vacío
- Identificación debe ser única

### Validaciones en Ventas
- Usuario debe existir
- Producto debe existir
- Cantidad debe ser > 0
- Stock debe ser suficiente
- Cantidad debe ser válida (número entero)

## Flujo de Ejecución

```
1. Ejecutar main.py
2. Sistema carga datos desde archivos
3. Muestra menú principal
4. Usuario selecciona opción
5. Sistema ejecuta acción
6. Retorna al menú o solicita datos
7. Sistema guarda cambios automáticamente
8. Paso 3 se repite hasta seleccionar "Salir"
```

## Pruebas Realizadas

### Prueba 1: Carga y Guardado Básico
- ✓ Registrar un producto con stock
- ✓ Verificar que se guarda en productos.json
- ✓ Registrar un usuario
- ✓ Verificar que se guarda en usuarios.json
- ✓ Cerrar y reiniciar la aplicación
- ✓ Confirmar que los datos se recuperan

### Prueba 2: Venta Exitosa
- ✓ Crear usuario y producto
- ✓ Realizar venta válida
- ✓ Verificar que stock disminuye
- ✓ Verificar que se crea entrada en ventas.json
- ✓ Confirmar que ventas.json se guarda correctamente

### Prueba 3: Venta con Stock Insuficiente
- ✓ Crear usuario y producto con stock 5
- ✓ Intentar vender cantidad 10
- ✓ Sistema rechaza la operación
- ✓ Verificar que stock no cambia
- ✓ Verificar que no se crea entrada en ventas.json

### Prueba 4: Consulta de Ventas por Usuario
- ✓ Realizar múltiples ventas al mismo usuario
- ✓ Consultar ventas del usuario
- ✓ Verificar que se muestran todas las ventas correctas
- ✓ Verificar cálculo de totales

### Prueba 5: Persistencia Completa
- ✓ Registrar múltiples productos, usuarios y ventas
- ✓ Guardar datos
- ✓ Cerrar aplicación
- ✓ Reiniciar aplicación
- ✓ Verificar que todos los datos se recuperan completos

### Prueba 6: Manejo de Excepciones
- ✓ Intentar vender con usuario inexistente
- ✓ Intentar vender con producto inexistente
- ✓ Intentar vender cantidad inválida
- ✓ Intentar registrar producto con precio negativo
- ✓ Intentar registrar usuario con datos vacíos

## Cambios Respecto a Semana 10

### Nuevos Componentes
1. **Clase Venta**: Representa la relación usuario-producto
2. **Persistencia de Usuarios**: Ahora usuarios se guardan en JSON
3. **Persistencia de Ventas**: Nueva colección completamente persistida

### Cambios en Producto
1. **Stock**: Nuevo atributo obligatorio
2. **Método vender()**: Para disminuir stock validado
3. **Actualización JSON**: Ahora incluye stock

### Cambios en Usuario
1. **Validación mejorada**: Valida que campos no estén vacíos
2. **Método a_diccionario()**: Para serialización JSON
3. **Persistencia**: Ahora se guarda en usuarios.json

### Cambios en Restaurante
1. **Nueva colección**: self.ventas
2. **Nueva operación**: vender_producto()
3. **Nueva consulta**: obtener_ventas_usuario()
4. **Método buscar_usuario()**: Nuevo método de búsqueda
5. **Métodos de persistencia**: Incluyen usuarios y ventas

### Cambios en ArchivoServicio
1. **Nuevos métodos**: guardar/cargar usuarios y ventas
2. **Manejo de 3 archivos**: productos, usuarios, ventas

### Cambios en main.py
1. **Nuevo menú**: Opción 8-10 para ventas
2. **Nuevas funciones**: realizar_venta(), consultar_ventas_usuario()
3. **Carga automática**: Ahora carga usuarios y ventas

## Forma de Ejecución

### Requisitos
- Python 3.7+
- No se requieren librerías externas (solo módulos estándar)

### Pasos para Ejecutar

1. Navegar al directorio del proyecto:
```bash
cd restaurante_app
```

2. Ejecutar el programa:
```bash
python main.py
```

3. Interactuar con el menú:
- Seleccionar opción numérica (1-13)
- Seguir las solicitudes de entrada
- Los datos se guardan automáticamente

### Estructura de Directorios Esperada

```
restaurante_app/
├── main.py
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
└── datos/
    ├── productos.json (creado automáticamente)
    ├── usuarios.json (creado automáticamente)
    └── ventas.json (creado automáticamente)
```

## Notas Importantes

1. **Colecciones de Objetos**: El sistema utiliza objetos del dominio (Producto, Usuario, Venta), no diccionarios
2. **Persistencia automática**: Los cambios se guardan automáticamente en JSON después de operaciones
3. **Recuperación garantizada**: Al reiniciar la aplicación, se recuperan todos los datos
4. **Sin bases de datos**: Utiliza solo archivos JSON
5. **Validación en capas**: Validación en modelos y en servicio
6. **Manejo explícito**: No utiliza `except: pass`; todas las excepciones se manejan específicamente

## Restricciones y Limitaciones

- No hay facturación, IVA ni descuentos
- No hay carrito de compras
- No hay métodos de pago
- No hay proveedores ni órdenes
- No hay interfaz gráfica
- No hay base de datos persistente
- No hay autenticación
- Ventas simples (usuario + producto + cantidad)

## Contacto y Entrega

Este proyecto se entrega como repositorio público de GitHub con:
- Código completo y funcional
- Archivos JSON de ejemplo (si aplica)
- README.md documentado
- Estructura modular clara
- Validaciones robustas

---

**Versión**: Semana 11
**Última actualización**: 2026-08-27
**Estado**: ✓ Completo y Funcional

