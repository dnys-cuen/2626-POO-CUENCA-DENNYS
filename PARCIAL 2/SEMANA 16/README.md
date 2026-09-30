# Restaurante App - Semana 16

Esta versión evoluciona la aplicación desarrollada en la Semana 15 conservando la arquitectura modular del proyecto y reforzando la gestión de usuarios con eventos, permisos y persistencia.

## Objetivo

Aplicar de forma práctica el manejo de eventos en la interfaz gráfica para gestionar usuarios desde un formulario y un Treeview, sin concentrar la lógica de negocio dentro de la interfaz.

## Funcionalidades destacadas

- Inicio de sesión con validación a través de `RestauranteServicio`.
- Navegación principal con Productos, Ventas y Usuarios.
- Gestión administrativa de usuarios para rol `Administrador`.
- Modelo `Usuario` con atributo `rol` y soporte para `Administrador`, `Empleado` y `Cliente`.
- Tabla `Treeview` con selección mediante `<<TreeviewSelect>>`.
- Formularios con `command=` para botones y eventos de teclado `<Return>` y `<Escape>`.
- Combobox para cambiar el rol con `<<ComboboxSelected>>`.
- Validaciones, reglas y persistencia centralizadas en `RestauranteServicio`.
- Integración visual con recursos de `assets/` y diseño consistente.

## Estructura

- `datos/` para archivos JSON
- `modelos/` para entidades
- `servicios/` para lógica de negocio y persistencia
- `ui/` para vistas de login y menú principal
- `assets/` para íconos y recursos visuales
- `main.py` como punto de entrada

## Ejecución

1. Abrir una terminal dentro de la carpeta `restaurante_app`.
2. Ejecutar: `python main.py`
3. Iniciar sesión con el usuario administrador:
   - usuario: `admin`
   - contraseña: `admin123`

## Observaciones

- La sección de usuarios solo está activa para usuarios con rol `Administrador`.
- La eliminación de la cuenta actualmente autenticada queda bloqueada para evitar borrados accidentales.
- Los cambios se persisten en `datos/usuarios.json` y se reflejan en la interfaz tras cada operación.
