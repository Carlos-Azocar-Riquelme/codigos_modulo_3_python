

class Empleado:
    sueldo_base = 100.000
    
    def __init__(self, _name):
        self.__name = _name


# Esto es para atributos de la instancia
    @property
    def name(self):
        return self.__name
        
    @name.setter  #hace referencia al nombre de la función
    def name(self, _name):
        self.__name = _name

# Esto es para los atributos de los métodos
    @classmethod
    def get_sueldo_base(cls):  #Obtener
        return cls.sueldo_base
    
    @classmethod
    def set_sueldo_base(cls, _sueldo): #Modificar
        cls.sueldo_base = _sueldo