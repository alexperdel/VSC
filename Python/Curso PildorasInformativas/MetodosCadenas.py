nombreUsuario = input("Introduce tu nombre de usuario: ")
print("Tu nombre de usuario es:", nombreUsuario)

# Método para pasar a mayúsculas
print("Tu nombre de usuario en mayúsculas es:", nombreUsuario.upper())

# Método para pasar a minúsculas
print("Tu nombre de usuario en minúsculas es:", nombreUsuario.lower())

# Método para capitalizar (primera letra en mayúscula)
print("Tu nombre de usuario capitalizado es:", nombreUsuario.capitalize())

# Método para contar el número de veces que aparece una letra
letra = input("Introduce una letra para contar en tu nombre de usuario: ")
print(f"La letra '{letra}' aparece {nombreUsuario.count(letra)} veces en tu nombre de usuario.")

# Método para encontrar la posición de una letra
posicion = nombreUsuario.find(letra)
if posicion != -1:
    print(f"La letra '{letra}' se encuentra en la posición {posicion} de tu nombre de usuario.")
else:
    print(f"La letra '{letra}' no se encuentra en tu nombre de usuario.")

# Método para verificar si la cadena es alfanumérica
print("¿Tu nombre de usuario es alfanumérico?", nombreUsuario.isalnum())

# Método para verificar si la cadena está en mayúsculas
print("¿Tu nombre de usuario está en mayúsculas?", nombreUsuario.isupper())

# Método para verificar si la cadena está en minúsculas
print("¿Tu nombre de usuario está en minúsculas?", nombreUsuario.islower())

# Método para reemplazar una letra por otra
letra_a_reemplazar = input("Introduce la letra que deseas reemplazar: ")
nueva_letra = input("Introduce la nueva letra: ")
print(f"Tu nombre de usuario después de reemplazar '{letra_a_reemplazar}' por '{nueva_letra}' es:", nombreUsuario.replace(letra_a_reemplazar, nueva_letra))

# Método para verificar si la cadena empieza con una letra específica
letra_inicial = input("Introduce una letra para verificar si tu nombre de usuario empieza con ella: ")
print(f"¿Tu nombre de usuario empieza con '{letra_inicial}'?", nombreUsuario.startswith(letra_inicial))

# Método para verificar si la cadena termina con una letra específica
letra_final = input("Introduce una letra para verificar si tu nombre de usuario termina con ella: ")
print(f"¿Tu nombre de usuario termina con '{letra_final}'?", nombreUsuario.endswith(letra_final))


