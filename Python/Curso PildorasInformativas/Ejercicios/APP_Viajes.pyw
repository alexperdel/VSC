from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("App de viajes personal")

#Funciones 

def mostrarResumen():
    #Recoger datos de los formularios
    nombre=miNombre.get()
    apellido=miApellido.get()
    direccion=miDireccion.get()
    edad=miEdad.get()
    
    #Sexo
    if miSexo.get()==1:
        sexo="Masculino"
    elif miSexo.get()==2:
        sexo="Femenino"
    else:
        sexo="No especificado"
        
    #Destinos
    destinosSeleccionados = []
    if varEdimburgo.get():
        destinosSeleccionados.append("Edimburgo")
    if varFlorencia.get():
        destinosSeleccionados.append("Florencia")
    if varMalta.get():
        destinosSeleccionados.append("Malta")
    
    #Mensaje resumen
    resumen = (
        f"Nombre: {nombre}\n"
        f"Apellidos: {apellido}\n"
        f"Direccion: {direccion}\n"
        f"Sexo: {sexo}\n"
        f"Edad: {edad}\n"
        f"Destino/s: {', '.join(destinosSeleccionados)}"
    )
    
    # Mostrar el mensaje
    messagebox.showinfo("Resumen de tu pedido", resumen)

#Frames izquierdo y derecho
miFrameLeft = Frame(root, width=250, height=450, bg="#ccc")
miFrameLeft.pack(side="left", padx=5, pady=5)

miFrameRight = Frame(root, width=250, height=450, bg="#ccc")
miFrameRight.pack(side="left", padx=5, pady=5)

#Etiquetas en grid frame izquierdo
datosLabel= Label(miFrameLeft, text="Datos personales:")
datosLabel.grid(row=1, column=1, sticky="e", padx=5, pady=5)
datosLabel.config(bg="#ccc")

nombreLabel= Label(miFrameLeft, text="Nombre:")
nombreLabel.grid(row=2, column=1, sticky="e", padx=5, pady=5)
nombreLabel.config(bg="#ccc")

apellidosLabel= Label(miFrameLeft, text="Apeliidos:")
apellidosLabel.grid(row=3, column=1, sticky="e", padx=5, pady=5)
apellidosLabel.config(bg="#ccc")

direccionLabel= Label(miFrameLeft, text="Dirección:")
direccionLabel.grid(row=4, column=1, sticky="e", padx=5, pady=5)
direccionLabel.config(bg="#ccc")

sexoLabel= Label(miFrameLeft, text="Sexo:")
sexoLabel.grid(row=5, column=1, sticky="e", padx=5, pady=5)
sexoLabel.config(bg="#ccc")

edadLabel= Label(miFrameLeft, text="Edad:")
edadLabel.grid(row=6, column=1, sticky="e", padx=5, pady=5)
edadLabel.config(bg="#ccc")


#Campos en grid frame izquierdo

miNombre=StringVar()
cuadroNombre=Entry(miFrameLeft, textvariable=miNombre)
cuadroNombre.grid(row=2, column=2, padx=5, pady=5)
cuadroNombre.config(justify="center")

miApellido=StringVar()
cuadroApellido=Entry(miFrameLeft, textvariable=miApellido)
cuadroApellido.grid(row=3, column=2, padx=5, pady=5)
cuadroApellido.config(justify="center")

miDireccion=StringVar()
direccionApellido=Entry(miFrameLeft, textvariable=miDireccion)
direccionApellido.grid(row=4, column=2, padx=5, pady=5)
direccionApellido.config(justify="center")

miSexo=IntVar()
Radiobutton(miFrameLeft, text="Masculino", variable=miSexo, value=1,  bg="#ccc").grid(row=5, column=2,padx=5, pady=5)
Radiobutton(miFrameLeft, text="Femenino", variable=miSexo, value=2, bg="#ccc").grid(row=5, column=3, padx=5, pady=5)

miEdad=IntVar()
edadLabel=Spinbox(miFrameLeft, from_=0, to=100,  textvariable=miEdad)
edadLabel.grid(row=6, column=2,padx=5, pady=5)
edadLabel.config(justify="center")


#Campos en grid frame derecho
destinosLabel=Label(miFrameRight, text="Destinos disponibles:")
destinosLabel.grid(row=1, column=1, sticky="w", padx=5, pady=5)
destinosLabel.config(bg="#ccc")

varEdimburgo=IntVar()
Checkbutton(miFrameRight, text="Edimburgo", variable=varEdimburgo, onvalue=1, offvalue=0, bg="#ccc").grid(row=2,column=1, sticky="w")

varFlorencia=IntVar()
Checkbutton(miFrameRight, text="Florencia", variable=varFlorencia, onvalue=1, offvalue=0, bg="#ccc").grid(row=3,column=1, sticky="w")

varMalta = IntVar()
Checkbutton(miFrameRight, text="Malta", variable=varMalta, onvalue=1, offvalue=0, bg="#ccc").grid(row=4,column=1, sticky="w")

resumenLabel=Label(miFrameRight, text="Resumen de tu pedido:")
resumenLabel.grid(row=5,column=1, padx=5, pady=5)
resumenLabel.config(bg="#ccc")

infoButton = Button(miFrameRight, text="Comprobar", command=mostrarResumen).grid(row=7, column=1, padx=5, pady=5)


root.mainloop()