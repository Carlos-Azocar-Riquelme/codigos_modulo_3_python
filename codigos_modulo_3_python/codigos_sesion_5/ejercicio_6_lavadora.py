
# 6. Se le asignado un tarea para programar un algoritmo para una lavadora, debe investigar cuanta agua se neceita para lavar prendas
#     con las siguientes caracteriticas, algodon, nilon, poliester, debe investigar para una lavadora de xx kg cuantas prendas de cada una puede 
#     lavar entendiendo, que solo se puede lavar ropa de un mismo tipo y asi poder calcular lo siguiente

#     Por ejemplo, si la carga es 10, la cantidad de agua que requiere es 5 y la cantidad de ropa a lavar es 14, entonces necesitas 5 * 1.1 ^ (14 - 10) cantidad de agua.

#     Escribe una función para calcular cuánta agua se necesita si tienes una cantidad de ropa.
#     La función aceptará 2 argumentos: - carga lavadora y ropa.

# si la lavadora tiene una capacidad de carga de 7 kg, se esperaría que use alrededor de 50-75 litros de agua por carga.


# ALGODON
# Como regla general, se estima que una prenda de algodón, como una camisa o un pantalón, ocupa aproximadamente 0,1 a 0,15 kilogramos. Por lo tanto, si una lavadora tiene una capacidad de carga de 7 kg, se pueden lavar entre 46 y 69 prendas de algodón por carga. Sin embargo, esta estimación es aproximada y puede variar en función del tamaño y la forma de las prendas.

# NILON
# Como regla general, se estima que una prenda de nailon, como una camiseta o unos pantalones cortos, ocupa aproximadamente 0,05 a 0,1 kilogramos. Por lo tanto, si una lavadora tiene una capacidad de carga de 7 kg, se pueden lavar entre 70 y 140 prendas de nailon por carga. Sin embargo, esta estimación es aproximada y puede variar en función del tamaño y la forma de las prendas.


# POLIESTER
# Como regla general, se estima que una prenda de poliéster, como una camiseta o unos pantalones cortos, ocupa aproximadamente 0,05 a 0,1 kilogramos. Por lo tanto, si una lavadora tiene una capacidad de carga de 7 kg, se pueden lavar entre 70 y 140 prendas de poliéster por carga. Sin embargo, esta estimación es aproximada y puede variar en función del tamaño y la forma de las prendas.

# consumo de agua https://es.calcuworld.com/cuantos/cuantos-litros-de-agua-consume-una-lavadora


cpacidad_kg_lavadora_usuario = 7
tipo_prenda_usuario= 'A'
numero_prenda_usuario= 46

def cantidad_agua_tipo_ropa(capacidad_kg_lavadora, numero_prendas, tipo_de_prendas):   
    
    if tipo_de_prendas == "A":
        capacidad_unidades_ropa_lavadora_algodon = capacidad_kg_lavadora/0.15 #calcula la cantidad de ropa máxima que el ususario puede ingresar en la lavadora, considerando el escenario más pesimista en que la ropa toma el valor promedio por unidad más alto, es decir, 0,15 kg/unidad.
        if numero_prendas <= capacidad_unidades_ropa_lavadora_algodon:
            
            
            print('podemos seguir lavando')
            cantidad_agua_tipo_ropa= numero_prendas*0.48
            
            
            
        else:
            print('Has exedido la capacidad de la lavadora, por favor, disminuye el número de prendas')
            
    elif tipo_de_prendas == "N":
        capacidad_unidades_ropa_lavadora_nilon = capacidad_kg_lavadora/0.1 #calcula la cantidad de ropa máxima que el ususario puede ingresar en la lavadora, considerando el escenario más pesimista en que la ropa toma el valor promedio por unidad más alto, es decir, 0,15 kg/unidad.
        if numero_prendas <= capacidad_unidades_ropa_lavadora_nilon:
            print('podemos seguir lavando')
            
            
            
            
            
            
        else:
            print('Has exedido la capacidad de la lavadora, por favor, disminuye el número de prendas')
    
    
    elif tipo_de_prendas == "P":
        capacidad_unidades_ropa_lavadora_poliester = capacidad_kg_lavadora/0.1 #calcula la cantidad de ropa máxima que el ususario puede ingresar en la lavadora, considerando el escenario más pesimista en que la ropa toma el valor promedio por unidad más alto, es decir, 0,15 kg/unidad.
        if numero_prendas <= capacidad_unidades_ropa_lavadora_poliester:
            print('podemos seguir lavando')
            
            
            
            
            
        else:
            print('Has exedido la capacidad de la lavadora, por favor, disminuye el número de prendas')
    
    


cantidad_agua_tipo_ropa(cpacidad_kg_lavadora_usuario,numero_prenda_usuario, tipo_prenda_usuario)
