
# 4. Dado un mes como un número entero del 1 al 12, devuelva a qué trimestre del año pertenece como un número entero.
#     Por ejemplo: el mes 2 (febrero), forma parte del primer trimestre; el mes 6 (junio), 
#     forma parte del segundo trimestre; y el mes 11 (noviembre), forma parte del cuarto trimestre.



es_numero_1 = False


# Repetir hasta que el usuario ingrese un número
while es_numero_1==False:
    valor_1 = input("Ingresa el número del mes entre 1 y 12: ")
    try:
        # Intentar convertir el valor a float
        numero_1 = int(valor_1)

        # Verificar que el número esté entre 1 y 12
        if 1 <= numero_1 <= 12:
            # Cambiar la bandera para salir del bucle
            es_numero_1 = True
            
            if 1 <= numero_1 <= 3: # es_numero_1 >= 1 or es_numero_2 <= 3
                print('Primer trimestre')

            elif 4 <= numero_1 <= 6:
                print('Segundo trimestre')
            
            elif 7 <= numero_1 <= 9:
                print('Tercer trimestre')

            else:
                print('Cuarto Trimestre')

        else:
            # Imprimir un mensaje de error
            print("El número debe estar entre 1 y 12, ambos inclusive.")
        
    except ValueError:
        # Si la conversión falla, imprimir un mensaje de error
        print("El valor ingresado no es un número.")
