from tkinter import *

# Crear la raíz de la ventana
raiz = Tk()

# Establecer el título de la ventana
raiz.title("Ventana Python")
raiz.config(bg="grey")

#Configurar el Frame dentro de tk
miFrame=Frame()
miFrame.pack(side="bottom")
miFrame.config(bg="pink")
miFrame.configure(width="450", height="200")


# Ejecutar el bucle principal de la ventana
raiz.mainloop()
