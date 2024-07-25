#Ejemplo de Try Except

try:
    valor = int(input("Ingresa un número: "))
    resultado = 10 / valor
    print(f"El resultado es {resultado}")
except ValueError:
    print("Por favor, ingresa un número válido.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")

