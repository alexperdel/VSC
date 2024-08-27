from tkinter import *
from tkinter import messagebox

root=Tk()

def alert():
    messagebox.showinfo("ALERT",  "Mensaje de alerta al pulsar un botón/menú")
    messagebox.showerror("Mensaje de error")
    messagebox.showwarning("Mensaje Warning")
    messagebox.askquestion("Yes o no")
    messagebox.askokcancel("True o False")
    messagebox.askretrycancel("Cancel o Retry")

barraMenu=Menu (root)
root. config(menu=barraMenu, width=300, height=300)

#Menú para que al pulsar Acerca de... aparezca el Alert
archivoAyuda=Menu (barraMenu)
archivoAyuda.add_command(label="Acerca de...", command=alert)
barraMenu.add_cascade (label="Ayuda", menu=archivoAyuda)


root.mainloop()


