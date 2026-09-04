# Sistema de Restaurante - Semana 12: Optimización con Colecciones

## Descripción General

Esta es la continuación del proyecto de **Semana 11** con mejoras enfocadas en **optimizar búsquedas, consultas y validaciones** utilizando estructuras de datos auxiliares (diccionarios e índices).

El objetivo **NO es reemplazar las colecciones principales**, sino complementarlas con índices que aceleren operaciones frecuentes que actualmente requieren recorrer listas completas.

---

## Mejoras Implementadas

### 1. **Índice de Productos por Código** (`indice_productos`)
- **Tipo**: Diccionario `{codigo: Producto}`
- **Propósito**: Acelerar búsquedas de productos por código
- **Operación Original**: Búsqueda lineal O(n) recorriendo toda la lista
- **Operación Optimizada**: Búsqueda en diccionario O(1)

**Métodos optimizados:**
- `buscar_producto_por_codigo()`: Ahora usa `indice_productos.get(codigo)`
- `_codigo_producto_existe()`: Verifica con `codigo in indice_productos`

### 2. **Índice de Usuarios por Identificación** (`indice_usuarios`)
- **Tipo**: Diccionario `{identificacion: Usuario}`
- **Propósito**: Acelerar búsquedas de usuarios por identificación
- **Operación Original**: Búsqueda lineal O(n)
- **Operación Optimizada**: Búsqueda en diccionario O(1)

**Métodos optimizados:**
- `buscar_usuario()`: Ahora usa `indice_usuarios.get(identificacion)`
- `_identificacion_usuario_existe()`: Verifica con `identificacion in indice_usuarios`

### 3. **Índice de Ventas por Usuario** (`indice_ventas_usuario`)
- **Tipo**: Diccionario `{usuario_id: [Venta]}`
- **Propósito**: Evitar recorrer toda la colección de ventas cada vez que se consulten las ventas de un usuario
- **Operación Original**: Búsqueda lineal O(n) filtrando la lista completa
- **Operación Optimizada**: Acceso directo O(1) + iteración solo sobre ventas del usuario

**Métodos optimizados:**
- `obtener_ventas_usuario()`: Ahora usa `indice_ventas_usuario.get(usuario_id, [])`

---

## Sincronización de Índices

Los índices se mantienen sincronizados automáticamente en todas las operaciones:

### Al Registrar
- ✅ `registrar_producto()`: Añade a `indice_productos`
- ✅ `registrar_usuario()`: Añade a `indice_usuarios`
- ✅ `vender_producto()`: Añade a `indice_ventas_usuario`

### Al Eliminar
- ✅ `eliminar_producto()`: Elimina de `indice_productos`

### Al Cargar desde Archivo
- ✅ `cargar_datos_desde_archivo()`: Reconstruye todos los índices con `_reconstruir_indices()`
- Garantiza coherencia entre colecciones e índices

---

## Estructura de Datos Principal

```
Restaurante
├── productos: List[Producto]               # Colección principal (persistencia)
├── usuarios: List[Usuario]                 # Colección principal (persistencia)
├── ventas: List[Venta]                     # Colección principal (persistencia)
│
└── Índices Auxiliares:
    ├── indice_productos: {código -> Producto}       # Búsqueda O(1)
    ├── indice_usuarios: {identificación -> Usuario} # Búsqueda O(1)
    └── indice_ventas_usuario: {usuario_id -> [Venta]} # Acceso O(1)
```

---

## Análisis de Complejidad

### Antes de Optimización (Semana 11)
| Operación | Complejidad | Descripción |
|-----------|-------------|-------------|
| Buscar producto | O(n) | Recorre lista completa |
| Buscar usuario | O(n) | Recorre lista completa |
| Obtener ventas de usuario | O(n) | Recorre todas las ventas |

### Después de Optimización (Semana 12)
| Operación | Complejidad | Descripción |
|-----------|-------------|-------------|
| Buscar producto | O(1) | Acceso directo en diccionario |
| Buscar usuario | O(1) | Acceso directo en diccionario |
| Obtener ventas de usuario | O(1) | Acceso directo + solo itera ventas del usuario |

---

## Flujo de Ejecución

### Inicio del Programa
1. Se crea instancia de `Restaurante`
2. Se llama a `cargar_datos_desde_archivo()`
3. Se cargan productos, usuarios y ventas desde JSON
4. Se ejecuta `_reconstruir_indices()` para sincronizar índices
5. El programa está listo para consultas optimizadas

### Durante la Sesión
- Todas las búsquedas usan los índices
- Los índices se actualizan automáticamente con cada operación
- Las operaciones son más rápidas para aplicaciones con muchos datos

