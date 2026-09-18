# Semana 14 - Restaurante App

En esta semana se continuó con el desarrollo de la aplicación de restaurante, enfocándose en mejorar la capa de interfaz mediante componentes y contenedores de Tkinter/ttk. El objetivo principal fue mantener la estructura modular del proyecto y evolucionar la vista principal para organizar mejor la navegación, los formularios y la presentación de información.

## Propósito de la semana

La actividad busca aplicar correctamente la separación entre interfaz, lógica de negocio y persistencia. Se mantiene el flujo de inicio de sesión y se refuerza la gestión de productos para que funcione con operaciones sencillas de registro, consulta, actualización y eliminación, siempre delegando la validación y la lógica del dominio al servicio correspondiente.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
├── README.md
```

## Componentes y contenedores utilizados

Se utilizó una arquitectura modular con separación por responsabilidades:

- `modelos`: define las clases `Usuario` y `Producto`.
- `servicios`: concentra la lógica de negocio y la persistencia mediante archivos JSON.
- `ui`: contiene las vistas de acceso y la interfaz principal.
- `main.py`: inicializa la aplicación y controla la navegación entre pantallas.

En la interfaz principal se emplearon contenedores para separar visualmente las zonas de:

- navegación lateral,
- formulario de productos,
- consulta de usuarios,
- visualización de información en tablas,
- mensajes de estado y acciones del sistema.

También se usaron controles como `Label`, `Entry`, `Button`, `Frame`, `Treeview`, `StringVar` y `ttk`, siguiendo una organización clara y legible para el usuario.

## Mejoras realizadas en la interfaz

Se mejoró la vista principal para que la aplicación se vea más ordenada y clara. Se incorporaron contenedores para diferenciar cada sección y facilitar la navegación. La interfaz mantiene la consulta de usuarios disponible y agrega una zona específica para gestionar productos con un formulario estructurado.

La vista de productos incluye:

- campo para ingresar el ID,
- nombre,
- precio,
- cantidad,
- botones para registrar, consultar, actualizar, eliminar y limpiar,
- tabla que muestra la información actual almacenada,
- mensajes visuales que informan sobre el resultado de cada operación.

## Operaciones implementadas sobre productos

La aplicación permite realizar las siguientes acciones sobre los productos:

- Registrar un nuevo producto.
- Consultar un producto por su ID.
- Actualizar los datos de un producto.
- Eliminar un producto.
- Visualizar la lista actual de productos.

Estas operaciones están gestionadas desde `RestauranteServicio`, evitando que la lógica de negocio se escriba directamente en los botones o formularios de la interfaz. La vista solo solicita la operación y muestra el resultado.

## Persistencia

La persistencia se mantiene a través de archivos JSON y el servicio `ArchivoServicio`:

- `datos/usuarios.json`: almacena los usuarios del sistema.
- `datos/productos.json`: almacena la información de los productos.

Cuando se realiza una operación sobre productos, el servicio actualiza la lista interna y luego guarda los cambios en `productos.json` para que permanezcan al cerrar y volver a ejecutar la aplicación.

## Ejecución

Para ejecutar la aplicación, debe ubicarse en la carpeta del proyecto y correr el archivo `main.py`:

```bash
cd "PARCIAL 2/SEMANA 14/restaurante_app"
python main.py
```

## Credenciales de prueba

Usuario válido:

- Usuario: `admin`
- Contraseña: `admin123`

También se incluye otro usuario de ejemplo:

- Usuario: `camarero`
- Contraseña: `camarero`

Con esto se puede iniciar sesión y probar el flujo completo de la interfaz principal.
