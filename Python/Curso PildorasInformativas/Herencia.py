class Vehiculo():
    
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        self.enMarcha=True
        
    def acelerar(self):
        self.acelerea=True
    
    def frenar (self):
        self.frena=True
        
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha, "\nAcelarando:", self.acelera, "\nFrenando: " , self.frena)
        
    
class Moto(Vehiculo):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    
    #Sobreescribir el método ESTADO de la clase padre para añadir un estado nuevo "CABALLITO"
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha, "\nAcelarando:", self.acelera, "\nFrenando: " , self.frena, "\n", self.hcaballito)
        
        
class Furgoneta(Vehiculo):
    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return("Furgoneta cargada")
        else:
            return("Furgoneta vacia")
        
 
#Esta clase no herada de ningún otro       
class vElectricos(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        
        self.autonomia=100
        
    def cargarEnergia(self):
        self.cargando=True
    
        
miMoto=Moto("Honda", "CBR")

miMoto.arrancar()
miMoto.caballito()
miMoto.estado()

print("---------XXX---------")

#Creamos una instancia herando de MOTO, por lo que hereda las propiedades de MOTO, incluida el caballito
miQuad=Moto("Honda", "SHR")

miQuad.arrancar()
miQuad.caballito()
miQuad.estado()

print("---------XXX---------")

miFurgoneta=Furgoneta("Citroën","Jumper")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))


#Creamos una instancia con HERENCIAMULTIPLE. Ojo porque toma el construtor de la primera clase que se pone.
#En este caso, la primera es vElectricos por lo que no soporta Marca y Modelo del constructor de Vehiculo 
class BicicletaElectrica(vElectricos,Vehiculo):
    pass
   
miBici=BicicletaElectrica("Orbea", "2000P")
miBici.estado()
