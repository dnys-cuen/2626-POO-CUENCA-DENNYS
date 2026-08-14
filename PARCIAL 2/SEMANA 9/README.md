# Sistema de Restaurante con Persistencia en JSON
## PARCIAL 2 - SEMANA 9

### Descripción General
Este proyecto es una extensión del Sistema de Restaurante de PARCIAL 1 SEMANA 8, que incorpora **funcionalidad de persistencia de datos en archivos JSON** utilizando una estructura tipo **diccionario**.

### Características Principales

#### 1. **Gestión de Productos**
- Registrar productos (Producto y Bebida)
- Listar todos los productos
- Guardar/Cargar productos en/desde JSON

#### 2. **Gestión de Clientes**
- Registrar clientes
- Listar todos los clientes
- Guardar/Cargar clientes en/desde JSON

#### 3. **Persistencia en JSON con Estructura Diccionario**
La persistencia utiliza diccionarios para optimizar acceso y búsqueda:

**Estructura de Productos (productos.json):**
```json
{
    "codigo1": {
        "tipo": "Producto" | "Bebida",
        "nombre": "...",
        "categoria": "...",
        "precio": 0.0,
        "tamaño": "..." (solo para Bebida),
        "tipo_envase": "..." (solo para Bebida)
    }
}
```

**Estructura de Clientes (clientes.json):**
```json
{
    "identificacion1": {
        "nombre": "...",
        "correo": "..."
    }
}
```

### Menú Principal
```
1. Registrar producto
2. Registrar bebida
3. Registrar cliente
4. Listar productos
5. Listar clientes
6. Guardar datos en JSON
7. Cargar datos desde JSON
8. Salir
```

### Estructura de Directorios

```
restaurante_app/
├── main.py                      # Punto de entrada
├── test_persistencia.py         # Script de pruebas automatizadas
├── modelos/
│   ├── __init__.py
│   ├── producto.py             # Clase Producto
│   ├── bebida.py               # Clase Bebida (hereda de Producto)
│   └── cliente.py              # Clase Cliente
├── servicios/
│   ├── __init__.py
│   ├── restaurante.py          # Lógica de negocio
│   └── persistencia_json.py    # Gestión de archivos JSON
└── datos/
    ├── productos.json          # Almacén de productos (estructura diccionario)
    └── clientes.json           # Almacén de clientes (estructura diccionario)
```

### Cómo Usar

#### Ejecutar la Aplicación Interactiva
```bash
python main.py
```

#### Ejecutar Pruebas Automatizadas
```bash
python test_persistencia.py
```

### Clase PersistenciaJSON

La clase `PersistenciaJSON` en `servicios/persistencia_json.py` proporciona:

**Métodos Principales:**
- `guardar_productos(productos)` → Guarda lista de productos en JSON
- `cargar_productos()` → Carga productos desde JSON
- `guardar_clientes(clientes)` → Guarda lista de clientes en JSON
- `cargar_clientes()` → Carga clientes desde JSON

**Características:**
- Conversión automática de objetos Python a diccionarios
- Conversión automática de diccionarios JSON a objetos Python
- Manejo robusto de errores
- Codificación UTF-8 para caracteres especiales
- Creación automática de directorio `datos/`

### Integración con la Clase Restaurante

La clase `Restaurante` incluye:
```python
def guardar_datos() -> bool:
    """Guarda productos y clientes en JSON"""
    
def cargar_datos() -> bool:
    """Carga productos y clientes desde JSON"""
```

### Ventajas de la Estructura Diccionario

1. **Acceso O(1)**: Búsqueda rápida por código/identificación
2. **No duplicados**: La clave única previene duplicaciones
3. **Facilidad de consulta**: Buscar un producto específico es trivial
4. **Escalabilidad**: Ideal para grandes volúmenes de datos
5. **Legibilidad**: Estructura clara y autodocumentada

### Flujo de Uso Típico

1. **Iniciar la aplicación** → Carga automáticamente datos previos
2. **Registrar productos y clientes** → Se mantienen en memoria
3. **Guardar datos** → Persiste en `datos/productos.json` y `datos/clientes.json`
4. **Cerrar aplicación** → Datos se pierden de memoria (pero existen en archivos)
5. **Reiniciar aplicación** → Carga automáticamente datos desde archivos

### Ejemplo de Uso en Código

```python
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

# Crear restaurante y cargar datos previos
restaurante = Restaurante()
restaurante.cargar_datos()

# Registrar nuevo producto
producto = Producto("P003", "Ensalada", "Platos Principales", 8.50)
restaurante.registrar_producto(producto)

# Guardar en JSON
restaurante.guardar_datos()
```

### Consideraciones Técnicas

- **Directorio de datos**: Se crea automáticamente en `datos/`
- **Formato JSON**: Indentado con 4 espacios para legibilidad
- **Codificación**: UTF-8 para soportar caracteres especiales
- **Herencia**: Bebida hereda de Producto, se diferencia por campo "tipo"
- **Robustez**: Cargar desde archivos inexistentes devuelve listas vacías

### Pruebas Incluidas

El script `test_persistencia.py` verifica:
- ✓ Registro de productos (Producto y Bebida)
- ✓ Registro de clientes
- ✓ Guardado de datos en JSON
- ✓ Estructura correcta de diccionarios en JSON
- ✓ Carga de datos desde JSON
- ✓ Integridad de datos tras guardar/cargar
- ✓ Cantidad correcta de registros

### Próximas Mejoras Posibles

- Base de datos SQL en lugar de JSON
- Búsqueda y filtrado avanzado
- Exportación a formatos adicionales (CSV, XML)
- Control de versiones de datos
- Autenticación de usuarios
- Validación avanzada de datos

---
**Autor**: Sistema de Restaurante - PARCIAL 2 SEMANA 9  
**Lenguaje**: Python 3.8+  
**Última Actualización**: 2026-08-14
