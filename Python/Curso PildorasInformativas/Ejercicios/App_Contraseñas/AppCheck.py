from io import open

# Función para verificar la contraseña
def verificar_contrasena(contrasena):
    try:
        with open("/Users/alexperdel/Visual Studio Code/Python/Curso PildorasInformativas/Ejercicios/App_Contraseñas/contrasenas_expuestas.txt", "r", encoding='latin-1') as archivo:
            contrasenas = archivo.read().splitlines()
        return contrasena in contrasenas

    except FileNotFoundError:
        return None
    
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
        return None
