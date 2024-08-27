from tkinter import *

#Crear raiz
root = Tk()
root.title("Calculadora Python")

#Crear frame
miFrame=Frame(root, width=600, height=600)
miFrame.config(padx=10,pady=10)
miFrame.pack()

#-----Operación------
operacion=""

#-----Resultado------
resultado=0

#Crar variable para mostar numero
numeroPantalla=StringVar()
numeroPantalla.set("0")

#Entrada visual de los numeros y resultados
entrada = Entry(miFrame, width=16, font=('Arial', 16), borderwidth=2, relief="solid", textvariable=numeroPantalla)
entrada.grid(row=0, column=0, columnspan=5)
entrada.config(background="black", fg="#03f943", justify="right")

#Pulsasiones teclado

def numeroPulsado(num):
    global operacion
    if operacion !="":
        numeroPantalla.set(num)
        operacion=""
    else:    
        numeroPantalla.set(numeroPantalla.get()+num)
    
def borrarPulsado():
    numeroPantalla.set("0")
    
#-----funcion suma---------

def suma(num):
    global operacion
    
    global resultado
    
    resultado+=float(num)
    
    operacion= "suma"
    
    numeroPantalla.set(resultado)
    
    
#-----funcion resta------
num1=0

contador_resta=0

def resta(num):

	global operacion
	global resultado
	global num1
	global contador_resta


	if contador_resta==0:

		num1=float(num)

		resultado=num1

	else:

		if contador_resta==1:

			resultado=num1-int(num)

		else:

			resultado=int(resultado)-int(num)	

		numeroPantalla.set(resultado)

		resultado=numeroPantalla.get()


	contador_resta=contador_resta+1

	operacion="resta"
    
#------funcion multiplicar------

contador_multi=0

def multiplica(num):

	global operacion

	global resultado

	global num1

	global contador_multi

	global reset_pantalla
	
	if contador_multi==0:

		num1=int(num)
		
		resultado=num1

	else:

		if contador_multi==1:

			resultado=num1*int(num)

		else:

			resultado=int(resultado)*int(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_multi=contador_multi+1

	operacion="multiplicacion"




#------funcion elResultado = para la suma--------
def elResultado():
    global resultado
    
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    
    resultado=0


#-----Fila 1------

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)

#-----Fila 2------

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="X", width=3, command=lambda:numeroPantalla.get())
botonMult.grid(row=3, column=4)

#-----Fila 3------

boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=3)
botonRestar=Button(miFrame, text="-", width=3, command=lambda: resta(numeroPantalla.get()))
botonRestar.grid(row=4, column=4)

#-----Fila 4------

boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda: elResultado())
botonIgual.grid(row=5, column=3)
botonSuma=Button(miFrame, text="+", width=3, command=lambda: suma(numeroPantalla.get()))
botonSuma.grid(row=5, column=4)

#-----Fila 5------

botonBorrar=Button(miFrame, text="C", width=3, command=borrarPulsado)
botonBorrar.grid(row=6, column=2)










# Iniciar el bucle principal
root.mainloop()