#El polimorfismo se usa para que el mismo objeto tenga diferentes formas
#Aquí cada objeto usa el mismo método dentro de su clase, aunque cada uno es diferente

class Coche():
    def desplazamiento (self):
        print("Me desplazo utilizando 4 ruedas")
        
class Moto():
    def desplazamiento (self):
        print("Me desplazo utilizando 2 ruedas")
        
class Camion():
    def desplazamiento (self):
        print("Me desplazo utilizando 6 ruedas")
        
#Para ver como se desplaza cada uno, lo normal sería crear objetos por separados

miCoche=Coche()
miCoche.desplazamiento()

miMoto=Moto()
miMoto.desplazamiento()

miCamion=Camion()
miCamion.desplazamiento()

#Para simplificar esto, creamos una funcion que recibe por parámetro un vehiculo

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
    
miVehiculo=Camion() #Este objeto se puede cambiar por Coche/Moto que siempre llama al desplazamiento correspondiente
desplazamientoVehiculo(miVehiculo)