### Al Cerrar
- Se guarda a JSON (colecciones principales)
- Los índices se pierden (solo en memoria)
- Al reiniciar, se reconstruyen automáticamente

---

## Modelo de Datos

### Producto
```python
{
    "codigo": "P001",
    "nombre": "Hamburguesa",
    "categoria": "Platos Principales",
    "precio": 15.50,
    "stock": 50
}
```

### Usuario
```python
{
    "identificacion": "123456789",
    "nombre": "Juan Pérez",
    "correo": "juan@example.com"
}
```

### Venta
```python
{
    "usuario_id": "123456789",
    "producto_codigo": "P001",
    "cantidad": 2
}
```

---

## Funcionalidades Conservadas

✅ Registrar productos con validación  
✅ Registrar usuarios con validación  
✅ Registrar ventas con control de stock  
✅ Listar productos, usuarios y ventas  
✅ Buscar productos y usuarios  
✅ Actualizar productos  
✅ Eliminar productos  
✅ Consultar ventas por usuario  
✅ Persistencia en JSON  
✅ Carga automática de datos al iniciar

---

## Instrucciones de Uso

### Ejecutar la Aplicación
```bash
python main.py
```

### Menú Principal
1. **Registrar producto** - Añade un nuevo producto al índice
2. **Listar productos** - Itera la colección principal
3. **Buscar producto por código** - Usa el índice (O(1))
4. **Actualizar producto** - Busca y modifica (índice O(1))
5. **Eliminar producto** - Elimina de colección e índice
6. **Registrar usuario** - Añade a índice de usuarios
7. **Listar usuarios** - Itera la colección principal
8. **Realizar venta** - Actualiza todos los índices
9. **Listar todas las ventas** - Itera colección principal
10. **Consultar ventas de usuario** - Usa índice (O(1))
11. **Guardar datos a archivo** - Persiste colecciones
12. **Cargar datos desde archivo** - Reconstruye índices
13. **Salir** - Cierra la aplicación

---

## Ventajas de la Implementación

### 1. **Rendimiento Escalable**
- Búsquedas rápidas incluso con millones de registros
- Tiempo de respuesta constante (O(1)) para consultas por clave

### 2. **Integridad de Datos**
- Colecciones principales mantienen el orden y permiten recorridos
- Índices se reconstruyen automáticamente después de cargar datos
- Sincronización garantizada en todas las operaciones

### 3. **Arquitectura Limpia**
- Mejoras solo en la capa de servicios
- No requiere cambios en main.py (excepto versión)
- Modelos sin cambios
- Servicios de archivo sin cambios

### 4. **Flexibilidad Futura**
- Índices adicionales pueden añadirse fácilmente
- Bases de datos pueden reemplazar JSON sin cambios en main
- Optimizaciones dirigidas por análisis de uso real

---

## Comprobación de Funcionamiento

Se recomienda realizar las siguientes pruebas:

1. ✅ Ejecutar main.py y confirmar que el programa inicia correctamente
2. ✅ Registrar productos y verificar que aparecen en búsquedas
3. ✅ Registrar usuarios y verificar búsquedas por identificación
4. ✅ Realizar ventas y confirmar que el stock se actualiza
5. ✅ Buscar un producto específico (usa índice O(1))
6. ✅ Buscar un usuario específico (usa índice O(1))
7. ✅ Consultar ventas de un usuario (usa índice O(1))
8. ✅ Cerrar y reiniciar el programa
9. ✅ Verificar que los datos se recuperan correctamente
10. ✅ Confirmar que los índices se reconstruyen correctamente

---

## Consideraciones Técnicas

### Uso de Memoria
- Índices duplican referencias a objetos (sin duplicación de datos)
- Impacto de memoria: ~2 entradas de diccionario por objeto principal
- Para 10,000 productos/usuarios: < 1MB adicional

### Thread-Safety
- La implementación actual **no es thread-safe**
- Para uso multi-hilo, se recomienda agregar locks/semáforos

### Persistencia
- Solo las colecciones principales se guardan en JSON
- Los índices se reconstruyen cada vez que se cargan datos
- Garantiza consistencia incluso si se modifican los archivos JSON manualmente

---

## Limitaciones

- ❌ No se implementaron préstamos ni nuevas entidades
- ❌ No se incluye base de datos (se usa JSON)
- ❌ No hay interfaz gráfica
- ❌ No se implementó facturación ni descuentos
- ❌ No hay sistema de proveedores

---

## Autor

**Dennys Silvano Cuenca Japon** - Semana 12

---

## Versión

**1.0.0** - Semana 12 (Optimización con Colecciones)

Basado en:
- Semana 11: Ventas y Persistencia JSON
- Semana 10: Persistencia de Datos
- Semana 9-8: Gestión de Entidades

---

