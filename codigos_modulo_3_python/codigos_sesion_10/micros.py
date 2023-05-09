
class Sistema_Pagos_Micros:
    micros = []
    
    def __init__(self):
        pass

    @classmethod
    def registrar_micro(cls, _nombre_conductor, _patente_micro):
        # Verificar si la patente ya existe en la lista de micros
        for micro_existente in cls.micros:
            if micro_existente['patente_micro'] == _patente_micro:
                print(f'Error: La patente {_patente_micro} ya existe.')
                return
            
        # Si la patente no existe, registra la nueva micro (fuera del bucle for)
        micro = {
            'nombre_conductor': _nombre_conductor,
            'patente_micro': _patente_micro,
            'recaudacion': 0,
            'movimientos': [] 
        }
        cls.micros.append(micro)
        print(f'Micro patente: {_patente_micro}, conductor: {_nombre_conductor}, agregado con éxito')

        
    @classmethod
    def agregar_movimiento(cls, _patente_micro, _tipo_pasajero, _fecha):
        
        cobro_general=730
        cobro_menores= 0
        cobro_adultos_mayores= cobro_general/2
        
        # Las personas que aboradan la micro son, mujeres, hombres, niños y aduto mayor, de los cuales los niños no pagan y lso adultos mayores pagan la tarifa
        
        for micro in cls.micros:
            if micro['patente_micro'] == _patente_micro:
                if _tipo_pasajero == 'Menor':
                    micro['recaudacion'] += cobro_menores
                    movimiento = {
                        'id': len(micro['movimientos']) + 1,
                        'tipo': _tipo_pasajero,
                        'monto': micro['recaudacion'],
                        'fecha': _fecha,
                        'pasaje': cobro_menores
                    }
                    micro['movimientos'].append(movimiento)
                elif _tipo_pasajero =='Adulto Mayor':
                    micro['recaudacion'] += cobro_adultos_mayores
                    movimiento = {
                        'id': len(micro['movimientos']) + 1,
                        'tipo': _tipo_pasajero,
                        'monto': micro['recaudacion'],
                        'fecha': _fecha,
                        'pasaje': cobro_adultos_mayores
                    }
                    micro['movimientos'].append(movimiento)
                elif _tipo_pasajero == 'Adulto':
                    micro['recaudacion'] += cobro_general
                    movimiento = {
                        'id': len(micro['movimientos']) + 1,
                        'tipo': _tipo_pasajero,
                        'monto': micro['recaudacion'],
                        'fecha': _fecha,
                        'pasaje': cobro_general
                    }
                    micro['movimientos'].append(movimiento)

                else:
                    print('Tipo de movimiento no válido')
                    return
                print('Movimiento realizado con éxito')
                return
        print(f'La patente {_patente_micro} no existe')

        
    @classmethod
    def ver_reporte_operacion_patente(cls, _patente_micro):
        # for micro in cls.micros:
        #     if micro['patente_micro'] == _patente_micro:
        #         print('Los datos son: ')
        #         print('Nombre del conductor:', micro['nombre_conductor'])
        #         print('Patente:', micro['patente_micro'])
        #         print('Movimientos:')
        #         for movimiento in micro['movimientos']:
        #             print('- ID:', movimiento['id'])
        #             print('  Tipo:', movimiento['tipo'])
        #             print('  Monto:', movimiento['monto'])
        #             print('  Fecha:', movimiento['fecha'])
        #         return
        # print(f'La Patente {_patente_micro} no existe')

        for micro in cls.micros:
            if micro['patente_micro'] == _patente_micro:
                print("{:<20}".format("Fecha"), "{:<20}".format("Nombre del conductor"), "{:<20}".format("Patente"), "{:<20}".format("ID"), "{:<20}".format("Tipo"), "{:<20}".format("Monto"))
                for movimiento in micro['movimientos']:
                    print("{:<20}".format(movimiento['fecha']), "{:<20}".format(micro['nombre_conductor']), "{:<20}".format(micro['patente_micro']), "{:<20}".format(str(movimiento['id'])), "{:<20}".format(movimiento['tipo']), "{:<20}".format(str(movimiento['pasaje'])))
                return
        print(f'La Patente {_patente_micro} no existe')
        
        
        
    @classmethod
    def ver_reporte_operacion(cls):
        for micro in cls.micros:
            print("{:<20}".format("Fecha"), "{:<20}".format("Nombre del conductor"), "{:<20}".format("Patente"), "{:<20}".format("Total"))
            for movimiento in micro['movimientos']:
                print("{:<20}".format(movimiento['fecha']), "{:<20}".format(micro['nombre_conductor']), "{:<20}".format(micro['patente_micro']), "{:<20}".format(str(movimiento['pasaje'])))
            
        
    @classmethod
    def ver_reporte_operacion_dia(cls, _fecha):
        # for micro in cls.micros:
        #     for movimiento in micro['movimientos']:
        #         if movimiento['fecha'] == _fecha:
        #             print('Nombre del conductor:', micro['nombre_conductor'])
        #             print('Patente:', micro['patente_micro'])
        #             print('  Fecha:', movimiento['fecha'])
        #             print('- ID:', movimiento['id'])
        #             print('  Tipo:', movimiento['tipo'])
        #             print('  Monto:', movimiento['monto'])

        print("{:<20}".format("Fecha"), "{:<20}".format("Nombre del conductor"), "{:<20}".format("Patente"), "{:<20}".format("ID"), "{:<20}".format("Tipo"), "{:<20}".format("Monto"))
        for micro in cls.micros:
            movimientos_micros = list(filter(lambda movimiento: movimiento['fecha'] == _fecha, micro['movimientos']))
            for movimiento in movimientos_micros:
                print("{:<20}".format(str(movimiento['fecha'])), "{:<20}".format(micro['nombre_conductor']), "{:<20}".format(micro['patente_micro']), "{:<20}".format(str(movimiento['id'])), "{:<20}".format(movimiento['tipo']), "{:<20}".format(str(movimiento['pasaje'])))

    
    @classmethod
    def ver_reporte_operacion_conductor(cls, _nombre_conductor):
        print("{:<20}".format("Fecha"), "{:<20}".format("Nombre del conductor"), "{:<20}".format("Patente"), "{:<20}".format("ID"), "{:<20}".format("Tipo"), "{:<20}".format("Monto"))
        for micro in cls.micros:
            if micro['nombre_conductor'] == _nombre_conductor:
                for movimiento in micro['movimientos']:
                    print("{:<20}".format(str(movimiento['fecha'])), "{:<20}".format(micro['nombre_conductor']), "{:<20}".format(micro['patente_micro']), "{:<20}".format(str(movimiento['id'])), "{:<20}".format(movimiento['tipo']), "{:<20}".format(str(movimiento['pasaje'])))


