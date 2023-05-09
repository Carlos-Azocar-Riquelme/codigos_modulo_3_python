
# 7. Cree una función notaFinal, que calcule la nota final de un estudiante en función de dos parámetros: una nota para el examen y una cantidad de proyectos completados.
#     Esta función debe tomar dos argumentos: examen - calificación del examen (de 0 a 100); proyectos - número de proyectos completados (de 0 en adelante);
#     Esta función debería devolver un número (calificación final). Hay cuatro tipos de calificaciones finales:

#     100, si la calificación del examen es superior a 90 o si el número de proyectos terminados es superior a 10.
#     90, si la calificación del examen es superior a 75 y si el número de proyectos completados es mínimo 5.
#     75, si la calificación del examen es superior a 50 y si el número de proyectos completados es mínimo 2.



def NotaFinal (calificacion_examen, numero_proyectos_completados):
    
    if calificacion_examen > 90 or numero_proyectos_completados > 10:
        notaFinal = "El alumno aprueba con una calificación final de 100"
        return notaFinal
    elif calificacion_examen > 75 and numero_proyectos_completados >= 5:
        notaFinal = "El alumno aprueba con una calificación final de 90"
        return notaFinal
    elif calificacion_examen > 50 and numero_proyectos_completados >= 2:
        notaFinal = "El alumno aprueba con una calificación final de 75"
        return notaFinal
    else:
        notaFinal = "El estudiante está reprobado"
        return notaFinal   



validacion_calificacion_usuario = False
validacion_proyectos_usuario = False

# Repetir hasta que el usuario ingrese un número
while validacion_calificacion_usuario==False:
    valor_calificacion_usuario = input("Ingrese la calificación del examen: ")
    try:
        # Intentar convertir el valor a float
        calificacion_usuario_float = float(valor_calificacion_usuario)

        # Verificar que el número esté entre 0 y 100
        if 0 <= calificacion_usuario_float <= 100:
            # Cambiar la bandera para salir del bucle
            validacion_calificacion_usuario = True

        else:
            # Imprimir un mensaje de error
            print("El número debe estar entre 1 y 100.")
        
    except ValueError:
        # Si la conversión falla, imprimir un mensaje de error
        print("El valor tiene que encontrarse entre 1 y 100, ambos inclusive.")

# Repetir hasta que el usuario ingrese un número
while validacion_proyectos_usuario == False:
    valor_proyectos_usuario = input("Ingrese la cantidad de proyectos completados: ")
    try:
        # Intentar convertir el valor a float
        proyectos_usuario_float = float(valor_proyectos_usuario)

        # Verificar que el número esté entre 0 y 7
        if 0 <= proyectos_usuario_float:
            # Cambiar la bandera para salir del bucle
            validacion_proyectos_usuario = True
        else:
            # Imprimir un mensaje de error
            print("El número de proyectos debe ser mayor a 0.")
        
    except ValueError:
        # Si la conversión falla, imprimir un mensaje de error
        print("El valor ingresado tiene que ser un número entero mayor a 0.")
    

print(NotaFinal(calificacion_usuario_float, proyectos_usuario_float))