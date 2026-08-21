"""
Módulo de servicio para manejo de persistencia de productos en JSON.
Centraliza la lectura y escritura de datos en archivos JSON.
Implementa manejo específico de excepciones.
"""

import json
import os
from typing import List
from modelos.producto import Producto


class ArchivoServicio:
    """
    Servicio responsable de la persistencia de productos mediante archivos JSON.
    Maneja la carga y guardado de productos con validación y manejo de excepciones específicas.

    Attributes:
        ruta_datos (str): Directorio donde se almacenan los archivos JSON.
        archivo_productos (str): Ruta completa del archivo de productos.
    """

    def __init__(self, ruta_datos: str = "datos") -> None:
        """
        Inicializa el servicio de archivo.
        Crea el directorio de datos si no existe.

        Args:
            ruta_datos (str): Directorio para almacenar archivos (por defecto: 'datos').
        """
        self.ruta_datos = ruta_datos
        self.archivo_productos = os.path.join(self.ruta_datos, "productos.json")
        self._crear_directorio_si_no_existe()

    def _crear_directorio_si_no_existe(self) -> None:
        """
        Crea el directorio de datos si no existe.

        Raises:
            PermissionError: Si no hay permisos para crear el directorio.
        """
        try:
            if not os.path.exists(self.ruta_datos):
                os.makedirs(self.ruta_datos)
        except PermissionError:
            print(f"Error: No hay permisos para crear el directorio '{self.ruta_datos}'.")
            raise

    def guardar_productos(self, productos: List[Producto]) -> bool:
        """
        Guarda la lista de productos en un archivo JSON.
        Convierte cada producto a un diccionario antes de guardar.

        Estructura JSON:
        [
            {
                "codigo": "...",
                "nombre": "...",
                "categoria": "...",
                "precio": 0.0
            },
            ...
        ]

        Args:
            productos (List[Producto]): Lista de productos a guardar.

        Returns:
            bool: True si la operación fue exitosa, False en caso contrario.

        Maneja excepciones:
            - PermissionError: Si no hay permisos de escritura.
            - isinstance: Validación del tipo de datos.
        """
        try:
            productos_lista = []

            for producto in productos:
                datos = {
                    "codigo": producto.codigo,
                    "nombre": producto.nombre,
                    "categoria": producto.categoria,
                    "precio": producto.precio
                }
                productos_lista.append(datos)

            with open(self.archivo_productos, 'w', encoding='utf-8') as archivo:
                json.dump(productos_lista, archivo, indent=4, ensure_ascii=False)

            return True

        except PermissionError:
            print(f"Error: No hay permisos para escribir en '{self.archivo_productos}'.")
            return False
        except Exception as error:
            print(f"Error al guardar productos: {error}")
            return False

    def cargar_productos(self) -> List[Producto]:
        """
        Carga la lista de productos desde el archivo JSON.
        Convierte cada diccionario recuperado en un objeto Producto.

        Returns:
            List[Producto]: Lista de objetos Producto cargados.
                           Lista vacía si el archivo no existe o hay error.

        Maneja excepciones:
            - FileNotFoundError: Si el archivo productos.json no existe.
            - json.JSONDecodeError: Si el contenido no es JSON válido.
            - PermissionError: Si no hay permisos de lectura.
            - KeyError: Si falta alguna clave esperada en los datos.
            - ValueError: Si los dados no son válidos para crear un Producto.
        """
        try:
            if not os.path.exists(self.archivo_productos):
                print(f"Información: Archivo '{self.archivo_productos}' no encontrado. Iniciando con colección vacía.")
                return []

            with open(self.archivo_productos, 'r', encoding='utf-8') as archivo:
                productos_data = json.load(archivo)

            productos: List[Producto] = []

            for datos in productos_data:
                try:
                    # Validar que todas las claves requeridas estén presentes
                    claves_requeridas = {"codigo", "nombre", "categoria", "precio"}
                    if not claves_requeridas.issubset(datos.keys()):
                        claves_faltantes = claves_requeridas - set(datos.keys())
                        print(f"Advertencia: Registro incompleto. Faltan claves: {claves_faltantes}. Omitiendo registro.")
                        continue

                    # Validar que precio es un número válido
                    try:
                        precio = float(datos["precio"])
                    except (TypeError, ValueError):
                        print(f"Advertencia: Precio inválido en producto '{datos.get('codigo', 'desconocido')}'. Omitiendo registro.")
                        continue

                    # Crear el objeto Producto con validación
                    producto = Producto(
                        codigo=datos["codigo"],
                        nombre=datos["nombre"],
                        categoria=datos["categoria"],
                        precio=precio
                    )
                    productos.append(producto)

                except ValueError as error:
                    print(f"Advertencia: Datos inválidos en registro: {error}. Omitiendo registro.")
                    continue
                except Exception as error:
                    print(f"Advertencia: Error al procesar registro: {error}. Omitiendo registro.")
                    continue

            return productos

        except FileNotFoundError:
            print(f"Información: Archivo '{self.archivo_productos}' no encontrado.")
            return []
        except json.JSONDecodeError as error:
            print(f"Error: Contenido JSON inválido en '{self.archivo_productos}': {error}.")
            return []
        except PermissionError:
            print(f"Error: No hay permisos para leer '{self.archivo_productos}'.")
            return []
        except Exception as error:
            print(f"Error al cargar productos: {error}")
            return []

