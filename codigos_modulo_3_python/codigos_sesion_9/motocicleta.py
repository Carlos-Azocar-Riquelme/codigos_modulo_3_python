

# Punto 1 
class Motocicleta:
    is_new= True # Punto 2
    motor = False #Punto 5
    
    # Punto 3
    def __init__(self, _color, _matricula, _combustible_litros, _numero_ruedas,
                _marca, _modelo, _fecha_fabricacion, _velocidad_punta, _peso, _capacidad_max_combustible):
        self.color = _color
        self.matricula =_matricula
        self.combustible_litros =_combustible_litros
        self.numero_ruedas =_numero_ruedas
        self.marca = _marca
        self.modelo = _modelo
        self.fecha_fabricacion = _fecha_fabricacion
        self.velocidad_punta = _velocidad_punta
        self.peso = _peso
        self.capacidad_max_combustible = _capacidad_max_combustible
        


# Punto 6

#Opción 1
    # def arrancar(self):
    #     if self.motor == True: #En este caso, puedo quitar el ==True y funcionará igual
    #         print('El motor ya está arrancado')
    #     else:
    #         print('El motor ha arrancado')


    # def detener(self):
    #     if self.motor == False: # en este caso puedo quitar el False y colocar not, es decir, if not self.motor:
    #         print('El motor ya estaba detenido')
    #     else:
    #         print('El motor se ha apagado')
    


    # Método arrancar(): 
    # - Si el motor está detenido, se indica que el motor ha arrancado
    # - Si el motor ya está en marcha y se intenta arrancar de nuevo, se indica que el motor ya estaba en marcha.
    
    def arrancar(self):
        if self.motor == False: #En este caso, puedo quitar el ==True y funcionará igual
            print('El motor ha arrancado')
        else:
            print('El motor ya está arrancado')             

    
    # Método detener()
    # Si el motor está en marcha, se indica que el motor se ha detenido
    # Si el motor está ya detenido, y se intenta detener de nuevo, se indica que el motor ya estaba detenido

    def detener(self):
        if self.motor == True: # en este caso puedo quitar el False y colocar not, es decir, if not self.motor:
            print('El motor se ha detenido')
        else:
            print('El motor ya está detenido')
            
    def consultar_precio(self):
        print(f'El precio de la motocicleta {self.marca}, modelo {self.modelo}, es de ${self.precio}')

    def consultar_combustible(self):

        self.combustible_faltante= self.capacidad_max_combustible - self.combustible_litros #¿Se pueden hacer cálculos en los atributos?
        print(f'Reporte del depósito de la motocicleta Marca: {self.marca}; Modelo: {self.modelo}; Matricula {self.matricula}')        
        print(f'La cantidad de combustible en el tanque es de {self.combustible_litros} litros, la capacidad máxima del estanque es de {self.capacidad_max_combustible} litros y faltan {self.combustible_faltante} litros para completar el tanque.')


    def repostar(self):     
        validacion_combustible_repostar = False
        self.combustible_faltante= self.capacidad_max_combustible - self.combustible_litros #¿Se pueden hacer cálculos en los atributos?
        # Repetir hasta que el usuario ingrese un número
        while validacion_combustible_repostar==False:   #También se puede hacer con un while True, en cuando se cumpla, se coloca el break
            valor_combustible_repostar = input("¿Cuántos litros desea repostar? ")
            try:
            # Intentar convertir el valor a float
                numero_combustible_repostar= float(valor_combustible_repostar)
                if numero_combustible_repostar >= 0 and numero_combustible_repostar <= self.combustible_faltante:
                    validacion_combustible_repostar= True
                    self.combustible_litros = numero_combustible_repostar + self.combustible_litros
                    self.combustible_faltante= self.capacidad_max_combustible - self.combustible_litros
                    print(f'Has recargado {numero_combustible_repostar} litros. La nueva cantidad de combustible es {self.combustible_litros} litros.')
                else:
                    print(f'La cantidad de litros tiene que ser mayor a 0 y menor o igual a {self.combustible_faltante} litros \n')
            except ValueError:
            # Si la conversión falla, imprimir un mensaje de error
                print("El valor ingresado tiene que ser un número entero o decimal.\n")

# # punto 7
# motocicleta_1= Motocicleta('Rojo', 'ABCD-1234', 10, 2, 'Honda','CB300R', 2018, 300, 143)

# print(motocicleta_1.color, 
#     motocicleta_1.matricula,
#     motocicleta_1.combustible_litros,
#     motocicleta_1.numero_ruedas,
#     motocicleta_1.marca,
#     motocicleta_1.modelo,
#     motocicleta_1.fecha_fabricacion,
#     motocicleta_1.velocidad_punta,
#     motocicleta_1.peso)

# # Punto 8

# motocicleta_2 = Motocicleta(
#     _peso = 150,
#     _velocidad_punta = 350,
#     _fecha_fabricacion = 2022,
#     _modelo = 'Suzuki',    
#     _marca = 'GSX150FI',
#     _numero_ruedas = 2,
#     _combustible_litros = 0,
#     _matricula = 'EFGH-5678',
#     _color = 'Green', 
# )

# print(motocicleta_2.color, 
#     motocicleta_2.matricula,
#     motocicleta_2.combustible_litros,
#     motocicleta_2.numero_ruedas,
#     motocicleta_2.marca,
#     motocicleta_2.modelo,
#     motocicleta_2.fecha_fabricacion,
#     motocicleta_2.velocidad_punta,
#     motocicleta_2.peso)


# # Punto 9
# # motocicleta_1.arrancar()
# # motocicleta_2.detener()

# motocicleta_1.arrancar()
# motocicleta_1.detener()


# # Punto 10
# motocicleta_1.precio = 3000000

# # punto 11
# print(f'El precio de la motocicleta {motocicleta_1.marca}, modelo {motocicleta_1.modelo}, es de ${motocicleta_1.precio}')

# # punto 12
# motocicleta_1.consultar_precio()

# # Punto 13
# motocicleta_2.consultar_precio()





#  Punto 14
# Instanciamiento de la clase con argumentos posicionales
# motocicleta_3= Motocicleta('Rojo', 'ABCD-1234', 10, 2, 'Honda','CB300R', 2018, 300, 143,15)

# Instanciamiento de la clase con argumentos de clave
motocicleta_3 = Motocicleta(
    _peso = 143,
    _velocidad_punta = 300,
    _fecha_fabricacion = "2020-04-12",
    _modelo = 'Honda',    
    _marca = 'CB300R',
    _numero_ruedas = 2,
    _combustible_litros = 10,
    _matricula = 'ABCD-1234',
    _color = 'Rojo',
    _capacidad_max_combustible = 17
)

motocicleta_4 = Motocicleta(
    _peso = 160,
    _velocidad_punta = 280,
    _fecha_fabricacion = "2022-12-05",
    _modelo = 'Suzuki',    
    _marca = 'GSX150FI',
    _numero_ruedas = 2,
    _combustible_litros = 3,
    _matricula = 'EFGH-5678',
    _color = 'Green',
    _capacidad_max_combustible = 20
)

print('\n')
print('************** Motocicleta 1 ******************')
print('\n')

motocicleta_3.consultar_combustible()

print('\n')

motocicleta_3.repostar()

print('\n')

motocicleta_3.consultar_combustible()

print('\n')

print('************** Motocicleta 2 ******************')

print('\n')

motocicleta_4.consultar_combustible()

print('\n')

motocicleta_4.repostar()

print('\n')

motocicleta_4.consultar_combustible()

print('\n')
