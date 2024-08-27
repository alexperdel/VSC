import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona con el nombre de: ", self.nombre)
        
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    
    
class listaPersonas:
    personas=[]
    
    def __init__(self):
        listaPersonasFicheroExterno=open("/Users/alexperdel/Visual Studio Code/Python/FicheroListaPersonas", "ab+")
        listaPersonasFicheroExterno.seek(0)
        
        try:
            self.personas=pickle.load(listaPersonasFicheroExterno)
            print("Se cargaron {} personas del ficher externo".format(len(self.personas)))
            
        except:
            print("Fichero vacio")
            
        finally:
            listaPersonasFicheroExterno.close
            del(listaPersonasFicheroExterno)
    
    
    def agregarPersonas(self,p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()
        
        
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
            
    def guardarPersonasEnFicheroExterno(self):
        listaPersonasFicheroExterno=open("/Users/alexperdel/Visual Studio Code/Python/FicheroListaPersonas", "wb")
        pickle.dump(self.personas, listaPersonasFicheroExterno)
        listaPersonasFicheroExterno.close
        del(listaPersonasFicheroExterno)
        
    def mostrarFicheroExterno(self):
        print("La información del fichero externo es:")
        for p in self.personas:
            print(p)
                
miLista=listaPersonas()   

p=Persona("Luisa","Femenino","66")
miLista.agregarPersonas(p)

miLista.mostrarFicheroExterno()
