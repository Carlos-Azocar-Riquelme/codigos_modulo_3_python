# EJERCICIO MARVEL

# Escriba un programa que permita adivinar un personaje de marvel en base a estas 3 preguntas
# ¿Puede volar?, ¿Es humano?, ¿Tiene máscara?

volador = 'No'
humano= 'No'
enmascarado='No'

if volador == 'Si':
    if humano == 'Si' :
        if enmascarado == 'Si':
            print('El personaje es volador, humano y enmascarado')
        else:
            print('El personajes es volador, humano, pero no enmascarado')
    else:
        if enmascarado == 'Si':
            print('El personaje vuela, no es humano, pero si enmascarado')
        else:
            print('El personaje vuela, no es humano y no es enmascarado ')
else:
    if humano=='Si':
        if enmascarado=='Si':
            print('El personaje no es volador, si humano y enmascarado')
        else:
            print('El personaje no es volador, si es humano, pero no enmascarado')
    else:
        if enmascarado== 'Si':
            print('el personaje no es volador, no es humano, pero si enmascarado')
        else:
            print('El personaje no es volador, no es humano, ni es enmascarado')
