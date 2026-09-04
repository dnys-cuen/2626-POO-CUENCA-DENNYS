"""
Módulo de servicio para manejo de persistencia JSON.
Centraliza la lectura y escritura de datos en archivos JSON para productos, usuarios y ventas.
Implementa manejo específico de excepciones.
"""

import json
import os
from typing import List
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    """
    Servicio responsable de la persistencia mediante archivos JSON.
    Maneja la carga y guardado de productos, usuarios y ventas con validación y
    manejo específico de excepciones.

    Attributes:
        ruta_datos (str): Directorio donde se almacenan los archivos JSON.
        archivo_productos (str): Ruta completa del archivo de productos.
        archivo_usuarios (str): Ruta completa del archivo de usuarios.
        archivo_ventas (str): Ruta completa del archivo de ventas.
    """

    def __init__(self, ruta_datos: str = "datos") -> None:
        """
        Inicializa el servicio de archivo.
        Crea el directorio de datos si no existe.

        Args:
            ruta_datos (str): Directorio para almacenar archivos (por defecto: 'datos').

        Raises:
            PermissionError: Si no hay permisos para crear el directorio.
        """
        self.ruta_datos = ruta_datos
        self.archivo_productos = os.path.join(self.ruta_datos, "productos.json")
        self.archivo_usuarios = os.path.join(self.ruta_datos, "usuarios.json")
        self.archivo_ventas = os.path.join(self.ruta_datos, "ventas.json")
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

    # ==================== MÉTODOS PARA PRODUCTOS ====================

    def guardar_productos(self, productos: List[Producto]) -> bool:
        """
        Guarda la lista de productos en un archivo JSON.

        Args:
            productos (List[Producto]): Lista de productos a guardar.

        Returns:
            bool: True si la operación fue exitosa, False en caso contrario.

        Maneja excepciones:
            - PermissionError: Si no hay permisos de escritura.
        """
        try:
            productos_lista = [producto.a_diccionario() for producto in productos]

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

        Returns:
            List[Producto]: Lista de objetos Producto cargados.
                           Lista vacía si el archivo no existe o hay error.

        Maneja excepciones:
            - FileNotFoundError: Si el archivo no existe.
            - json.JSONDecodeError: Si el contenido no es JSON válido.
            - PermissionError: Si no hay permisos de lectura.
            - KeyError: Si falta alguna clave esperada.
            - ValueError: Si los datos no son válidos.
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
                    claves_requeridas = {"codigo", "nombre", "categoria", "precio", "stock"}
                    if not claves_requeridas.issubset(datos.keys()):
                        claves_faltantes = claves_requeridas - set(datos.keys())
                        print(f"Advertencia: Registro incompleto. Faltan claves: {claves_faltantes}. Omitiendo.")
                        continue

                    try:
                        precio = float(datos["precio"])
                        stock = int(datos["stock"])
                    except (TypeError, ValueError):
                        print(f"Advertencia: Datos inválidos en producto '{datos.get('codigo', 'desconocido')}'. Omitiendo.")
                        continue

                    producto = Producto(
                        codigo=datos["codigo"],
                        nombre=datos["nombre"],
                        categoria=datos["categoria"],
                        precio=precio,
                        stock=stock
                    )
                    productos.append(producto)

                except ValueError as error:
                    print(f"Advertencia: Datos inválidos: {error}. Omitiendo registro.")
                    continue
                except Exception as error:
                    print(f"Advertencia: Error al procesar registro: {error}. Omitiendo.")
                    continue

            return productos

        except FileNotFoundError:
            print(f"Información: Archivo '{self.archivo_productos}' no encontrado.")
            return []
        except json.JSONDecodeError as error:
            print(f"Error: Contenido JSON inválido en '{self.archivo_productos}': {error}")
            return []
        except PermissionError:
            print(f"Error: No hay permisos para leer '{self.archivo_productos}'.")
            return []
        except Exception as error:
            print(f"Error al cargar productos: {error}")
            return []

    # ==================== MÉTODOS PARA USUARIOS ====================

    def guardar_usuarios(self, usuarios: List[Usuario]) -> bool:
        """
        Guarda la lista de usuarios en un archivo JSON.

        Args:
            usuarios (List[Usuario]): Lista de usuarios a guardar.

        Returns:
            bool: True si la operación fue exitosa, False en caso contrario.

        Maneja excepciones:
            - PermissionError: Si no hay permisos de escritura.
        """
        try:
            usuarios_lista = [usuario.a_diccionario() for usuario in usuarios]

            with open(self.archivo_usuarios, 'w', encoding='utf-8') as archivo:
                json.dump(usuarios_lista, archivo, indent=4, ensure_ascii=False)

            return True

        except PermissionError:
            print(f"Error: No hay permisos para escribir en '{self.archivo_usuarios}'.")
            return False
        except Exception as error:
            print(f"Error al guardar usuarios: {error}")
            return False

    def cargar_usuarios(self) -> List[Usuario]:
        """
        Carga la lista de usuarios desde el archivo JSON.

        Returns:
            List[Usuario]: Lista de objetos Usuario cargados.
                          Lista vacía si el archivo no existe o hay error.

        Maneja excepciones:
            - FileNotFoundError: Si el archivo no existe.
            - json.JSONDecodeError: Si el contenido no es JSON válido.
            - PermissionError: Si no hay permisos de lectura.
            - KeyError: Si falta alguna clave esperada.
            - ValueError: Si los datos no son válidos.
        """
        try:
            if not os.path.exists(self.archivo_usuarios):
                print(f"Información: Archivo '{self.archivo_usuarios}' no encontrado. Iniciando con colección vacía.")
                return []

            with open(self.archivo_usuarios, 'r', encoding='utf-8') as archivo:
                usuarios_data = json.load(archivo)

            usuarios: List[Usuario] = []

            for datos in usuarios_data:
                try:
                    claves_requeridas = {"identificacion", "nombre", "correo"}
                    if not claves_requeridas.issubset(datos.keys()):
                        claves_faltantes = claves_requeridas - set(datos.keys())
                        print(f"Advertencia: Registro incompleto. Faltan claves: {claves_faltantes}. Omitiendo.")
                        continue

                    usuario = Usuario(
                        identificacion=datos["identificacion"],
                        nombre=datos["nombre"],
                        correo=datos["correo"]
                    )
                    usuarios.append(usuario)

                except ValueError as error:
                    print(f"Advertencia: Datos inválidos: {error}. Omitiendo registro.")
                    continue
                except Exception as error:
                    print(f"Advertencia: Error al procesar registro: {error}. Omitiendo.")
                    continue

            return usuarios

        except FileNotFoundError:
            print(f"Información: Archivo '{self.archivo_usuarios}' no encontrado.")
            return []
        except json.JSONDecodeError as error:
            print(f"Error: Contenido JSON inválido en '{self.archivo_usuarios}': {error}")
            return []
        except PermissionError:
            print(f"Error: No hay permisos para leer '{self.archivo_usuarios}'.")
            return []
        except Exception as error:
            print(f"Error al cargar usuarios: {error}")
            return []

    # ==================== MÉTODOS PARA VENTAS ====================

    def guardar_ventas(self, ventas: List[Venta]) -> bool:
        """
        Guarda la lista de ventas en un archivo JSON.

        Args:
            ventas (List[Venta]): Lista de ventas a guardar.

        Returns:
            bool: True si la operación fue exitosa, False en caso contrario.

        Maneja excepciones:
            - PermissionError: Si no hay permisos de escritura.
        """
        try:
            ventas_lista = [venta.a_diccionario() for venta in ventas]

            with open(self.archivo_ventas, 'w', encoding='utf-8') as archivo:
                json.dump(ventas_lista, archivo, indent=4, ensure_ascii=False)

            return True

        except PermissionError:
            print(f"Error: No hay permisos para escribir en '{self.archivo_ventas}'.")
            return False
        except Exception as error:
            print(f"Error al guardar ventas: {error}")
            return False

    def cargar_ventas(self) -> List[Venta]:
        """
        Carga la lista de ventas desde el archivo JSON.

        Returns:
            List[Venta]: Lista de objetos Venta cargados.
                        Lista vacía si el archivo no existe o hay error.

        Maneja excepciones:
            - FileNotFoundError: Si el archivo no existe.
            - json.JSONDecodeError: Si el contenido no es JSON válido.
            - PermissionError: Si no hay permisos de lectura.
            - KeyError: Si falta alguna clave esperada.
            - ValueError: Si los datos no son válidos.
        """
        try:
            if not os.path.exists(self.archivo_ventas):
                print(f"Información: Archivo '{self.archivo_ventas}' no encontrado. Iniciando con colección vacía.")
                return []

            with open(self.archivo_ventas, 'r', encoding='utf-8') as archivo:
                ventas_data = json.load(archivo)

            ventas: List[Venta] = []

            for datos in ventas_data:
                try:
                    claves_requeridas = {"usuario_id", "producto_codigo", "cantidad"}
                    if not claves_requeridas.issubset(datos.keys()):
                        claves_faltantes = claves_requeridas - set(datos.keys())
                        print(f"Advertencia: Registro incompleto. Faltan claves: {claves_faltantes}. Omitiendo.")
                        continue

                    try:
                        cantidad = int(datos["cantidad"])
                    except (TypeError, ValueError):
                        print(f"Advertencia: Cantidad inválida en venta. Omitiendo.")
                        continue

                    venta = Venta(
                        usuario_id=datos["usuario_id"],
                        producto_codigo=datos["producto_codigo"],
                        cantidad=cantidad
                    )
                    ventas.append(venta)

                except ValueError as error:
                    print(f"Advertencia: Datos inválidos: {error}. Omitiendo registro.")
                    continue
                except Exception as error:
                    print(f"Advertencia: Error al procesar registro: {error}. Omitiendo.")
                    continue

            return ventas

        except FileNotFoundError:
            print(f"Información: Archivo '{self.archivo_ventas}' no encontrado.")
            return []
        except json.JSONDecodeError as error:
            print(f"Error: Contenido JSON inválido en '{self.archivo_ventas}': {error}")
            return []
        except PermissionError:
            print(f"Error: No hay permisos para leer '{self.archivo_ventas}'.")
            return []
        except Exception as error:
            print(f"Error al cargar ventas: {error}")
            return []

