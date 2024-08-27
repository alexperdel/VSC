#Comparador de sueldos en la misma linea del IF
salario_presidente=int(input("Introduce salario presidente "))
print("Salario presidente: " + str(salario_presidente))

salario_director=int(input("Introduce salario director "))
print("Salario director: " + str(salario_director))

salario_jefe=int(input("Introduce salario jefe "))
print("Salario jefe: " + str(salario_jefe))

salario_administrativo=int(input("Introduce administrativo jefe "))
print("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe<salario_director<salario_presidente:
    print("Todo OK")
else:
    print("Algo va mal")
    

#Comparador AND/OR para obtener una beca, según distancia, con hermanos en el centro y salario familiar
print("Programa de becas")
distancia = int(input("Introduce distancia: "))
hermanos = int(input("Intrduce el número de hermanos "))
salario = int(input("Introduce salario: "))

if distancia>40 and hermanos>=2 or salario >=2000:
    print("Tienes derecho a becha")
else:
    print("No tienes derecho a beca")

#Comparador IN elegir asigantura de un listado, si no dará error
print("Asisgnaturas optativas")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input ("Escribe la asignatura escogida: ")

asignatura=opcion.lower()

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Has alegido: " + asignatura)
else:
    print("Error")