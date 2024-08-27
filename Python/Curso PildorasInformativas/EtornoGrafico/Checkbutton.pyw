from tkinter import *

root = Tk()
root.title("Checkbutton Ejemplo")


playa=IntVar()
montagna=IntVar()
ciudad=IntVar()

def opcionesViaje():
    opcionEscogida=""
    if(playa.get()==1):
        opcionEscogida+=" playa"

    if(montagna.get()==1):
        opcionEscogida+=" montaña"
        
    if(ciudad.get()==1):
        opcionEscogida+=" ciudad"
        
    textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file="/Users/alexperdel/Visual Studio Code/Python/Curso PildorasInformativas/EtornoGrafico/python.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige tu destino:", width=100).pack()


Checkbutton(root, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Montaña",  variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Ciudad",  variable=ciudad, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()