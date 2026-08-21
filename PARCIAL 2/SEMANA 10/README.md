# Sistema de Restaurante - Semana 10

## Descripción General

Este proyecto continúa desarrollando la aplicación `restaurante_app` iniciada en semanas anteriores. Para la **Semana 10**, se ha implementado una evolución significativa: la persistencia de productos mediante archivos JSON.

### Mejora Principal: Persistencia de Productos

El sistema ahora es capaz de:
- **Guardar productos** en un archivo JSON (`datos/productos.json`) después de cada operación (registrar, actualizar, eliminar)
- **Cargar productos** automáticamente al iniciar la aplicación
- **Mantener la continuidad** de los datos entre diferentes ejecuciones del programa
- **Validar y reconstruir** objetos Producto a partir de la información persistida

## Estructura del Proyecto

```
restaurante_app/
├── datos/
│   └── productos.json          # Almacenamiento persistente de productos
├── modelos/
│   ├── __init__.py
│   ├── producto.py             # Clase Producto con método a_diccionario()
│   └── usuario.py              # Clase Usuario (en memoria, no persiste)
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py     # Servicio de persistencia JSON
│   └── restaurante.py          # Servicio principal del negocio
├── main.py                     # Punto de entrada con menú interactivo
└── README.md                   # Este archivo
```

## Componentes Principales

### 1. **modelos/producto.py**
- **Clase Producto**: Entidad que representa un producto del restaurante
- **Atributos**: codigo, nombre, categoria, precio
- **Método `a_diccionario()`**: Convierte el producto a diccionario para JSON
- **Validación**: El precio no puede ser negativo (genera `ValueError`)

### 2. **modelos/usuario.py**
- **Clase Usuario**: Entidad que representa a un usuario
- **Atributos**: identificacion, nombre, correo
- **Nota**: Los usuarios NO se persisten en esta semana, se almacenan solo en memoria

### 3. **servicios/archivo_servicio.py** ⭐
Nuevo servicio encargado de toda la persistencia de productos:

**Métodos principales:**
- `guardar_productos(productos: List[Producto]) -> bool`: Guarda productos en JSON
- `cargar_productos() -> List[Producto]`: Carga productos desde JSON

**Manejo de Excepciones Específicas:**
- `FileNotFoundError`: Cuando `productos.json` no existe (primera ejecución)
  - Comportamiento: Inicia con colección vacía
- `json.JSONDecodeError`: Cuando el archivo existe pero no contiene JSON válido
  - Comportamiento: Registra error y devuelve colección vacía
- `PermissionError`: Cuando no hay permisos de lectura/escritura
  - Comportamiento: Notifica al usuario y retorna False
- `KeyError`/`ValueError`: Cuando un registro no tiene los datos completos o válidos
  - Comportamiento: Omite ese registro y continúa con los demás

### 4. **servicios/restaurante.py**
Servicio principal del negocio que:
- Gestiona la colección de productos en memoria
- Proporciona operaciones CRUD: registrar, buscar, actualizar, eliminar
- Coordina con `ArchivoServicio` para guardar cambios automáticamente
- También maneja usuarios (sin persistencia en esta semana)

**Métodos de Producto:**
- `registrar_producto(producto: Producto) -> bool`
- `buscar_producto_por_codigo(codigo: str) -> Optional[Producto]`
- `actualizar_producto(codigo, nuevo_nombre, nueva_categoria, nuevo_precio) -> bool`
- `eliminar_producto(codigo: str) -> bool`
- `listar_productos() -> List[str]`

### 5. **main.py** 
Punto de entrada con menú interactivo que:
1. Al iniciar, carga automáticamente los productos desde JSON
2. Permite al usuario:
   - Registrar productos (registra automáticamente en archivo)
   - Listar productos
   - Buscar producto por código
   - Actualizar producto (actualiza automáticamente en archivo)
   - Eliminar producto (elimina automáticamente en archivo)
   - Registrar usuarios (en memoria)
   - Listar usuarios
   - Cargar productos desde archivo manualmente

## Flujo de Carga de Productos

```
┌─────────────────────────────────────┐
│ Inicio de la Aplicación (main.py)   │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│ Restaurante() crea ArchivoServicio  │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│ cargar_productos_desde_archivo()    │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│ ArchivoServicio.cargar_productos()  │
└────────────┬────────────────────────┘
             │
      ┌──────┴──────┐
      │             │
      ▼             ▼
  Existe       No existe
  archivo      archivo
      │             │
      ▼             ▼
  json.load()   Retorna []
      │             │
      ▼             │
  Validar       Menú principal
  estructura    (continúa)
      │
      ▼
  Para cada registro:
  - Validar claves
  - Validar tipos
  - Crear Producto(...)
      │
      ▼
  Retorna List[Producto]
      │
      ▼
  Restaurante los almacena
      │
      ▼
  Menú principal disponible
```

## Flujo de Guardado de Productos

```
┌──────────────────────────────────────┐
│ Usuario: Registra/Actualiza/Elimina  │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│ main.py solicita operación           │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│ Restaurante modifica colección       │
│ (en memoria: List[Producto])         │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│ Restaurante solicita guardar         │
│ a ArchivoServicio                    │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│ ArchivoServicio convierte a dicts:   │
│ [{codigo, nombre, categoria, precio},│
│  {...}]                              │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│ json.dump() escribe en              │
│ datos/productos.json                │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│ ✓ Cambio persistido                  │
│ (puede cerrarse sin pérdida)         │
└──────────────────────────────────────┘
```

