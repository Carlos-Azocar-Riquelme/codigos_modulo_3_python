

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

gato = Animal("Angora", "Persa")
print(gato.type) #sirve para conocer el valor de un atributo

gato.type = "Grandanes" #Sirve para modificar el valor 
print(gato.type)


class Hero:
    def __init__(self, name, super_power):
        self.name = name
        self.super_power = super_power



batman = Hero("Batman", "Intelligence")
print(batman.super_power)

batman.super_power = "Money"
print(batman.super_power)


# @property ----> este sería como el getter .... lo que se pone verde es un decorador
# .setter  ----> este sería como el setter

print("__________________________________")

class Droid:
    def __init__(self, name):
        self.hidden_name = name
        
    @property #Es como el getter
    def name(self) -> str:
        return self.hidden_name
    
    @name.setter
    def name(self, name:str) -> None:
        self.hidden_name= name
        
        
        
androide = Droid("Arthur")
print(androide.name)

androide.name = "Citripio"
print(androide.name)


androide.hidden_name= "Rojo"
print(androide.hidden_name)
print(androide.name)

print("__________________________________")


# VALORES CALCULADOS
# Jamás reciben parámetros

class CalculateValue:
    def __init__ (self, _name, _height):
        self.name= _name
        self.height = _height
        
    @property
    def get_calculate_value(self) -> float:
        return 0.35* self.height

valuex= CalculateValue("ratio", 10)
print(f'El ratio de {valuex.name} es_ {valuex.get_calculate_value}')



print("__________________________________")

class Dog:
    obeys_owner = True
    def __init__(self, name):
        self.name = name


dog_one = Dog("Robin")
dog_two = Dog("Malta")
dog_three = Dog("Luz")

print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owner}')


print("__________________________________")

dog_one.obeys_owner = False
dog_two.obeys_owner = False


print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owner}')


print("__________________________________")

Dog.obeys_owner = True
print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owner}')