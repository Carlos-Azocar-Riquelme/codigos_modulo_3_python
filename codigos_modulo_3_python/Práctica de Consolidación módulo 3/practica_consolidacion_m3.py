

# FILTRANDO DATOS

# INSTRUCCIONES

# Lee con atención cada uno de los requerimientos que se presentan a continuación, y desarrolla la prueba de acuerdo con lo solicitado.
# DESCRIPCIÓN


# Dada la siguiente lista de nombres:
# • Harry Houdini,Newton, David Blaine, Hawking, Messi, Teller, Einstein, Pele, Juanes
# Y sabiendo que Harry Houdini, David Blaine y Teller son magos. 
# Y también que Newton, Hawking y  Einstein son científicos. 
# Debemos separar los nombres en tres grupos: magos, científicos y otros; 

magos= ['Harry Houdini', 'David Blaine', 'Teller']
cientificos = ['Newton', 'Hawking', 'Einstein']
otros = ['Messi', 'Juanes']

# y escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la
# frase ‘El gran‘ antes del nombre de cada mago.

def hacer_grandioso(nombres):
    for nombre in range(len(nombres)):
        nombres[nombre] = "El gran " + nombres[nombre]
    return nombres


# Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la lista.

def imprimir_nombres(*lista_nombres):
    lista_completa = []
    for nombre in range(len(lista_nombres)):
        lista_completa = lista_completa + lista_nombres[nombre]
    print(lista_completa)
    
    print('\nLos nombres impresos por separados son:')
    for nombre in range(len(lista_completa)):
        print(lista_completa[nombre])




# Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; 

print('\n')
print('La lista de nombres completa antes de ser modificada es: ')
imprimir_nombres(magos, cientificos, otros)


# luego imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.

print('\n')
print('La lista de nombres completa después de ser modificada es: ')
imprimir_nombres(hacer_grandioso(magos), cientificos, otros)
