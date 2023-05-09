# 3. Escriba un programa que calcule el máximo común divisor entre dos números enteros.


es_numero_1 = False
es_numero_2 = False

# Repetir hasta que el usuario ingrese un número
while es_numero_1==False:
    valor_1 = input("Ingresa el primer número: ")
    try:
        # Intentar convertir el valor a float
        numero_1 = int(valor_1)
        es_numero_1 = True
        
    except ValueError:
        # Si la conversión falla, imprimir un mensaje de error
        print("El valor ingresado tiene que ser un número entero.")
        
# Repetir hasta que el usuario ingrese un número
while es_numero_2==False:
    valor_2 = input("Ingresa el segundo número: ")
    try:
        # Intentar convertir el valor a float
        numero_2 = int(valor_2)
        es_numero_2 = True
        
    except ValueError:
        # Si la conversión falla, imprimir un mensaje de error
        print("El valor ingresado no es un número.")



# Algoritmo de Euclides

def mcd(a, b):
    a = abs(a)
    b = abs(b) #Sí, se puede calcular el máximo común divisor (MCD) para números negativos. En realidad, el MCD de dos números negativos es igual al MCD de sus valores absolutos. Por lo tanto, para calcular el MCD de dos números negativos, primero se deben convertir a sus valores absolutos y luego se aplica el algoritmo para calcular el MCD.
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

print("El MCD de", numero_1, "y", numero_2, "es", mcd(numero_1, numero_2))


# No, el orden en el que se ingresan los valores no importa en el cálculo del máximo común divisor (MCD). El MCD es una propiedad de dos números y es el mismo independientemente del orden en que se ingresen los valores. Por ejemplo, el MCD entre 10 y 20 es igual al MCD entre 20 y 10, que es 10. Esto se aplica a cualquier par de números y a cualquier método utilizado para calcular el MCD.