class Vehiculo():
    
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self._enMarcha=True
        
    def arrancar(self,arrancamos):
        self._enMarcha=arrancamos
        if(self._enMarcha):
            chequeo=self.__chequeoInterno()
        
        if(self._enMarcha and chequeo):
            return("Vehiculo  en marcha")
        elif(self._enMarcha and chequeo==False):
            return("Fallo de chequeo")
        else:
            return("Vehiculo parado")
        
    def estado(self):
        print("Marca es ", self.marca, "Y modelo ", self.modelo)
            
    def __chequeoInterno(self):
        print("Chequeando Vehiculo")
        self.aceite="OK"
        self.gasolina="OK"
        
        if(self.aceite=="OK" and self.gasolina=="OK"):
            return True
        else:
            return False
        
class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

miCoche=Coche("Citroen", "C4")
print(miCoche.arrancar(True))
miCoche.estado()

class Moto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        
miMoto=Moto("Honda", "BCR")
miMoto.estado()