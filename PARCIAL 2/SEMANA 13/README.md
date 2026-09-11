# Restaurante App - Base gráfica (Semana 13)

Propósito:
Proyecto base para la Semana 13: proporcionar una estructura mínima y funcional de aplicación gráfica (Tkinter) adaptada al dominio de un restaurante. Incluye modelos, servicios, datos locales y vistas separadas, y demuestra el flujo de login -> panel principal.

Estructura del proyecto:
restaurante_app/
├── datos/
│   ├── productos.json    # datos de ejemplo de productos
│   └── usuarios.json     # usuarios de prueba
├── modelos/
│   ├── __init__.py
│   ├── producto.py       # clase Producto (id, nombre, precio, cantidad)
│   └── usuario.py        # clase Usuario (username, password, nombre)
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py   # lectura de JSON desde carpeta datos/
│   └── restaurante_servicio.py # operaciones: validar_usuario, listar_usuarios, listar_productos, obtener_cantidad
├── ui/
│   ├── __init__.py
│   ├── login_view.py     # pantalla de acceso (LoginView)
│   └── main_view.py      # panel principal (MainView)
├── main.py               # punto de entrada: prepara servicios y controla cambio de vistas
└── README.md

Flujo de la aplicación (mínimo):
1. main.py prepara Tkinter y los servicios (ArchivoServicio -> RestauranteServicio).
2. Se muestra LoginView en la misma ventana principal.
3. El usuario ingresa usuario y contraseña.
4. RestauranteServicio valida las credenciales.
5. Si son válidas, se muestra MainView en la misma ventana.
6. Desde MainView se pueden ver: Productos, Usuarios y una opción marcada como "Ventas (pendiente)".
7. Cerrar sesión vuelve al LoginView dentro de la misma ventana.

Vistas implementadas:
- LoginView: formulario sencillo con campos Usuario y Contraseña, mensajes de error y botón de ingresar. Solicita validación a RestauranteServicio.
- MainView: panel con botones para mostrar Usuarios y Productos (lista simple) y botón para cerrar sesión. Ventas aparece como funcionalidad pendiente.

Ejecución:
1. Abrir una terminal en la carpeta restaurante_app (la que contiene main.py).
2. Ejecutar: python main.py

Credenciales de prueba:
- admin / admin123
- camarero / camarero

Notas importantes:
- La UI no lee archivos JSON directamente; todas las vistas usan RestauranteServicio para obtener datos.
- Los datos de ejemplo están en la carpeta datos/ como JSON; ArchivoServicio es responsable de su lectura.
- Esta base es intencionalmente simple: se añadirá más funcionalidad gráfica en semanas posteriores (formularios, ventas, edición de datos, etc.).

---
Actualizado: versión inicial que cumple los requisitos de la Semana 13 (usuarios y productos, estructura separada por capas, una ventana principal y ciclo único de ejecución).
