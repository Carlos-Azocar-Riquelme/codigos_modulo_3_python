
# Creando una clase

class Trasnporte:
    pass

# pass permite declarar una clase vacía

# hacer uso del molde, para instanciarla (llamarla para que apartir de esa cclase, se cree un objeto) y crear un objeto

transporte_1 = Trasnporte()
transporte_2= Trasnporte()

print(type(transporte_1))


class Droid:
    def __init__(self): #Este es el método constructor
        self.power_on = False
    
    
    def switch_on(self):
        print('Hola soy un Droid, y estoy a tu orden')
        self.power_on = True
        
    def switch_off(self):
        print('Adios, enciéndeme cuiando me necesites')
        self.power_on = False


# por ahora siempre debe ser incluido dentro de la función



k8_arthur = Droid()
k8_citripio = Droid()


k8_arthur.switch_on()
print("power on Arthur",k8_arthur.power_on)

k8_citripio.switch_off()
print("power on tripio",k8_citripio.power_on)

k8_arthur.switch_off()
print(k8_arthur.power_on)


class Vehicle:
    def __init__(self, type, model):
        self.type_vehicle = type
        self.model_vehicle = model
        

sedan = Vehicle('Sedan', 'Aveo')
print(sedan.type_vehicle, sedan.model_vehicle)

pickup = Vehicle('Pickup', 'Ranger')
print(pickup.type_vehicle, pickup.model_vehicle)