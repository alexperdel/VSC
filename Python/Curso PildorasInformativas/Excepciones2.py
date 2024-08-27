def divide():
    #Capturamos las excepciones con múltiples EXCEPT 
    try:
        n1 = (float(input("Numero 1: ")))
        n2 = (float(input("Numero 2: ")))
        print("La división es: " + str(n1/n2))
    
    except ValueError:
        print("Introduce un numero")
    except ZeroDivisionError:
        print("No se puede dividir por cero")

    #FINALLY para que siempre se ejecute un código, usado en cierre de conexiones con BBDD
    finally:     
        print("Calculo terminado")

divide()