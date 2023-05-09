
# 1. Cree un programa que encuentre el promedio de los tres puntajes dados y devuelva el valor de la letra 
# asociada con esa calificación. con al siguiente tabla
#     0   - 2     D
#     2.1 - 5     C
#     5.1 - 6     B
#     6.1 - 7     A


# La función float se usa para intentar convertir el valor ingresado por el usuario a un número decimal. Si la conversión es exitosa, se imprime el número en la consola y la bandera es_numero se cambia a True para salir del bucle. Si la conversión falla, se lanza una excepción ValueError y se imprime un mensaje de error en la consola. El bucle se vuelve a ejecutar hasta que el usuario ingrese un número decimal válido.

es_numero_1 = False
es_numero_2 = False
es_numero_3 = False

# Repetir hasta que el usuario ingrese un número
while es_numero_1==False:
    valor_1 = input("Ingresa el primer número: ")
    try:
        # Intentar convertir el valor a float
        numero_1 = float(valor_1)

        # Verificar que el número esté entre 0 y 7
        if 0 <= numero_1 <= 7:
            # Cambiar la bandera para salir del bucle
            es_numero_1 = True
        else:
            # Imprimir un mensaje de error
            print("El número debe estar entre 0 y 7.")
        
    except ValueError:
        # Si la conversión falla, imprimir un mensaje de error
        print("El valor ingresado no es un número.")

# Repetir hasta que el usuario ingrese un número
while es_numero_2 == False:
    valor_2 = input("Ingresa el segundo número: ")
    try:
        # Intentar convertir el valor a float
        numero_2 = float(valor_2)

        # Verificar que el número esté entre 0 y 7
        if 0 <= numero_2 <= 7:
            # Cambiar la bandera para salir del bucle
            es_numero_2 = True
        else:
            # Imprimir un mensaje de error
            print("El número debe estar entre 0 y 7.")
        
    except ValueError:
        # Si la conversión falla, imprimir un mensaje de error
        print("El valor ingresado no es un número.")
        

# Repetir hasta que el usuario ingrese un número
while es_numero_3== False:
    valor_3 = input("Ingresa el tercer número: ")
    try:
        # Intentar convertir el valor a float
        numero_3 = float(valor_3)

        # Verificar que el número esté entre 0 y 7
        if 0 <= numero_3 <= 7:
            # Cambiar la bandera para salir del bucle
            es_numero_3 = True
        else:
            # Imprimir un mensaje de error
            print("El número debe estar entre 0 y 7.")
        
        
    except ValueError:
        # Si la conversión falla, imprimir un mensaje de error
        print("El valor ingresado no es un número.")
        

average= (numero_1 + numero_2 + numero_3)/3

print('El promedio es:', average)

if average >= 0 and average <=2:
    print("Este promedio equivale a una D")
elif average >= 2.1 and average <=5:
    print("Este promedio equivale a una C")
elif average >= 5.1 and average <=6:
    print("Este promedio equivale a una B")
elif average >= 6.1 and average <=7:
    print("Este promedio equivale a una A")
else:
    print('El valor se encuentra fuera del rango de la tabla') #En teoría el usuario no debiese poder llegar a acá, pero por es para poder controlar un error no previsto
