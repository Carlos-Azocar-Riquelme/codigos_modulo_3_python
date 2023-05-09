# Diccionario: Tienen palabras y un significado asociado

print("===========TRABAJANDO CON DICCIONARIOS=================")

empty_dict = {}


# ESTE ES EL MÁS ÓPTIMO
fullfild_dict = {
    "id": 1,
    "name": "Valeria"
}

print(empty_dict)
print(fullfild_dict)

lista_1= ['a1', 'b2']
dict_converted= dict(lista_1)
print(dict_converted)

tupla_1 = ('a1','b2')
print(tupla_1, dict(tupla_1))


print("diccionario dimensional")
list_dimensional=[['a',1], ['b',3]]
print(list_dimensional, dict(list_dimensional))



# 1. OBTENER UN ELEMENTO DE IN DICCIONARIO
diccionario = {'nombre': 'Carlos', 'edad': 30, 'profesión': 'programador'}

# Obtener el valor asociado a la clave 'nombre'
nombre = diccionario['nombre']
print(nombre)  # Imprime: Carlos



# 2. AÑADIR UN ELEMENTO A UN DICCIONARIO
diccionario = {'nombre': 'Carlos', 'edad': 30, 'profesión': 'programador'}
# Añadir una nueva clave-valor al diccionario
diccionario['ciudad'] = 'Santiago'
print(diccionario)  # Imprime: {'nombre': 'Carlos', 'edad': 30, 'profesión': 'programador', 'ciudad': 'Santiago'}



# 3. MODIFICAR UN ELEMENTO DE UN DICCIONARIO
diccionario = {'nombre': 'Carlos', 'edad': 30, 'profesión': 'programador'}
    # Modificar el valor asociado a la clave 'edad'
diccionario['edad'] = 31
print(diccionario)  # Imprime: {'nombre': 'Carlos', 'edad': 31, 'profesión': 'programador'}


# 4. ELIMINAR UN ELEMENTO DE UN DICCIONARIO
diccionario = {'nombre': 'Carlos', 'edad': 30, 'profesión': 'programador'}

    # Eliminar la clave-valor asociada a la clave 'profesión'
del diccionario['profesión']
print(diccionario)  # Imprime: {'nombre': 'Carlos', 'edad': 30}


# la función dict, por si sola crea un diccionario vacio
empty_dict_2= dict()
print(empty_dict_2)



# Crear un diccionario con la función dict
full_dict = dict(
    genero = "M",
    Nacionalidad = "E" 
)
print(full_dict)


# ¿COMO ITERAR DICCIONARIOS?

# por valores
empleado = {
    "name":"valeria",
    "aellido": "roso",
    "edad": 18,
    "rut":"11.111.111-1"
}

    # value me dievuelve todos los valores de empleado, indipendientemente de su clave
for variable_x in empleado.values():
    print(variable_x)


empleado = {
    "name":"valeria",
    "aellido": "roso",
    "edad": 18,
    "rut":"11.111.111-1"
}
# Item agarra cada elemento, los separa en dos variables y los asigna a clave y valor... enteniendose que clave, sería el primer valor y valor el segundo
for clave, valor in empleado.items():
    print(clave,valor)
    
    
    


print("===========TRABAJANDO CON CONDICIONALES=================")

edad = 30

if edad > 50:
    print("hola Don")
    
    
temperatura = 35

if temperatura >= 37:
    print("Alerta de temperatura alta")
else:
    print("La temperatura aún es normal")
    
    

temperatura = 5
pais = 'Chile'

if temperatura <10:
    if pais =='chile':
        print('cccc')   
    else:
        print('zzzzz')
else:
    if pais== 'chile':
        print('XXXXX')
    else:
        print('2222')


if temperatura < 10:
    print('Es altamente probable nieve')
elif temperatura >= 10 and temperatura <=20:
    print('Es medianamente probable que nieva')
else:
    print('No hay posibilidades de nieve')


# and or not
# != para que no es igual en javascript es !==
#  en python es == para igualdad en javascript es ===


# Ejemplos de uso de not

x = True
print(not x)  # Imprime: False

y = False
print(not y)  # Imprime: True

z = (1 > 2)
print(not z)  # Imprime: True

# EJERCICIO MARVEL

# Escriba un programa que permita adivinar un personaje de marvel en base a estas 3 preguntas
# ¿Puede volar?, ¿Es humano?, ¿Tiene máscara?

print('==========TRABAJANDO CON CICLOS============')
print('==========WHILE 1============')

want_exit = 'n'
while want_exit =='n':
    print('¿Hola cómo estás?')
    want_exit = input('¿Quieres salir S/N?')
print('print fuera del while')

print('==========TRABAJANDO CON CICLOS============')
print('==========WHILE 2============')

want_exit = 'n'
num_questions = 0
while want_exit== 'n':
    print('Hola cómo estás?')
    want_exit = input('¿Quieres salir S/N?')
    num_questions +=1
    if num_questions == 4:
        print('Alcanzaste el máximo permitido')
        break

print('Se acabó el while')