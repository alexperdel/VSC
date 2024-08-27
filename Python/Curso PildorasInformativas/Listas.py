# Crear una lista
frutas = ["manzana", "banana", "cereza"]

# Acceder a elementos de la lista
print("Primera fruta:", frutas[0])  # Índices empiezan en 0
print("Segunda fruta:", frutas[1])

# Agregar un elemento a la lista
frutas.append("durazno")
print("Lista después de agregar una fruta:", frutas)

# Eliminar un elemento de la lista
frutas.remove("banana")
print("Lista después de eliminar una fruta:", frutas)

# Iterar sobre una lista
for fruta in frutas:
    print("Fruta:", fruta)
