from tkinter import *

root=Tk()
barraMenu=Menu (root)
root. config(menu=barraMenu, width=300, height=300)

#Elementos del menú
archivoMenu=Menu(barraMenu)
archivoEdicion=Menu(barraMenu)
archivoHerramientas=Menu(barraMenu)
archivoAyuda=Menu (barraMenu)

#Subelementos del menú Archivo
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

#Texto para los elementos del menú
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade (label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade (label="Ayuda", menu=archivoAyuda)

root.mainloop()