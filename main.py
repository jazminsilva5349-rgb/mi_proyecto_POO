# Importamos las clases desde nuestro módulo modelos.py
from modelos import CuentaBancaria, CuentaPremium


def ejecutar_pruebas():
    print("=== INICIANDO PRUEBAS DEL SISTEMA BANCARIO ===\n")

    # 1. Instanciación de objetos (Clase Base y Subclase)
    cuenta_1 = CuentaBancaria("001", "Ana López", 1500, "Ahorro")
    cuenta_2 = CuentaBancaria("002", "Carlos Pérez", 500, "Crédito")
    cuenta_premium = CuentaPremium("003", "María Gómez", 3000, "Crédito", "Bonificación anual")

    # 2. Prueba de Encapsulamiento y Operaciones
    print("--- Operaciones y Encapsulamiento ---")
    cuenta_1.depositar(500)
    cuenta_1.retirar(300)
    print(f"Consulta mediante getter (Encapsulamiento): ${cuenta_1.get_saldo()}\n")

    cuenta_2.retirar(200)
    cuenta_2.consultar_saldo()
    print()

    # 3. Prueba de Herencia y Polimorfismo
    print("--- Herencia y Polimorfismo (mostrar_info sobrescrito) ---")
    cuenta_1.mostrar_info()
    print()
    cuenta_premium.depositar(1000)
    cuenta_premium.mostrar_info()

    # 4. Prueba de Composición (Delegación hacia objetos Transaccion)
    print("\n--- Composición (Historial de Transacciones) ---")
    cuenta_1.mostrar_historial()
    cuenta_premium.mostrar_historial()


# Punto de entrada estándar en Python
if __name__ == "__main__":
    ejecutar_pruebas()
