class Vehiculo():
    def __init__(self,marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self._enMarcha=False
        
    def arrancar(self, arrancamos):
        self._enMarcha=arrancamos
        
        if (self._enMarcha):
            chequeo=self.__chequeoInicial()
        
        if(self._enMarcha and chequeo):
            return ("Vehiculo en marcha")
        elif(self._enMarcha and chequeo==False):
            return ("Chequeo con error")
        else:
            return("Vehiculo parado")
        
        
    def __chequeoInicial(self):
        print("Haciendo chequeo....")
        self.gasolina="OK"
        self.aceite="OK"
        
        if(self.aceite=="OK" and self.gasolina=="OK"):
            return True
        else:
            return False

        
class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def desplazamiento(self):
        return("Me desplazo con 4 ruedas")

class Moto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def desplazamiento(self):
        return("Me desplazo con 2 ruedas")
        
class Camion(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        
    def desplazamiento(self):
        return("Me desplazo con 6 ruedas")
    

miCoche=Coche("Citroen", "C4")
print(miCoche.arrancar(True))
print(miCoche.desplazamiento())

miMoto=Moto("Honda", "BCR")
print(miMoto.arrancar(False))
print(miMoto.desplazamiento())
