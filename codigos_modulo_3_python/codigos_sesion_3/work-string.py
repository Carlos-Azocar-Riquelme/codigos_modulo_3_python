first_name ="Carlos"
last_name="Azócar"

print(first_name + " " + last_name)

mensaje1= "Hola " * 3
print(mensaje1)

mensaje3 ="Carlos"
print(mensaje3)
mensaje3 += ","
print(mensaje3)

print(len(first_name)) #esto es una función

cadena= "Esto es una oración por Ucrania"
posicion = cadena.find("pelo")
print("Pelo se encuentra en: ", posicion)
posicion = cadena.find("Ucrania")
print("Ucrania se encuentra en: ", posicion)


#  convierte todos los caracteres de una cadena a minúsculas.
texto= "HELLO, WORLD!"
texto = texto.lower()
print(texto)


# Este método toma dos argumentos: la cadena a buscar y la cadena de reemplazo.
string = "Hello, world!"
string = string.replace("world", "Python") #esto es un método, es una función propia, es decir que nace a partir de un objeti, en este caso, la variable string
print(string)

print("=========== Listas ============")

empty_list = []
print(empty_list)

fullfiled_list = [1, 3, 500, 1.4, [2, "a"], {"name":"Richar"}, (1,3,5)]
print(fullfiled_list)

second_list = list() #permite convertir a lista o convertir un string en una lista
print(second_list)

print(list("Esto es una lista fragmentada"))


range_one = range(10)
print(list(range_one))

numeros = [1,4,6]
print(numeros)
numeros.append(7)
print(numeros)


print(numeros[3])




# ITERAR ELEMENTOS DE UNA LISTA

mi_lista = [1, 2, 3, 4, 5]

for elemento in mi_lista:
    print(elemento)



# ELIMINANDO ELEMENTOS 

# Utilizando el método remove: Este método eliminará la primera aparición del elemento especificado en la lista.
mi_lista = [1, 2, 3, 4, 5]
mi_lista.remove(3)
print(mi_lista)  # [1, 2, 4, 5]


# Utilizando el método del: Este método elimina un elemento en una posición específica en la lista.
mi_lista = [1, 2, 3, 4, 5]
del mi_lista[2]
print(mi_lista)  # [1, 2, 4, 5]


# ELIMINAR EL ÚLTIMO ELEMENTO DE UNA LISTA

# Utilizando el método pop: Este método elimina el último elemento de la lista y devuelve su valor.
mi_lista = [1, 2, 3, 4, 5]
ultimo_elemento = mi_lista.pop()
print(mi_lista)  # [1, 2, 3, 4]
print(ultimo_elemento)  # 5


# Utilizando la notación de índice negativo: Los índices negativos se refieren a los elementos desde el final de la lista, por lo que puedes utilizar -1 para hacer referencia al último elemento.
mi_lista = [1, 2, 3, 4, 5]
del mi_lista[-1]
print(mi_lista)  # [1, 2, 3, 4]


# MODIFICAR ELEMENTOS DE UNA LISTA

# Modificando un elemento en una posición específica: Puedes asignar un nuevo valor a una posición específica en la lista.
mi_lista = [1, 2, 3, 4, 5]
mi_lista[2] = 6
print(mi_lista)  # [1, 2, 6, 4, 5]

# TUPLAS

# son inmutables

empty_tuple = ()
fullfiled_tuple = (1, "Carlos")

print(empty_tuple, fullfiled_tuple)

one_tuple_string = ('juan')
print(type(one_tuple_string)) #si lo definimos como una tupla de 1, lo interpretará como string, porque es solo un elemento

one_tuple_tuple =('juan',) #para que realmente lo tome como una tupla, hay que ponerle una "," al final
print(type(one_tuple_tuple))

# se pueden declarar tuplas sin parentesis, pero es mala práctica

hojas = 'carta', 'oficio'
print(type(hojas))
print(hojas)

empty_tuple_2 = tuple()

list_to_convert = [2,6,8,9]
print(list_to_convert)

tuple_converted = tuple(list_to_convert)
print(tuple_converted)


# métodos de las tuplas


# reverse(): Este método invierte el orden de los elementos en una lista. Por ejemplo:
mi_lista = [1, 2, 3, 4, 5]
mi_lista.reverse()
print(mi_lista)  # [5, 4, 3, 2, 1]




# Más métodos de listas 

# reverse(): Este método invierte el orden de los elementos en una lista. Por ejemplo:
mi_lista = [1, 2, 3, 4, 5]
mi_lista.reverse()
print(mi_lista)  # [5, 4, 3, 2, 1]

# append(): Este método agrega un nuevo elemento al final de una lista. Por ejemplo:
mi_lista = [1, 2, 3, 4, 5]
mi_lista.append(6)
print(mi_lista)  # [1, 2, 3, 4, 5, 6]

# extend(): Este método agrega varios elementos a la lista al mismo tiempo. Por ejemplo:
mi_lista = [1, 2, 3, 4, 5]
mi_lista.extend([6, 7, 8])
print(mi_lista)  # [1, 2, 3, 4, 5, 6, 7, 8]

# remove(): Este método elimina la primera aparición de un elemento específico en una lista. Por ejemplo:
mi_lista = [1, 2, 3, 4, 5]
mi_lista.remove(3)
print(mi_lista)  # [1, 2, 4, 5]

# clear(): Este método elimina todos los elementos de una lista. Por ejemplo:
mi_lista = [1, 2, 3, 4, 5]
mi_lista.clear()
print(mi_lista)  # []

# sort(): Este método ordena los elementos de una lista en orden ascendente o en otro orden específico. Por ejemplo:
mi_lista = [5, 3, 2, 4, 1]
mi_lista.sort()
print(mi_lista)  # [1, 2, 3, 4, 5]


# aplicarlo con tuplas

# reverse(): Puedes crear una nueva tupla que incluya los elementos de la tupla original en orden inverso. Por ejemplo:
mi_tupla = (1, 2, 3, 4, 5)
mi_nueva_tupla = mi_tupla[::-1]
print(mi_nueva_tupla)  # (5, 4, 3, 2, 1)


# append(): No puedes agregar elementos a una tupla una vez creada, pero puedes crear una nueva tupla que incluya los elementos originales más los nuevos. Por ejemplo:
mi_tupla = (1, 2, 3, 4, 5)
mi_nueva_tupla = mi_tupla + (6,)
print(mi_nueva_tupla)  # (1, 2, 3, 4, 5, 6)

# extend(): No puedes agregar varios elementos a una tupla una vez creada, pero puedes crear una nueva tupla que incluya los elementos originales más los nuevos. Por ejemplo:
mi_tupla = (1, 2, 3, 4, 5)
mi_nueva_tupla = mi_tupla + (6, 7, 8)
print(mi_nueva_tupla)  # (1, 2, 3, 4, 5, 6, 7, 8)

# remove(): No puedes eliminar elementos de una tupla una vez creada, pero puedes crear una nueva tupla que excluya el elemento deseado. Por ejemplo:
mi_tupla = (1, 2, 3, 4, 5)
mi_nueva_tupla = tuple(elemento for elemento in mi_tupla if elemento != 3)
print(mi_nueva_tupla)  # (1, 2, 4, 5)