micros_Spa= Sistema_Pagos_Micros()

print('\n')

micros_Spa.registrar_micro('Carlos Azócar', 'abcd-1234')


print('\n')

micros_Spa.registrar_micro('Camilo Azócar', 'efgh-5678')

print('\n')
print('Ver reporte de Operación por patente micro: abcd-1234')
micros_Spa.ver_reporte_operacion_patente('abcd-1234')

print('\n')
print('Ver reporte de Operación por patente micro: efgh-5678')
micros_Spa.ver_reporte_operacion_patente('efgh-5678')

# Agrega pasajeros a micro 1

print('\n')
print('Agrega un pasajero Menor de edad a la Micro patente "abcd-1234" ')
micros_Spa.agregar_movimiento('abcd-1234','Menor', '2023-05-01')

print('\n')
print('Agrega un pasajero Menor de edad a la Micro patente "abcd-1234" ')
micros_Spa.agregar_movimiento('abcd-1234','Adulto', '2023-04-30')


# Agrega pasajeros a micro 2


print('\n')
print('Agrega un pasajero Adulto Mayor de edad a la Micro patente "efgh-5678" ')
micros_Spa.agregar_movimiento('efgh-5678','Adulto Mayor','2023-05-01')

print('\n')
print('Agrega un pasajero Adulto  de edad a la Micro patente "efgh-5678" ')
micros_Spa.agregar_movimiento('efgh-5678','Adulto','2023-05-01')

print('\n')
print('Agrega un pasajero Adulto  de edad a la Micro patente "efgh-5678" ')
micros_Spa.agregar_movimiento('efgh-5678','Adulto','2023-04-30')

print('\n')
print('Agrega un pasajero Adulto  de edad a la Micro patente "efgh-5678" ')
micros_Spa.agregar_movimiento('efgh-5678','Adulto Mayor','2023-04-30')


# Se genera un reporte de operación de ambos vehículos

print('\n')
print('Ver reporte de Operación por patente micro: abcd-1234')
micros_Spa.ver_reporte_operacion_patente('abcd-1234')

print('\n')
print('Ver reporte de Operación por patente micro: efgh-5678')
micros_Spa.ver_reporte_operacion_patente('efgh-5678')

# Filtro por día

print('\n')
print('Ver reporte de Operación para el día 2023-04-30')
micros_Spa.ver_reporte_operacion_dia('2023-04-30')


# Filtro por conductor

print('\n')
print('Ver reporte de Operación por Nombre del conductor')
micros_Spa.ver_reporte_operacion_conductor('Camilo Azócar')


# ver reporte de operación
print('\n')
print('Ver reporte de Operación')
micros_Spa.ver_reporte_operacion()