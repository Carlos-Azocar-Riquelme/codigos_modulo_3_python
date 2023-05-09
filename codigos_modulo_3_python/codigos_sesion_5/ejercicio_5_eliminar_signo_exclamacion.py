
# 5. Escriba un programa que eliminar un signo de exclamación del final de una cadena. puede suponer que los datos de entrada son siempre una cadena, no es necesario verificarlos.



tiene_interrogacion = False

while tiene_interrogacion == False:
    texto_usuario= input('Ingrese una texto con un signo de exclamación al final, para poder eliminarlo: ')
    lista_texto= list(texto_usuario)
    
    if lista_texto[-1] == "!":
        tiene_interrogacion= True
        lista_texto.pop()
        lista_texto_str = ''.join(lista_texto)
        print('Tu palabra sin singo de expclamación es:',lista_texto_str)
    else:
        print('El texto no termina con "!" , por favor infreselo nuevamente')



