
def buscar_contrasena_expuesta(contrasena, contrasenas_expuestas):
    try:
        # Abrir el archivo en modo lectura con encoding 'latin-1'
        with open(contrasenas_expuestas, 'r', encoding='latin-1') as f:
            # Leer todas las líneas del archivo
            contrasenas = f.readlines()
            
            # Quitar los espacios en blanco al principio y final de cada línea
            contrasenas = [contrasena.strip() for contrasena in contrasenas]
            
            # Verificar si la contraseña está en la lista de contraseñas expuestas
            if contrasena in contrasenas:
                return True
            else:
                return False
    
    except FileNotFoundError:
        print(f"No se encontró el archivo '{contrasenas_expuestas}'")
        return False
    except Exception as e:
        print(f"Ocurrió un error al abrir el archivo: {e}")
        return False

# Nombre del archivo donde están las contraseñas expuestas
archivo_contrasenas = "/Users/alexperdel/Visual Studio Code/Python/BuscarContrasenas/contrasenas_expuestas.txt"

# Solicitar al usuario que ingrese la contraseña a verificar
contrasena_usuario = input("Ingresa tu contraseña para verificar si ha sido expuesta: ")

# Llamar a la función para buscar la contraseña
expuesta = buscar_contrasena_expuesta(contrasena_usuario, archivo_contrasenas)

# Mostrar el resultado al usuario
if expuesta:
    print(f"La contraseña '{contrasena_usuario}' ha sido expuesta.")
else:
    print(f"La contraseña '{contrasena_usuario}' no ha sido expuesta.")
