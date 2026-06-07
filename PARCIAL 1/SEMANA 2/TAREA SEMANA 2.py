
class CuentaBancaria:
	"""Representa una cuenta bancaria simple."""

	def __init__(self, titular: str, numero: str, saldo: float = 0.0):
		self.titular = titular
		self.numero = numero
		self.saldo = float(saldo)

	def depositar(self, cantidad: float) -> None:
		if cantidad <= 0:
			raise ValueError("La cantidad a depositar debe ser positiva.")
		self.saldo += cantidad

	def retirar(self, cantidad: float) -> bool:
		if cantidad <= 0:
			raise ValueError("La cantidad a retirar debe ser positiva.")
		if cantidad > self.saldo:
			return False
		self.saldo -= cantidad
		return True

	def mostrar_saldo(self) -> str:
		return f"Titular: {self.titular} | Nº: {self.numero} | Saldo: ${self.saldo:.2f}"

	def __str__(self) -> str:
		return self.mostrar_saldo()


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

