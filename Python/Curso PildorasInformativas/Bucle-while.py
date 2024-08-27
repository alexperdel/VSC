i=1
while i<=10:
    print(f"Ejecución {i}")
    i=i+1
    
print("terminó While")


#VALIDAR EDAD DE USUARIO ENTRE 5 Y 100
# Solicitar la edad al usuario
edad = int(input("Dime la edad: "))

# Iniciar un bucle while que se ejecuta mientras la edad esté en el rango de 5 a 99
while edad<5 or edad>100:
    print("Edad incorrecta")
    # Solicitar de nuevo la edad al usuario
    edad = int(input("Dime la edad: "))

# Este mensaje se muestra cuando la edad está en el rango correcto
print(f"Puedes pasar, tu edad es {edad}") 


#CALCULAR RAIZ CUADRADA CON UN MAXIMO DE 2 INTENTOS
# Importar el módulo math que contiene la función sqrt para calcular la raíz cuadrada
import math

print("Programa para calcular la raíz cuadrada de un número:")
numero = int(input("Introduce el número: "))

intentos = 0

# Iniciar un bucle while que se ejecuta mientras el número sea negativo
while numero < 0:
    print("No se puede hacer la raíz de un número negativo")
    numero = int(input("Introduce el número de nuevo: "))
    if numero < 0:
        intentos += 1
    
    # Comprobar si se han alcanzado los 2 intentos
    if intentos == 2:
        print("Has alcanzado el máximo de intentos")
        break

# Si los intentos son menos de 2, significa que se ha introducido un número válido
if intentos < 2:
    solucion = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es {solucion}")


#Comprobar la edad de una persona mayor de edad, pero validando que sea un valor númerico
edad=(input("Introduce tu edad:"))

while(edad.isdigit()==False):
    print("Introduce tu edad de nuevo")
    edad=int(input("Introduce tu edad:"))

if (int(edad)<18):
    print("No tienes edad para pasar")    
else:
    print("Puedes pasar")