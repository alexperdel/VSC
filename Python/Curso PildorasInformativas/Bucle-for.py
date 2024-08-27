# Iterar sobre cada elemento en la lista
for i in ["ejemplo", "python", "for", 2]:
    # Imprimir "Hola" seguido de un espacio en lugar de un salto de línea
    print("Hola", end=" ")
    
    
    
#COMPROBAR EMAIL CON FOR Y VARIABLE CONTADOR
# Inicializar contadores para arroba y punto
arroba = 0
punto = 0

# Solicitar el email al usuario
miEmail = input("Introduce mail: ")

# Recorrer cada carácter del email
for i in miEmail:
    # Si el carácter es "@", incrementar el contador de arrobas
    if i == "@":
        arroba += 1
    # Si el carácter es ".", incrementar el contador de puntos
    elif i == ".":
        punto += 1

# Comprobar si el email es correcto
# Debe tener exactamente una arroba y al menos un punto
if arroba == 1 and punto >= 1:
    print("Mail correcto")
else:
    print("Mail erróneo")
    
    

# Iterar del 0 al 4 (5 números en total)
for i in range(5):
    # Imprimir el valor actual de i usando una f-string
    print(f"valor de {i}")

# Iterar desde 2 hasta 39 (no incluye 40) con un paso de 4
for i in range(2, 40, 4):
    # Imprimir el valor actual de i usando una f-string
    print(f"valor de {i}")
    
    

    
#COMPROBAR EMAIL CON FOR Y RANGE
# Inicializar contadores para arroba y punto
arroba = 0
punto = 0

# Solicitar el email al usuario
miEmail = input("Introduce mail: ")

# Recorrer cada carácter del email usando su índice
for i in range(len(miEmail)):
    if miEmail[i] == "@":
        arroba += 1
    elif miEmail[i] == ".":
        punto += 1

# Comprobar si el email es correcto
if arroba == 1 and punto >= 1:
    print("Mail OK")
else:
    print("Mail mal")
