

# 2. utilizando dos while anidados, construya la tablas de mutiplicacion, ejemplo
#     Ejemplo whiole anidados:
#     while codicion1
#         while codicion2
#             .....


valor_1 = 0
valor_2 = 0

while  0 <= valor_1 < 10:
    valor_2=0
    valor_1 +=1
    while 0 <= valor_2 < 10:
        valor_2 +=1
        multiplicacion= valor_1 * valor_2
        print (valor_1, 'X', valor_2, '=', multiplicacion )