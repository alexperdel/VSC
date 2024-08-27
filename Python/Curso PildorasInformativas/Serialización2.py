import pickle

#Serializar a binario un objeto completo

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
        
        
coche1=Vehiculo("Citroen", "C4")
coche2=Vehiculo("Opel", "Grandland")
coche3=Vehiculo("Seat", "Cordoba")

cocheColeccion=[coche1,coche2,coche3]

ficheroCochesBinarios=open("ListadoCoches","wb")

pickle.dump(cocheColeccion,ficheroCochesBinarios)

ficheroCochesBinarios.close()
del(ficheroCochesBinarios)

#Recuperar la información desde el fichero serializado

ficheroSerializadoCoches=open("/Users/alexperdel/Visual Studio Code/Python/ListadoCoches", "rb")

misCochesSerializados=pickle.load(ficheroSerializadoCoches)

ficheroSerializadoCoches.close()

for i in misCochesSerializados:
    print(i.estado())