## Formato JSON

Los productos se almacenan con la siguiente estructura:

```json
[
    {
        "codigo": "P001",
        "nombre": "Pizza Margherita",
        "categoria": "Pizzas",
        "precio": 12.50
    },
    {
        "codigo": "P002",
        "nombre": "Ensalada César",
        "categoria": "Ensaladas",
        "precio": 8.75
    }
]
```

## Manejo de Excepciones

### Durante la Carga

| Excepción | Causa | Comportamiento |
|-----------|-------|----------------|
| `FileNotFoundError` | Archivo no existe | Devuelve lista vacía |
| `json.JSONDecodeError` | JSON inválido | Devuelve lista vacía + mensaje de error |
| `PermissionError` | Sin permisos de lectura | Devuelve lista vacía + mensaje de error |
| `KeyError` | Faltan claves en registro | Omite ese registro, continúa |
| `ValueError` | Datos inválidos | Omite ese registro, continúa |

### Durante el Guardado

| Excepción | Causa | Comportamiento |
|-----------|-------|----------------|
| `PermissionError` | Sin permisos de escritura | Retorna False + mensaje de error |
| Otras excepciones | Errores inesperados | Retorna False + mensaje genérico |

## Prueba de Persistencia

Para verificar que la persistencia funciona correctamente:

### Prueba Básica:
1. Ejecutar: `python main.py`
2. Seleccionar opción **1** (Registrar producto)
3. Ingresar datos: código `P001`, nombre `Coca Cola`, categoría `Bebidas`, precio `2.50`
4. Verificar que se crea/actualiza `datos/productos.json`
5. Cerrar la aplicación completamente
6. Ejecutar nuevamente: `python main.py`
7. Seleccionar opción **2** (Listar productos)
8. Confirmar que aparece el producto registrado

### Prueba de Actualización:
1. Ejecutar con datos cargados
2. Seleccionar opción **4** (Actualizar producto)
3. Actualizar código `P001` con nuevo precio
4. Cerrar y reiniciar
5. Verificar que el nuevo precio se conservó

### Prueba de Eliminación:
1. Ejecutar con datos cargados
2. Seleccionar opción **5** (Eliminar producto)
3. Eliminar un producto
4. Cerrar y reiniciar
5. Verificar que el producto no aparece en la lista

## Requisitos Cumplidos

✅ Estructura modular conservada  
✅ Carpeta `datos/` creada para persistencia  
✅ Archivo `productos.json` se genera automáticamente  
✅ Servicio `archivo_servicio.py` centraliza persistencia  
✅ Módulo `json` estándar utilizado  
✅ `with open()` con codificación UTF-8  
✅ Carga automática al iniciar  
✅ Conversión correcta JSON ↔ Producto  
✅ Actualización automática en JSON después de registrar  
✅ Actualización automática en JSON después de actualizar  
✅ Actualización automática en JSON después de eliminar  
✅ CRUD completo funcionando  
✅ Validaciones de Producto mantenidas  
✅ FileNotFoundError controlado  
✅ json.JSONDecodeError controlado  
✅ PermissionError controlado  
✅ Registros incompletos/inválidos controlados  
✅ Separación de responsabilidades clara  
✅ Anotaciones de tipos en métodos  
✅ Nombres descriptivos y convenciones Python  

## Restricciones Respetadas

✅ Proyecto evoluciona desde SEMANA 9  
✅ Clase Producto se mantiene (no reemplazada por dicts)  
✅ Sin datos quemados  
✅ archivo_servicio integrado en operaciones  
✅ Excepciones específicas, no genéricas  
✅ Sin interfaces gráficas  
✅ Sin bases de datos  
✅ Persistencia solo para productos (usuarios en memoria)  
✅ Código distribuido en archivos modulares  
✅ `__init__.py` presentes en paquetes  
✅ Colecciones no se manipulan desde main.py  
✅ Sin funcionalidades avanzadas adicionales  
✅ Nombres significativos en todo el código  

## Ejecución

```bash
# Asegurarse de estar en el directorio del proyecto
cd SEMANA\ 10/restaurante_app

# Ejecutar la aplicación
python main.py
```

**Nota**: Al primera ejecución, el sistema creará la carpeta `datos/` y el archivo `productos.json` automáticamente cuando registres el primer producto.

## Cambios Respecto a Semana 9

- **Nuevo archivo**: `servicios/archivo_servicio.py` (reemplaza parcialmente `persistencia_json.py`)
- **Mejor manejo de excepciones**: Específicas para cada caso de error
- **Adición de métodos**: Actualizar y eliminar productos con persistencia automática
- **Búsqueda de productos**: Búsqueda por código
- **Simplificación**: Se enfoca solo en persistencia de productos (usuarios en memoria)
- **Validaciones mejoradas**: Mejor control de datos inválidos durante carga

## Autor

Desarrollado para la actividad de Programación Orientada a Objetos - Semana 10

## Licencia

Este proyecto es parte de la asignatura y está disponible para fines educativos.

