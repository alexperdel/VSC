from tkinter import *

# Crear la raíz de la ventana
root = Tk()

# Configuración de la ventana principal
root.title("Formulario de Ejemplo")

# Configurar el Frame dentro de root
miFrame = Frame(root, width=500, height=400)
miFrame.pack(padx=10, pady=10)

# Crear variable para almacenar el nombre
miNombre = StringVar()

# Cuadro de texto para el nombre
cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")  # Configuración del cuadro de texto del nombre

# Cuadro de texto para la contraseña
cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")  # Configuración para ocultar la contraseña con '*'

# Cuadro de texto para el apellido
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

# Cuadro de texto para la dirección
cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

# Cuadro de texto para los comentarios
textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)

# Scrollbar vertical para los comentarios
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")

# Asociar el scrollbar vertical al cuadro de comentarios
textoComentario.config(yscrollcommand=scrollVert.set)

# Etiquetas para los cuadros de texto
nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Password:")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Dirección:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

# Crear la función que será ejecutada por el botón
def codigoBoton():
    miNombre.set("Alex")  # Cambia el valor del cuadro de texto del nombre

# Crear el botón del formulario (fuera del Frame)
botonEnvio = Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack(pady=10)  # Usamos pack() para colocar el botón debajo del Frame

# Ejecutar el bucle principal de la ventana
root.mainloop()
