import math

# Definición de la función calculaRaiz que calcula la raíz cuadrada de un número
def calculaRaiz(num1):
    if num1 < 0:
        # Si el número es negativo, lanzar una excepción de tipo ValueError con un mensaje descriptivo
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num1)

op1 = int(input("Introduce un número: "))

# Intentar ejecutar el bloque de código que puede causar una excepción
try:
    # Intentar calcular la raíz cuadrada del número introducido
    print(calculaRaiz(op1))
# Capturar la excepción ValueError si se lanza
except ValueError as ErrorDeNumeroNegativo:
    # Imprimir el mensaje de error contenido en la excepción
    print(ErrorDeNumeroNegativo)

print("Programa terminado")
