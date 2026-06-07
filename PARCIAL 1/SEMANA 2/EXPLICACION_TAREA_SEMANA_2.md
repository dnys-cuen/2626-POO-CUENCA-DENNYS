# Explicación detallada del programa: `CuentaBancaria`

Este documento explica paso a paso el contenido de `TAREA SEMANA 2.py` y conceptos básicos de Programación Orientada a Objetos (POO) necesarios para entenderlo. Está escrito para alguien que está empezando.

Archivo relevante: [PARCIAL 1/SEMANA 2/TAREA SEMANA 2.py](PARCIAL%201/SEMANA%202/TAREA%20SEMANA%202.py)

---

## 1. Objetivo del programa

El programa define una clase llamada `CuentaBancaria` que representa una cuenta bancaria simple. Permite crear cuentas, depositar dinero, retirar dinero y mostrar el saldo. Además incluye un ejemplo de uso en una función `ejemplo_uso()` que se ejecuta cuando el archivo se ejecuta como programa principal.

## 2. Conceptos básicos de POO usados en este programa

- **Clase:** Es una plantilla o molde que define cómo es un tipo de objeto. En este caso, `CuentaBancaria` es la clase.
- **Objeto / Instancia:** Es un ejemplar concreto de la clase. Por ejemplo, `cuenta = CuentaBancaria(...)` crea un objeto.
- **Atributos:** Son las variables que pertenecen a la instancia (por ejemplo, `titular`, `numero`, `saldo`).
- **Métodos:** Son funciones definidas dentro de la clase que operan sobre sus atributos (por ejemplo, `depositar`, `retirar`).
- **Encapsulación (básica):** Organización del estado (atributos) y comportamiento (métodos) dentro de la clase.

## 3. Código: explicación por secciones

A continuación se muestra cada parte importante del archivo y su explicación.

### a) Definición de la clase

```python
class CuentaBancaria:
    """Representa una cuenta bancaria simple."""

    def __init__(self, titular: str, numero: str, saldo: float = 0.0):
        self.titular = titular
        self.numero = numero
        self.saldo = float(saldo)
```

- `class CuentaBancaria:` declara la clase.
- `__init__` es el método constructor: se ejecuta cuando creas una nueva instancia. Recibe parámetros para inicializar los atributos.
- `self` es una referencia al objeto actual. Dentro de los métodos, se usa `self.atributo` para acceder o asignar atributos de la instancia.
- Aquí se asignan tres atributos: `titular` (nombre del dueño), `numero` (identificador de la cuenta) y `saldo` (saldo inicial convertido a `float`).

### b) Método `depositar`

```python
    def depositar(self, cantidad: float) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser positiva.")
        self.saldo += cantidad
```

- `depositar` recibe una `cantidad` y la suma al `saldo`.
- Valida que la cantidad sea positiva; si no, lanza un `ValueError` (excepción) para indicar uso incorrecto.
- No devuelve nada (`-> None`).

### c) Método `retirar`

```python
    def retirar(self, cantidad: float) -> bool:
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.saldo:
            return False
        self.saldo -= cantidad
        return True
```

- `retirar` intenta restar `cantidad` del `saldo`.
- Si la cantidad es negativa o cero, lanza `ValueError`.
- Si no hay fondos suficientes, devuelve `False` y no cambia el saldo.
- Si la operación es exitosa, resta la cantidad y devuelve `True`. El valor devuelto permite al código que llama saber si el retiro funcionó.

### d) Método `mostrar_saldo` y `__str__`

```python
    def mostrar_saldo(self) -> str:
        return f"Titular: {self.titular} | Nº: {self.numero} | Saldo: ${self.saldo:.2f}"

    def __str__(self) -> str:
        return self.mostrar_saldo()
```

- `mostrar_saldo` devuelve una cadena con la información de la cuenta y el saldo formateado con dos decimales.
- `__str__` es un método especial que define cómo se representa la instancia cuando se usa `print(cuenta)` o `str(cuenta)`. Aquí delega en `mostrar_saldo()`.

### e) Ejemplo de uso y punto de entrada

```python
def ejemplo_uso():
    cuenta = CuentaBancaria("Denys Cuenca", "ES12 3456 7890 1234", 150.0)
    print("Cuenta creada:")
    print(cuenta)

    print("\nDepositando $50...")
    cuenta.depositar(50)
    print(cuenta)

    print("\nIntentando retirar $220...")
    fue_retirado = cuenta.retirar(220)
    print("Retiro exitoso" if fue_retirado else "Fondos insuficientes")
    print(cuenta)

    print("\nRetirando $100...")
    cuenta.retirar(100)
    print(cuenta)


if __name__ == "__main__":
    ejemplo_uso()
```

- `ejemplo_uso()` crea una instancia y demuestra llamadas a los métodos `depositar` y `retirar`.
- `if __name__ == "__main__":` comprueba si el archivo se ejecuta directamente (no importado). Si es así, ejecuta `ejemplo_uso()`.

## 4. Cómo ejecutar el programa

Desde PowerShell (o cualquier terminal), navega a la carpeta que contiene el archivo y ejecuta:

```powershell
python "PARCIAL 1/SEMANA 2/TAREA SEMANA 2.py"
```

Salida de ejemplo esperada:

```
Cuenta creada:
Titular: Denys Cuenca | Nº: ES12 3456 7890 1234 | Saldo: $150.00

Depositando $50...
Titular: Denys Cuenca | Nº: ES12 3456 7890 1234 | Saldo: $200.00

Intentando retirar $220...
Fondos insuficientes
Titular: Denys Cuenca | Nº: ES12 3456 7890 1234 | Saldo: $200.00

Retirando $100...
Titular: Denys Cuenca | Nº: ES12 3456 7890 1234 | Saldo: $100.00
```

Dependiendo de tu versión de Python y del formato regional, la representación del número podría variar ligeramente.

## 5. Siguientes pasos recomendados para aprender

- Intenta añadir validaciones adicionales: por ejemplo, un límite máximo de depósito o cargos por retiro.
- Haz que los atributos `saldo` y `numero` sean "privados" (convención `_saldo`) y añade métodos para accederlos si quieres controlar más el acceso.
- Implementa otra clase, por ejemplo `Cliente` o `Tarjeta`, y crea relaciones entre clases (composición).
- Lee sobre conceptos como herencia y polimorfismo para ampliar la POO.

---

Si quieres, puedo:
- Añadir comentarios en línea directamente en el archivo `.py`.
- Crear ejercicios complementarios para practicar.
- Reescribir el ejemplo usando otra entidad, por ejemplo `Automovil` o `Libro`.

¿Qué prefieres que haga a continuación?
