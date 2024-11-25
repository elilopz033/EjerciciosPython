# Conversion de tipos de datos

#Convertir de cadena a numero
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Valor numérico en cadena: {numero_cadena}')
print(f'Cadena a entero: {numero_entero}')

#Convertir de cadena a float
numero_cadena = '3.14'
numero_float = float(numero_cadena)
print(f'Cadena a float: {numero_float}')

#Convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Numero a cadena: {numero_cadena}')

#Convertir a booleano
'''
Tipo bool es False en los siguientes casos
Si el valor es 0, cadena vacia, o None, entonces regresa False
Regresa True, si el calor es distinto de 0, si es distinto de cadena vacia
y también si es distinto de None
'''

numero_entero = 0
boolean = bool(numero_entero)
print(f'Valor booleano de 0: {boolean}') #False, incluye 0, 0.0

numero_entero = 5
boolean = bool(numero_entero)
print(f'Valor booleano de 5: {boolean}') #Tue


cadena = ''
boolean = bool(cadena)
print(f'Valor booleano de cadena vacía: {boolean}') #False, Incluye colecciones vacías

cadena = 'Cadena con valor'
boolean = bool(cadena)
print(f'Valor booleano de cadena NO vacía: {boolean}')

variable = None
boolean = bool(variable)
print(f'Valor booleano de None: {boolean}') #False


