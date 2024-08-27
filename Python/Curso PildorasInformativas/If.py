# Solicitar una nota al usuario y convertirla a entero
notaAlumno = int(input("Introduce la nota: "))

# Definir la función de evaluación
def evaluacion(nota):
    valoracion = "aprobado"  # Valor por defecto es aprobado
    if nota < 5:  # Condición: si la nota es menor que 5
        valoracion = "suspenso"  # Cambiar la valoración a suspenso
    return valoracion  # Devolver la valoración final

# Imprimir el resultado de la evaluación
print("Resultados de evaluación:", evaluacion(notaAlumno))


# Solicitar una nota al usuario y convertirla a entero
notaAlumno = int(input("Introduce la nota: "))

# Definir la función de evaluación con más categorías
def evaluacion(nota):
    if nota < 5:
        valoracion = "suspenso"
    elif nota < 7:
        valoracion = "aprobado"
    elif nota < 9:
        valoracion = "notable"
    else:
        valoracion = "sobresaliente"
    return valoracion

# Imprimir el resultado de la evaluación
print("Resultados de evaluación:", evaluacion(notaAlumno))

# Solicitar una nota al usuario y convertirla a entero
notaAlumno = int(input("Introduce la nota: "))

# Definir la función de evaluación con operadores lógicos
def evaluacion(nota):
    if nota < 5:
        valoracion = "suspenso"
    elif nota >= 5 and nota < 7:
        valoracion = "aprobado"
    elif nota >= 7 and nota < 9:
        valoracion = "notable"
    else:
        valoracion = "sobresaliente"
    return valoracion

# Imprimir el resultado de la evaluación
print("Resultados de evaluación:", evaluacion(notaAlumno))

# Solicitar una nota al usuario y convertirla a entero
notaAlumno = int(input("Introduce la nota: "))

# Definir la función de evaluación con condicionales anidadas
def evaluacion(nota):
    if nota < 5:
        valoracion = "suspenso"
    else:
        if nota < 7:
            valoracion = "aprobado"
        elif nota < 9:
            valoracion = "notable"
        else:
            valoracion = "sobresaliente"
    return valoracion

# Imprimir el resultado de la evaluación
print("Resultados de evaluación:", evaluacion(notaAlumno))

# Solicitar la edad del usuario
edad = int(input("Introduce tu edad: "))

# Evaluar el rango de edad
if edad < 0:
    print("Edad no válida")
elif edad < 13:
    print("Eres un niño")
elif edad < 20:
    print("Eres un adolescente")
elif edad < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")


# Solicitar una nota al usuario y convertirla a entero
notaAlumno = int(input("Introduce la nota: "))

# Definir la función de evaluación con comentarios adicionales
def evaluacion(nota):
    if nota < 5:
        valoracion = "suspenso"
        comentario = "Necesitas mejorar"
    elif nota < 7:
        valoracion = "aprobado"
        comentario = "Buen trabajo, pero puedes hacerlo mejor"
    elif nota < 9:
        valoracion = "notable"
        comentario = "Muy bien, sigue así"
    else:
        valoracion = "sobresaliente"
        comentario = "Excelente, felicidades"
    return valoracion, comentario

# Obtener el resultado de la evaluación
resultado, comentario = evaluacion(notaAlumno)

# Imprimir el resultado de la evaluación con el comentario
print("Resultados de evaluación:", resultado)
print("Comentario:", comentario)

