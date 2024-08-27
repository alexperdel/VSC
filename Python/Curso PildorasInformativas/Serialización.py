import pickle


#Crear una lista y pasarla a un fichero codificado como binario 
listaNombres = ["Alex", "Ro", "Raúl", "Óliver"]

ficheroBinario=open("listaNombres", "wb") #wb = escritura binaria

pickle.dump(listaNombres,ficheroBinario)

ficheroBinario.close()

del(ficheroBinario)

#Abrir e importar la información de un fichero binario

import pickle

fichero=open("/Users/alexperdel/Visual Studio Code/Python/listaNombres","rb") #rb = lectura binaria

lista=pickle.load(fichero)

print(lista)
