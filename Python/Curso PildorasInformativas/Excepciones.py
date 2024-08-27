# Definición de funciones matemáticas básicas

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplica(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación errónea"

# Solicitar al usuario que introduzca los números para la operación
#Con un bucle infinito para que siempre nos obligue a meter un número y no de errores
while True:
    try:
        op1 = int(input("Introduce el primer número: "))
        op2 = int(input("Introduce el segundo número: "))
        break
    except ValueError:
        print("Valores incorrectos, prueba otra vez.")

# Solicitar al usuario que introduzca la operación a realizar
operacion = input("Introduce la operación a realizar (suma, resta, multiplica, divide): ")
operacion = operacion.lower()

# Realizar la operación solicitada
if operacion == "suma":
    print(suma(op1, op2))
elif operacion == "resta":
    print(resta(op1, op2))
elif operacion == "multiplica":
    print(multiplica(op1, op2))
elif operacion == "divide":
    print(divide(op1, op2))
else:
    print("Operación no contemplada")

# Informar al usuario que la operación ha sido ejecutada
print("Operación ejecutada. Continuación de ejecución del programa")
