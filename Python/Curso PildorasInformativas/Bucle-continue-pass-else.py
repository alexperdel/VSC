#Uso de CONTINUE para saltar el bucle for y continuar la iteración
#Contar caracteres de una frase, saltando los espacios en blanco " "

frase = "Hola Mundo"
contador = 0

for i in frase:
    if i == " ":
        continue
    contador+=1
print(contador)

#PASS no ejecuta el bucle y devuelve NULL, porque aun no está terminado

class MiClase:
    pass

#ELSE en un for. Se ejecuta fuera de todo el bucle for. Si este no se cumple, entonces si no (else) se ejecutará

email = input("Dime tu email: ")

for i in email:
    if i == "@":
        arroba = True
        break
else:
    arroba = False
print (arroba)