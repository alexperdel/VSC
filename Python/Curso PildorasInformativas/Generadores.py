#Función generadora de nº pares
def generaPares(limite):
    num=1
    miLista=[]
    
    while num<limite:
        miLista.append(num*2)
        num+=1
    
    return miLista

print(generaPares(10))


#Esto mismo pero con un Generador
def generaPares(limite):
    num=1
   
    while num<limite:
        yield num*2
        num+=1

devuelvePares=generaPares(10)

print(next(devuelvePares))
print("Líneas de código...")
print(next(devuelvePares))

#YIELD FROM para array multidimencional

def devuelveCiudad(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento: (comentado porque se simplifica con YIELD FROM)
            yield from elemento
            
ciudadesDevueltas = devuelveCiudad("Madrid", "Sevilla", "Cadíz")
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))