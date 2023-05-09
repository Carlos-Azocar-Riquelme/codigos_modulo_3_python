
import random

defensa_a = random.randint(1,100)
print(f'La defensa de a es {defensa_a}')
defensa_b = random.randint(1,100)
print(f'La defensa de b es {defensa_b}')

primer_jugador= random.randint(1,2)

if primer_jugador == 1:
    print('El jugador que parte es a')
else:
    print('El jugador que parte es b')
muerto = False

if primer_jugador == 1:
    while muerto == False:
        ataque_a = random.randint(1,10)
        print(f'El ataque de a fue {ataque_a}')
        
        defensa_b = defensa_b - ataque_a
        print(f'la nueva defensa de b es {defensa_b}')
        
        if defensa_b <= 0:
            muerto = True
            print('El jugador b murió :(')
        else:
            ataque_b = random.randint(1,10)
            print(f'El ataque de b fue {ataque_b}')
            defensa_a = defensa_a - ataque_b
            print(f'la nueva defensa de a es {defensa_a}')
        
            if defensa_a <= 0:
                muerto = True
                print('El jugador a murió :(')
else:
    while muerto == False:
        
        ataque_b = random.randint(1,10)
        print(f'El ataque de b fue {ataque_b}')
        
        defensa_a = defensa_a - ataque_b
        print(f'la nueva defensa de a es {defensa_a}')
        
        if defensa_a <= 0:
            muerto = True
            print('El jugador a murió :( ')
        else:
            ataque_a = random.randint(1,10)
            print(f'El ataque de a fue {ataque_a}')
            defensa_b = defensa_b - ataque_a
            print(f'la nueva defensa de b es {defensa_b}')
        
            if defensa_b <= 0:
                muerto = True
                print('El jugador b murió :( ')