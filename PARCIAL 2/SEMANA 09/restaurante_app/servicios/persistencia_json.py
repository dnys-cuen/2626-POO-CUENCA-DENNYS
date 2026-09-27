"""
Módulo de persistencia de datos en JSON.
Maneja la serialización y deserialización de productos y clientes en archivos JSON.
Utiliza estructura tipo diccionario para acceso eficiente.
"""

import json
import os
from typing import Dict, List, Any
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente


class PersistenciaJSON:
    """
    Clase responsable de manejar la persistencia de datos en archivos JSON.
    
    Attributes:
        ruta_datos (str): Directorio donde se almacenan los archivos JSON.
        archivo_productos (str): Ruta del archivo de productos.
        archivo_clientes (str): Ruta del archivo de clientes.
    """
    
    def __init__(self, ruta_datos: str = "datos") -> None:
        """
        Inicializa el gestor de persistencia.
        
        Args:
            ruta_datos (str): Directorio para almacenar archivos JSON (por defecto: 'datos').
        """
        self.ruta_datos = ruta_datos
        self.archivo_productos = os.path.join(self.ruta_datos, "productos.json")
        self.archivo_clientes = os.path.join(self.ruta_datos, "clientes.json")
        
        self._crear_directorio_si_no_existe()
    
    def _crear_directorio_si_no_existe(self) -> None:
        """Crea el directorio de datos si no existe."""
        if not os.path.exists(self.ruta_datos):
            os.makedirs(self.ruta_datos)
    
    def guardar_productos(self, productos: List[Producto]) -> bool:
        """
        Guarda la lista de productos en un archivo JSON con estructura diccionario.
        
        Estructura JSON:
        {
            "codigo1": {
                "tipo": "Producto" o "Bebida",
                "nombre": "...",
                "categoria": "...",
                "precio": 0.0,
                "tamaño": "..." (solo para Bebida),
                "tipo_envase": "..." (solo para Bebida)
            },
            ...
        }
        
        Args:
            productos (List[Producto]): Lista de productos a guardar.
            
        Returns:
            bool: True si la operación fue exitosa, False en caso contrario.
        """
        try:
            productos_dict: Dict[str, Any] = {}
            
            for producto in productos:
                datos = {
                    "nombre": producto.nombre,
                    "categoria": producto.categoria,
                    "precio": producto.precio
                }
                
                # Identificar tipo de producto y agregar atributos específicos
                if isinstance(producto, Bebida):
                    datos["tipo"] = "Bebida"
                    datos["tamaño"] = producto.tamaño
                    datos["tipo_envase"] = producto.tipo_envase
                else:
                    datos["tipo"] = "Producto"
                
                productos_dict[producto.codigo] = datos
            
            with open(self.archivo_productos, 'w', encoding='utf-8') as archivo:
                json.dump(productos_dict, archivo, indent=4, ensure_ascii=False)
            
            return True
        
        except Exception as error:
            print(f"Error al guardar productos: {error}")
            return False
    
    def cargar_productos(self) -> List[Producto]:
        """
        Carga la lista de productos desde el archivo JSON.
        
        Returns:
            List[Producto]: Lista de productos cargados, o lista vacía si hay error.
        """
        try:
            if not os.path.exists(self.archivo_productos):
                return []
            
            with open(self.archivo_productos, 'r', encoding='utf-8') as archivo:
                productos_dict = json.load(archivo)
            
            productos: List[Producto] = []
            
            for codigo, datos in productos_dict.items():
                if datos.get("tipo") == "Bebida":
                    bebida = Bebida(
                        codigo=codigo,
                        nombre=datos["nombre"],
                        categoria=datos["categoria"],
                        precio=datos["precio"],
                        tamaño=datos["tamaño"],
                        tipo_envase=datos["tipo_envase"]
                    )
                    productos.append(bebida)
                else:
                    producto = Producto(
                        codigo=codigo,
                        nombre=datos["nombre"],
                        categoria=datos["categoria"],
                        precio=datos["precio"]
                    )
                    productos.append(producto)
            
            return productos
        
        except Exception as error:
            print(f"Error al cargar productos: {error}")
            return []
    
    def guardar_clientes(self, clientes: List[Cliente]) -> bool:
        """
        Guarda la lista de clientes en un archivo JSON con estructura diccionario.
        
        Estructura JSON:
        {
            "identificacion1": {
                "nombre": "...",
                "correo": "..."
            },
            ...
        }
        
        Args:
            clientes (List[Cliente]): Lista de clientes a guardar.
            
        Returns:
            bool: True si la operación fue exitosa, False en caso contrario.
        """
        try:
            clientes_dict: Dict[str, Any] = {}
            
            for cliente in clientes:
                clientes_dict[cliente.identificacion] = {
                    "nombre": cliente.nombre,
                    "correo": cliente.correo
                }
            
            with open(self.archivo_clientes, 'w', encoding='utf-8') as archivo:
                json.dump(clientes_dict, archivo, indent=4, ensure_ascii=False)
            
            return True
        
        except Exception as error:
            print(f"Error al guardar clientes: {error}")
            return False
    
    def cargar_clientes(self) -> List[Cliente]:
        """
        Carga la lista de clientes desde el archivo JSON.
        
        Returns:
            List[Cliente]: Lista de clientes cargados, o lista vacía si hay error.
        """
        try:
            if not os.path.exists(self.archivo_clientes):
                return []
            
            with open(self.archivo_clientes, 'r', encoding='utf-8') as archivo:
                clientes_dict = json.load(archivo)
            
            clientes: List[Cliente] = []
            
            for identificacion, datos in clientes_dict.items():
                cliente = Cliente(
                    identificacion=identificacion,
                    nombre=datos["nombre"],
                    correo=datos["correo"]
                )
                clientes.append(cliente)
            
            return clientes
        
        except Exception as error:
            print(f"Error al cargar clientes: {error}")
            return []
