

import random

# Ejercicio 1


frase = input('Por favor escriba una frase: ')
letra_ususario = input('Por davor escriba una letra: ')
contador= 0 

for letra in frase:
    if letra == letra_ususario:
            contador +=1
print(f'la cantidad de letras "{letra_ususario}" es {contador}')

# Ejercicio 2

capital = float(input('Ingrese el capital inicial: '))
interes = float(input('Ingrese la tasa de interés: ')) #(oscila entre 0 y 100)
años = int(input('Ingrese la cantidad de años a calcular : '))

# se desea saber el capital final 

capital_final = capital * (1+ (años * interes)/100)
print(capital_final)


for elemento in range(años):
    capital = capital + (capital*interes)
print(capital)


