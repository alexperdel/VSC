#Propiedades de la clase
class Coche():
    
    #Crear el construtor para guardar las propiedades iniciales
    #Se usa DEF __INIT__(SELF): 
        #SELF.laPropiedad
    #Para encapsular una propiedad, y que no pueda ser modificada SELF.__PROPIEDAD
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4 
        self.__enMarcha=False

#Comportamientos a través de los métodos (SELF es obligatorio)
    def arrancar(self,arrancamos):
       self.__enMarcha=arrancamos
       if (self.__enMarcha):
           chequeo=self.__chequeoInterno()
       
       if(self.__enMarcha and chequeo):
            return "El coche está en marcha"
       elif(self.__enMarcha and chequeo==False):
           return ("No se puede arrancar, chequeo erroneo")
       else:
            return "El coche está parado"
    
    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Y mide ", self.__anchoChasis, "de ancho")

    #Encapsular el método con __NombreMetodo para protegerlo que no sea accesible desde fuera
    def __chequeoInterno(self):
        print("Realizando chequeo interno...")
        self.gasolina="BAJO"
        self.aceite="OK"
        self.puertas="Cerradas"
        
        if (self.gasolina=="OK" and self.aceite=="OK" and self.puertas=="Cerradas"):
            return True
        else:
            return False
        
        
        
#Instanciar una clase = crear un Objeto
miCoche=Coche()
print(miCoche.arrancar(True))
print(miCoche.estado())

#Crear segundo Objeto con la misma clase
miCoche2=Coche()
print(miCoche.arrancar(False))
print(miCoche.estado())