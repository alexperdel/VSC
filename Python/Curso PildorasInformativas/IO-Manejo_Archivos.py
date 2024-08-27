from io import open

#'r': Modo de lectura.
#'w': Modo de escritura.
#'a': Modo de apéndice.
#'r+': Modo de lectura y escritura.

archivoTexto = open(r"/Users/alexperdel/Visual Studio Code/Python/archivo.txt","r+")


#Crear el contenido del archivo a través de una variable
frase="Creando nueva frase en archivo.txt"

#Variable para leer el contenido del archivo.txt que luego se declara
texto=archivoTexto.read()
print(texto)

#Crear una variable que a través de .readlines() crea una [lista] que se puede matipular
lineasTexto=archivoTexto.readlines()
print(lineasTexto)
print(lineasTexto[0]) #Acceder al elemento dentro de la lista

#Si tenemos activo el modo 'a'. Agregamos nuevo contenido con .whrite()
archivoTexto.write("Nuevo texto que se almacena")

#Colocar el cursor a partir de la posición 5 y leer desde
archivoTexto.seek(5)
print(archivoTexto.read())

#Colocar el cursor al final de la primera linea y luego lee
archivoTexto.seek(len(archivoTexto.readline()))
print(archivoTexto.read())

#Colocar el cursor en la mitad y leer desde ahí
archivoTexto.seek(len(archivoTexto.read())/2)
print(archivoTexto.read())

#Cerrar el archivo
archivoTexto.close()

#Incluir nuevo texto dentro del comumento a través de la lista y una variable
nuevoTexto=archivoTexto.readlines() #Esto lo convierte en un array
nuevoTexto[1]="Esta linea ha sido incluida desde el exterior"
archivoTexto.seek(0) #Esto coloca el cursor al inicio
archivoTexto.writelines(nuevoTexto) 

