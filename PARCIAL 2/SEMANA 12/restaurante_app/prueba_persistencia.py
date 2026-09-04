"""
Script de prueba para la aplicación de restaurante.
Prueba todas las funcionalidades principales.
"""

from servicios.restaurante import Restaurante

def main():
    # Crear instancia del restaurante
    rest = Restaurante()

    # Cargar datos
    print('Cargando datos...')
    rest.cargar_datos_desde_archivo()

    # Mostrar estadísticas
    print(f'\n✓ Productos cargados: {rest.obtener_cantidad_productos()}')
    print(f'✓ Usuarios cargados: {rest.obtener_cantidad_usuarios()}')
    print(f'✓ Ventas cargadas: {rest.obtener_cantidad_ventas()}')

    print('\n--- PRODUCTOS ---')
    for p in rest.listar_productos():
        print(f'  {p}')

    print('\n--- USUARIOS ---')
    for u in rest.listar_usuarios():
        print(f'  {u}')

    print('\n--- VENTAS ---')
    for v in rest.listar_ventas():
        print(f'  {v}')

    # Prueba: Venta exitosa
    print('\n=== PRUEBA: VENTA EXITOSA ===')
    exito = rest.vender_producto('HAMBURGUESA', '111222333', 2)
    print(f'Resultado: {exito}')
    print(f'Stock de HAMBURGUESA después: {rest.buscar_producto_por_codigo("HAMBURGUESA").stock}')
    print(f'Total de ventas después: {rest.obtener_cantidad_ventas()}')

    # Prueba: Venta con stock insuficiente
    print('\n=== PRUEBA: STOCK INSUFICIENTE ===')
    exito = rest.vender_producto('POSTRE', '123456789', 50)
    print(f'Resultado (debe ser False): {exito}')
    print(f'Stock de POSTRE no cambió: {rest.buscar_producto_por_codigo("POSTRE").stock}')

    # Prueba: Consultar ventas de un usuario
    print('\n=== PRUEBA: CONSULTAR VENTAS DE UN USUARIO ===')
    ventas_juan = rest.obtener_ventas_usuario('123456789')
    print(f'Juan Pérez ha realizado {len(ventas_juan)} venta(s)')
    for v in ventas_juan:
        prod = rest.buscar_producto_por_codigo(v.producto_codigo)
        print(f'  - {prod.nombre}: {v.cantidad} unidad(es)')

    # Mostrar ventas
    print('\n=== VENTAS DESPUÉS DE PRUEBA ===')
    print(f'Total de ventas: {rest.obtener_cantidad_ventas()}')
    for v in rest.listar_ventas():
        print(f'  {v}')

if __name__ == '__main__':
    main()

