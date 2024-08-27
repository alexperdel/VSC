# Crear una tupla
colores = ("rojo", "verde", "azul")

# Acceder a elementos de la tupla
print("Primer color:", colores[0])
print("Segundo color:", colores[1])

# Las tuplas son inmutables, no se pueden modificar
# colores[0] = "amarillo"  # Esto daría un error

# Desempaquetar una tupla
rojo, verde, azul = colores
print("Colores desempaquetados:", rojo, verde, azul)

# Crear una tupla con un solo elemento (nota la coma al final)
tupla_un_elemento = ("rojo",)
print("Tupla con un solo elemento:", tupla_un_elemento)

# Acceder a elementos de una tupla
print("Primer color:", colores[0])
print("Segundo color:", colores[1])

# Desempaquetar una tupla en variables
rojo, verde, azul = colores
print("Colores desempaquetados:", rojo, verde, azul)

# Convertir una tupla en una lista
lista_colores = list(colores)
print("Lista de colores convertida desde tupla:", lista_colores)

# Ahora podemos modificar la lista
lista_colores.append("amarillo")
print("Lista de colores después de agregar un elemento:", lista_colores)

# Convertir una lista en una tupla
nueva_tupla_colores = tuple(lista_colores)
print("Tupla de colores convertida desde lista:", nueva_tupla_colores)

# Crear una tupla inicial
mi_tupla = (1, 2, 3, 4)
print("Tupla original:", mi_tupla)

# Convertir la tupla en una lista para modificarla
mi_lista = list(mi_tupla)
print("Lista convertida desde tupla:", mi_lista)

# Modificar la lista
mi_lista.append(5)
mi_lista[0] = 0
print("Lista modificada:", mi_lista)

# Convertir la lista modificada de nuevo en una tupla
mi_tupla_modificada = tuple(mi_lista)
print("Tupla modificada:", mi_tupla_modificada)

# Iterar sobre una tupla
for color in colores:
    print("Color:", color)

# Contar cuántas veces aparece un elemento en una tupla
frutas = ("manzana", "banana", "cereza", "manzana")
conteo_manzanas = frutas.count("manzana")
print("Número de manzanas en la tupla:", conteo_manzanas)

# Encontrar el índice de un elemento en una tupla
indice_cereza = frutas.index("cereza")
print("Índice de cereza en la tupla:", indice_cereza)
