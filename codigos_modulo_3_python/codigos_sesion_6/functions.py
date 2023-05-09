def saludar(nombre):
    print(f'Hola {nombre}!!!!')
    

saludar('Carlos')

def saludar_dos (first_name, last_name):
    print(f'Hola {first_name}, {last_name}!!!!')


# puedo indicarle a qué parametro apunta cada argumento
saludar_dos(last_name= 'Azocar',first_name= 'Carlos')


def multiplicar_texto(texto, multiplier = 1):
    print(texto*multiplier)

multiplicar_texto('x',5)


def varieltal(param1, param2, *others):
    print(param1)
    print(param2)
    print(others)


varieltal("1A", "2B", 0, "XX", [0,1])


# con ** pasa a generar un diccionario

def varietal_2(param1, **others):
    print(param1)
    print(others)

varietal_2("1A", id= 10, name ='Carlos')