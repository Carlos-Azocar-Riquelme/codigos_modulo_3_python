# repetir = range(10)

# entrada = input("Introduce una palabra")

# for elemento in repetir:
#     print(entrada) 


# edad = int(input("Introduce tu edad: "))

# for elemento in range(edad):
#     print(elemento +1) 



# altura_triangulo = int(input("Ingrese la altura del triangulo:"))
# triangulo = ""

# for elemento in range(altura_triangulo):
#     triangulo= '*' + triangulo
#     print(triangulo) 



contraseña_correcta= 'casa'

while True:
    contraseña_usuario= input('Ingrese si contraseña: ')
    if contraseña_usuario != contraseña_correcta:
        print("Contraseña erronea, ingrese nuevamente")
    else:
        print("Contraseña correcta")
        break
