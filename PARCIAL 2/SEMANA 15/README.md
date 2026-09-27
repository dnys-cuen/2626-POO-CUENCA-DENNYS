# Restaurante App - Semana 15

Evolución de la aplicación restaurante_app para la Semana 15.

Propósito:
- Añadir la gestión de Ventas como una nueva sección que demuestra el flujo: acción de usuario -> command= -> callback -> servicio -> persistencia -> respuesta visual.

Qué se implementó:
- Nuevo modelo Venta en modelos/venta.py.
- RestauranteServicio ahora gestiona ventas: listar_ventas() y registrar_venta(username, producto_id). Las validaciones y persistencia están en el servicio.
- Persistencia de ventas en datos/ventas.json usando servicios/archivo_servicio.py.
- Interfaz en ui/main_view.py con sección Ventas: selección de usuario (Combobox), selección de producto (Combobox), botón "Registrar venta" (command=) y tabla Treeview para mostrar ventas.
- Carpeta assets/ incluida con recursos visuales generados automáticamente por script:
  - logo.png, logo_small.png, logo.svg (logotipo)
  - banner.png (banner principal)
  - icon.png (icono de la aplicación)
  - icon_users.png, icon_products.png, icon_sales.png, icon_logout.png (iconos de navegación)
  - decor_welcome.png (recurso decorativo)

Las imágenes fueron creadas programáticamente con Pillow y ya están integradas en la interfaz:
- ui/login_view.py carga assets/logo.png en la vista de login.
- ui/main_view.py usa los iconos para los botones de navegación y muestra banner.png si está disponible.
- main.py intenta usar assets/icon.png como icono de la ventana.

Reemplaze estos archivos si desea gráficos personalizados; los archivos actuales son recursos profesionales generados automáticamente para la entrega de la Semana 15.

Ejecución:
1. Abrir una terminal en esta carpeta (la que contiene main.py).
2. Activar el entorno virtual (opcional).
3. Ejecutar: python main.py

Notas:
- La lógica de validación y guardado está en servicios/restaurante_servicio.py.
- Los archivos JSON (usuarios.json, productos.json y ventas.json) se almacenan en la carpeta datos/.
- Esta entrega mantiene la estructura modular: datos/, modelos/, servicios/, ui/ y main.py.

Correcciones visuales y de navegación:
- Se corrigió la navegación: cada botón en la barra lateral muestra su sección correspondiente (Usuarios, Productos, Ventas) en lugar de mostrar siempre Ventas.
- Se añadieron barras de desplazamiento a los Treeview y se mejoró la disposición de formularios, espacios y botones para una interfaz más ordenada.
- Los recursos gráficos en assets/ fueron generados programáticamente y están integrados en las vistas (logo, banner, iconos, elementos decorativos).
