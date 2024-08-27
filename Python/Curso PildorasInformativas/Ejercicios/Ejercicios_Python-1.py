#EJERCICIO 1
#Pedir 2 numeros por teclado
numero1 = int(input("Introduce nº1: "))
numero2 = int(input("Introduce nº2: "))

#Funcion que devuelve el mayor nº
def devuelveMax (numero1, numero2):
    if numero1>numero2:
        return (numero1)
    elif numero2>numero1:
        return (numero2)
    else:
        return ("Son iguales")
        
#Obtener resultado
resultado = devuelveMax(numero1, numero2)

#Imrpimir en pantalla el resultado        
print ("El numero más alto es: ", resultado)

#EJERCICIO 2
#Pedir datos personales

nombre= input("Introduce el nombre: ")
direccion= input("Introduce la dirección: ")
telefono = int(input("Introduce el teléfono: "))

#Crear el diccionario
contacto ={
    "Nombre" : nombre,
    "Dirección" : direccion,
    "Teléfono" : telefono
}

#Obtener todos los valores del diccionario
valores = contacto.values()
print("Los datos personales son: ", list(valores))

#EJERCICIO3
#Pedir 2 numeros por teclado
numero1 = int(input("Introduce nº1: "))
numero2 = int(input("Introduce nº1: "))
numero3 = int(input("Introduce nº1: "))

#Calculo de la media
media = (numero1+numero2+numero3)/3

valorMedio = media

print("El valor medio es: ", valorMedio)
    