words = "Esto es una cadena de texto "


word = ''
for letter in words:
    if letter != ' ':
        word += letter
    else:
        print(word)
        word =''
        
        
        
for letter in words:
    if letter != ' ':
        print(letter)
    else:
        break

animals_list = ['Gato', 'Perro', 'Pájaro', 'Ardilla']

for animal in animals_list:
    print(animal)



list1 = range(1, 3)
print(list1)

for number_in in range(1,10):
    print(number_in)


for number_in in range(1,10,2):
    print(number_in)




for num_tabla in range (1,11):
    for num_mul in range (1,11):
        result = num_tabla * num_mul
        print(f'{num_tabla} X {num_mul} = {result}')
    print("_______________________________")
    
    


# lista de listas

double_list = [[1,2,3],[4,6,7]]
print(double_list[0])
print(double_list[1])

print(double_list[1][1])

double_list[0].pop()
print(double_list)
