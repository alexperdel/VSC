# Crear un diccionario
persona = {
    "nombre": "Juan",
    "edad": 20,
    "ciudad": "Madrid"
}

# Acceder a valores del diccionario
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])

# Modificar el valor de una clave
persona["edad"] = 21
print("Edad modificada:", persona["edad"])

# Agregar un nuevo par clave-valor
persona["profesión"] = "Estudiante"
print("Diccionario después de agregar una profesión:", persona)

# Eliminar un par clave-valor
del persona["ciudad"]
print("Diccionario después de eliminar la ciudad:", persona)

# Obtener todas las claves del diccionario
claves = persona.keys()
print("Claves del diccionario:", list(claves))

# Obtener todos los valores del diccionario
valores = persona.values()
print("Valores del diccionario:", list(valores))

# Obtener todos los pares clave-valor del diccionario
items = persona.items()
print("Pares clave-valor del diccionario:", list(items))

# Iterar sobre las claves
for clave in persona.keys():
    print("Clave:", clave)

# Iterar sobre los valores
for valor in persona.values():
    print("Valor:", valor)

# Iterar sobre los pares clave-valor
for clave, valor in persona.items():
    print(clave, ":", valor)

# Usar el método get para acceder a un valor
profesion = persona.get("profesión", "Desconocido")
print("Profesión:", profesion)

# Acceder a una clave inexistente usando get
direccion = persona.get("dirección", "No disponible")
print("Dirección:", direccion)

# Diccionario anidado
estudiante = {
    "nombre": "Ana",
    "edad": 22,
    "cursos": {
        "matemáticas": 95,
        "literatura": 88
    }
}

print("Diccionario de estudiante:", estudiante)
print("Nota en matemáticas:", estudiante["cursos"]["matemáticas"])


# Crear un diccionario de contactos
contactos = {
    "Juan": {
        "telefono": "123-456-7890",
        "email": "juan@example.com"
    },
    "Ana": {
        "telefono": "987-654-3210",
        "email": "ana@example.com"
    }
}

# Acceder a los datos de un contacto
print("Teléfono de Juan:", contactos["Juan"]["telefono"])
print("Email de Ana:", contactos["Ana"]["email"])

# Agregar un nuevo contacto
contactos["Pedro"] = {
    "telefono": "555-555-5555",
    "email": "pedro@example.com"
}
print("Diccionario después de agregar a Pedro:", contactos)

# Modificar el email de Ana
contactos["Ana"]["email"] = "ana.nueva@example.com"
print("Email de Ana modificado:", contactos["Ana"]["email"])

# Eliminar un contacto
del contactos["Juan"]
print("Diccionario después de eliminar a Juan:", contactos)


