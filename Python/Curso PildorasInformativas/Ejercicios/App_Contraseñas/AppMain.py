from tkinter import *
from tkinter import messagebox
from AppCheck import verificar_contrasena

root = Tk()
root.title("Verifica tu contraseña robada")
root.config(bg="#aaa")


#Función para comprobar la contraseña en el botón
def comprobar_contrasena():
    contrasena = miContrasena.get()
    print(f"contraeña ingresada {contrasena}")
    resultado = verificar_contrasena(contrasena)
    print(f"resultado {resultado}")
    if resultado is None:
        messagebox.showerror("Error", "no se ha podido cargar el archivo")
    elif resultado:
        messagebox.showwarning("Alerta", "tu contraseña ha sido vulnerada")
    else:
        messagebox.showinfo("Felicidades", "tu contraseña no ha sido vulnerada")
        

# Configuración del Frame
miFrame = Frame(root, width=350, height=145, bg="#aaa")
miFrame.pack(side="top", padx=10, pady=10)

# Etiqueta de texto
textoLabel = Label(miFrame, text="Más de 100.000 contraseñas han sido expuestas, introduce la tuya para ver si ha sido vulnerada:")
textoLabel.config(justify="center", wraplength=300, fg="#00ff00", bg="#aaa")  # Ajustar el texto dentro de los límites del Frame
textoLabel.pack(padx=5, pady=5)

# Campo de entrada de contraseña
miContrasena = StringVar()
cuadroContrasena = Entry(miFrame, textvariable=miContrasena, show="*")  # `show="*"` para ocultar la contraseña
cuadroContrasena.config(justify="center")
cuadroContrasena.pack(padx=10, pady=10)

# Botón para comprobar la contraseña
probarButton = Button(miFrame, text="Comprobar", command=comprobar_contrasena)
probarButton.pack(padx=15, pady=15)






root.mainloop()
