# restaurante_app

Proyecto de ejemplo desarrollado para la Semana 7 de Programación Orientada a Objetos.

Descripción
-----------
Este proyecto implementa un sistema sencillo de gestión de un restaurante en Python,
organizado en capas (modelos y servicios) y con un menú interactivo por consola.
Permite registrar, listar y buscar productos y clientes. Su objetivo principal es
demostrar la creación de objetos mediante constructores, el uso de `@property`/`@setter`
para encapsulación, el uso de `@dataclass` para entidades simples y la separación
de responsabilidades mediante una clase de servicio.

Estructura del proyecto
-----------------------
La estructura dentro de este directorio es:

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

Descripción de archivos importantes
----------------------------------
- `modelos/producto.py`: contiene la clase `Producto` que usa un constructor tradicional
  (`__init__`) y atributos encapsulados (`_nombre`, `_categoria`, `_precio`, `_disponible`).
  Se usan decoradores `@property` y `@setter` para controlar acceso y realizar
  validaciones (nombre y categoría no vacíos, precio > 0). También incluye el método
  `mostrar_informacion()` para presentar el producto de forma legible.

- `modelos/cliente.py`: contiene la clase `Cliente` definida con `@dataclass`.
  Tiene los campos `nombre`, `correo` e `id_cliente`.

- `servicios/restaurante.py`: contiene la clase `Restaurante` que administra listas
  de productos y clientes. Provee métodos para registrar, listar y buscar ambos tipos
  de entidades. Evita duplicar `id_cliente` al registrar clientes.

- `main.py`: punto de entrada. Presenta un menú interactivo (opciones 1..7) que permite
  crear objetos a partir de datos ingresados por `input()`, además carga datos de
  ejemplo al iniciar para facilitar la demostración.

Uso y ejecución
---------------
Desde PowerShell en Windows (ubicarse en el directorio `SEMANA 7` o usar la ruta absoluta):

```powershell
cd "C:\Users\PC-ENV\UEA\2626-POO-CUENCA-DENNYS\PARCIAL 1\SEMANA 7\restaurante_app"
python -u main.py
```

Al iniciar verá el menú con opciones para registrar/listar/buscar productos y clientes.
El programa incluye datos de ejemplo (productos y clientes) cargados automáticamente.

Explicación técnica requerida
----------------------------
- Constructor en `Producto`: se utiliza `__init__` para inicializar el objeto y luego
  se delega la asignación a los setters para aplicar las validaciones correspondientes.

- Uso de `@property` y `@setter`: cada atributo del `Producto` tiene su propiedad y
  su setter asociado, lo que permite encapsular la validación y transformación de datos
  (por ejemplo convertir el precio a `float` y validar que sea mayor que cero).

- Uso de `@dataclass` en `Cliente`: simplifica la definición de una clase destinada
  principalmente a almacenar datos, generando automáticamente `__init__`, `__repr__`,
  y otros métodos útiles.

Menú interactivo
-----------------
El `main.py` presenta el siguiente menú:

```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Listar productos
3. Buscar producto
----------------------------------------
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
----------------------------------------
7. Salir
```

Cada opción ejecuta funciones específicas que solicitan datos por `input()`, crean
objetos (`Producto` o `Cliente`) y los registran en la clase `Restaurante`.

Reflexión
---------
Trabajar con entradas de usuario para crear objetos es crucial en aplicaciones reales:
permite transformar datos no estructurados (texto) en estructuras de datos ricas
(objetos) que encapsulan comportamiento y reglas de negocio. El uso de `@property`
y `@dataclass` ayuda a mantener el código legible y seguro, aplicando validaciones
y reduciendo el código repetitivo.

Instrucciones para subir a GitHub (sugerencia)
--------------------------------------------
Si desea convertir esta carpeta en un repositorio para entregar en GitHub, puede usar:

```powershell
cd "C:\Users\PC-ENV\UEA\2626-POO-CUENCA-DENNYS\PARCIAL 1\SEMANA 7"
git init
git add README.md restaurante_app
git commit -m "Agregar proyecto restaurante_app con modelos, servicios y main"
rem <crear el repo en GitHub y luego ejecutar>
git remote add origin https://github.com/USUARIO/NOMBRE_REPO.git
git branch -M main
git push -u origin main
```

Donde `USUARIO` y `NOMBRE_REPO` son su usuario y el nombre del repositorio en GitHub.

Si desea, puedo ayudar a generar automáticamente el repositorio en GitHub desde aquí
si me autoriza (necesitaría credenciales o un token, que por seguridad debe crear usted).

---

Autor: Proyecto creado como respuesta a la actividad de la Semana 7 (POO).

