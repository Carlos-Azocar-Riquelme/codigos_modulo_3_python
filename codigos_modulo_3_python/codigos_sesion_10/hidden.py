class Droid:
    def __init__(self, name):
        self.__name = name
        
    @property #Es como el getter
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name:str) -> None:
        self.__name= name
        
androide = Droid("Arthur")
print(androide.name)
# print(androide.__name)

# Cree una clase llamada Artefacto, agreguele 3 atributos y utilice los getter and setter para acceder a ellos


class Artefacto:
    def __init__(self, _nombre, _color, _precio):
        self.__nombre = _nombre
        self.__color = _color
        self.__precio = _precio

    @property
    def _nombre(self) -> str:
        return self.__nombre
    
    @property
    def _color(self) -> str:
        return self.__color
    
    @property
    def _precio(self) -> str:
        return self.__precio
    
    @_nombre.setter
    def _nombre(self, _nombre:str) -> None:
        self.__nombre= _nombre
    
    @_color.setter
    def _color(self, _color:str) -> None:
        self.__color= _color
        
    @_precio.setter
    def _precio(self, _precio:float) -> None:
        self.__precio= _precio
        
artefacto_1 = Artefacto('Calculadora', 'Negra', 45000)
print(artefacto_1._nombre ,artefacto_1._color, artefacto_1._precio)
# print(artefacto_1.__nombre ,artefacto_1.__color, artefacto_1.__precio)

