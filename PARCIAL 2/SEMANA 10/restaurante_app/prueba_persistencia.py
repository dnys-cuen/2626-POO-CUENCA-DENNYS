"""
Script de prueba automatizado para verificar la persistencia de productos.
Esta prueba simula el flujo completo de carga, guardado y recuperación de datos.
"""

import os
import json
from modelos.producto import Producto
from servicios.restaurante import Restaurante


def prueba_completa() -> None:
    """Ejecuta una serie de pruebas para validar la funcionalidad del sistema."""

    print("\n" + "=" * 70)
    print("PRUEBA DE PERSISTENCIA DE PRODUCTOS - SEMANA 10")
    print("=" * 70)

    # PRUEBA 1: Crear restaurante e intentar cargar (debe estar vacío al inicio)
    print("\n[PRUEBA 1] Inicialización del Restaurante")
    print("-" * 70)
    restaurante = Restaurante()
    restaurante.cargar_productos_desde_archivo()
    cantidad_inicial = restaurante.obtener_cantidad_productos()
    print(f"✓ Restaurante inicializado")
    print(f"  Cantidad de productos cargados: {cantidad_inicial}")

    # PRUEBA 2: Registrar productos
    print("\n[PRUEBA 2] Registrar Productos")
    print("-" * 70)

    try:
        producto1 = Producto("P001", "Coca Cola", "Bebidas", 2.50)
        resultado1 = restaurante.registrar_producto(producto1)
        print(f"✓ Producto 1 registrado: {resultado1}")
        print(f"  {producto1.mostrar_informacion()}")

        producto2 = Producto("P002", "Pizza Margherita", "Pizzas", 12.99)
        resultado2 = restaurante.registrar_producto(producto2)
        print(f"✓ Producto 2 registrado: {resultado2}")
        print(f"  {producto2.mostrar_informacion()}")

        producto3 = Producto("P003", "Ensalada César", "Ensaladas", 8.50)
        resultado3 = restaurante.registrar_producto(producto3)
        print(f"✓ Producto 3 registrado: {resultado3}")
        print(f"  {producto3.mostrar_informacion()}")

    except ValueError as e:
        print(f"✗ Error: {e}")
        return

    # PRUEBA 3: Listar productos
    print("\n[PRUEBA 3] Listar Productos")
    print("-" * 70)
    productos_info = restaurante.listar_productos()
    print(f"Total de productos en memoria: {restaurante.obtener_cantidad_productos()}")
    for i, info in enumerate(productos_info, 1):
        print(f"  {i}. {info}")

    # PRUEBA 4: Verificar archivo JSON
    print("\n[PRUEBA 4] Verificar Archivo JSON")
    print("-" * 70)
    ruta_json = "datos/productos.json"
    if os.path.exists(ruta_json):
        print(f"✓ Archivo {ruta_json} existe")
        try:
            with open(ruta_json, 'r', encoding='utf-8') as f:
                datos_json = json.load(f)
            print(f"✓ JSON válido con {len(datos_json)} producto(s)")
            print("  Contenido:")
            print(json.dumps(datos_json, indent=4, ensure_ascii=False))
        except json.JSONDecodeError as e:
            print(f"✗ Error al leer JSON: {e}")
    else:
        print(f"✗ Archivo {ruta_json} no encontrado")
        return

    # PRUEBA 5: Buscar producto
    print("\n[PRUEBA 5] Buscar Producto por Código")
    print("-" * 70)
    producto_encontrado = restaurante.buscar_producto_por_codigo("P002")
    if producto_encontrado:
        print(f"✓ Producto encontrado: {producto_encontrado.mostrar_informacion()}")
    else:
        print("✗ Producto no encontrado")

    # PRUEBA 6: Actualizar producto
    print("\n[PRUEBA 6] Actualizar Producto")
    print("-" * 70)
    try:
        actualizado = restaurante.actualizar_producto("P002", nuevo_precio=15.99)
        if actualizado:
            print(f"✓ Producto actualizado")
            producto_act = restaurante.buscar_producto_por_codigo("P002")
            print(f"  {producto_act.mostrar_informacion()}")
        else:
            print("✗ No se pudo actualizar el producto")
    except ValueError as e:
        print(f"✗ Error: {e}")

    # PRUEBA 7: Verificar cambio en archivo JSON
    print("\n[PRUEBA 7] Verificar Cambio en JSON")
    print("-" * 70)
    with open(ruta_json, 'r', encoding='utf-8') as f:
        datos_json = json.load(f)
    precio_actualizado = next((p["precio"] for p in datos_json if p["codigo"] == "P002"), None)
    print(f"✓ Precio de P002 en JSON: ${precio_actualizado}")

    # PRUEBA 8: Crear nuevo restaurante y cargar datos
    print("\n[PRUEBA 8] Cargar Datos en Nuevo Restaurante")
    print("-" * 70)
    restaurante2 = Restaurante()
    restaurante2.cargar_productos_desde_archivo()
    cantidad_cargada = restaurante2.obtener_cantidad_productos()
    print(f"✓ Productos cargados en nuevo restaurante: {cantidad_cargada}")

    if cantidad_cargada == 3:
        print("✓ La cantidad es correcta")
    else:
        print(f"✗ Se esperaban 3 productos, se cargaron {cantidad_cargada}")

    # PRUEBA 9: Verificar que los datos son idénticos
    print("\n[PRUEBA 9] Verificar Integridad de Datos")
    print("-" * 70)
    productos_cargados = restaurante2.listar_productos()
    for i, info in enumerate(productos_cargados, 1):
        print(f"  {i}. {info}")

    # PRUEBA 10: Eliminar producto
    print("\n[PRUEBA 10] Eliminar Producto")
    print("-" * 70)
    eliminado = restaurante2.eliminar_producto("P001")
    if eliminado:
        print("✓ Producto P001 eliminado")
        print(f"  Productos restantes: {restaurante2.obtener_cantidad_productos()}")
    else:
        print("✗ No se pudo eliminar el producto")

    # PRUEBA 11: Verificar eliminación en JSON
    print("\n[PRUEBA 11] Verificar Eliminación en JSON")
    print("-" * 70)
    with open(ruta_json, 'r', encoding='utf-8') as f:
        datos_json = json.load(f)
    print(f"✓ Productos en JSON ahora: {len(datos_json)}")
    if len(datos_json) == 2:
        print("✓ Eliminación correctamente persistida")
    else:
        print(f"✗ Se esperaban 2 productos, hay {len(datos_json)}")

    # PRUEBA 12: Crear tercer restaurante para verificar persistencia total
    print("\n[PRUEBA 12] Verificar Persistencia Total")
    print("-" * 70)
    restaurante3 = Restaurante()
    restaurante3.cargar_productos_desde_archivo()
    cantidad_final = restaurante3.obtener_cantidad_productos()
    print(f"✓ Cantidad final de productos: {cantidad_final}")
    if cantidad_final == 2:
        print("✓ PERSISTENCIA CONFIRMADA: Los datos se conservan entre ejecuciones")
    else:
        print(f"✗ Se esperaban 2 productos finales, hay {cantidad_final}")

    # PRUEBA 13: Prueba de validación de precio negativo
    print("\n[PRUEBA 13] Validación de Precio Negativo")
    print("-" * 70)
    try:
        producto_invalido = Producto("P999", "Producto Inválido", "Test", -5.00)
        print("✗ No se lanzó excepción para precio negativo")
    except ValueError as e:
        print(f"✓ Excepción capturada correctamente: {e}")

    print("\n" + "=" * 70)
    print("PRUEBAS COMPLETADAS")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    prueba_completa()

