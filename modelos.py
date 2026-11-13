from datetime import datetime


# --- CLASE AUXILIAR PARA COMPOSICIÓN ---
class Transaccion:
    """Representa un movimiento individual dentro de una cuenta bancaria."""
    def __init__(self, tipo_movimiento, monto):
        self.tipo_movimiento = tipo_movimiento
        self.monto = monto
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def obtener_detalle(self):
        return f"[{self.fecha}] {self.tipo_movimiento}: ${self.monto}"


# --- CLASE BASE ---
class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo_inicial, tipo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.__saldo = saldo_inicial  # Encapsulamiento: atributo privado
        self.tipo = tipo
        
        # COMPOSICIÓN: Una CuentaBancaria "tiene-una" colección de objetos Transaccion
        self.historial = []
        if saldo_inicial > 0:
            self.historial.append(Transaccion("Apertura de cuenta", saldo_inicial))

    # Getter para acceder de forma segura al saldo encapsulado
    def get_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            self.historial.append(Transaccion("Depósito", monto))
            print(f"Depósito exitoso de ${monto}. Nuevo saldo: ${self.__saldo}")
        else:
            print("El monto a depositar debe ser mayor a cero.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            self.historial.append(Transaccion("Retiro", monto))
            print(f"Retiro de ${monto} realizado. Saldo restante: ${self.__saldo}")
        else:
            print(f"Fondos insuficientes o monto inválido. Saldo actual: ${self.__saldo}")

    def consultar_saldo(self):
        print(f"El saldo de la cuenta {self.numero_cuenta} es: ${self.__saldo}")

    def mostrar_info(self):
        print(f"Cuenta: {self.numero_cuenta} | Titular: {self.titular}")
        print(f"Tipo: {self.tipo} | Saldo: ${self.__saldo}")

    # DELEGACIÓN: Invoca el método obtener_detalle() de cada objeto Transaccion contenido
    def mostrar_historial(self):
        print(f"\n--- Historial de movimientos (Cuenta {self.numero_cuenta} - {self.titular}) ---")
        for transaccion in self.historial:
            print(transaccion.obtener_detalle())
        print("-" * 58)


# --- SUBCLASE (Herencia + Polimorfismo) ---
class CuentaPremium(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo_inicial, tipo, beneficios):
        super().__init__(numero_cuenta, titular, saldo_inicial, tipo)
        self.beneficios = beneficios

    # Polimorfismo: sobrescribe mostrar_info() accediendo al saldo vía get_saldo()
    def mostrar_info(self):
        print(f"Cuenta Premium: {self.numero_cuenta} | Titular: {self.titular}")
        print(f"Tipo: {self.tipo} | Saldo: ${self.get_saldo()} | Beneficios: {self.beneficios}")
