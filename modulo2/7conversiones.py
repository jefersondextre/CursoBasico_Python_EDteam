numero1 = 9
numero2 = 1
suma = numero1 + numero2
# el print solo acepta concatenaciones de string por eso comvertimos a string la variable suma
print('El resultado es: '+str(suma))


numero_decimal = 1.2
print('numero flotante decimal',type(numero_decimal))
numero_decimal = str(1.2)
print('numero de string',type(numero_decimal))
booleano = str(True)
print(booleano)
print('booleano convertido a string', str(booleano))
# ----------------------------------------
numero_entero = 6
texto = '2.4'
print(type(numero_entero), type(texto))
numero_entero = float(6)
texto = float('2.4')
print(type(numero_entero), type(texto))
# -----------------------------------------
numero_decimal = 2.7
texto = '5'
print(type(numero_decimal), type(texto))
numero_decimal = int(2.7)
texto = int('5')
print(type(numero_decimal), type(texto))
# -------------------------------------------
print(bool(0), bool(''), bool('hola'), bool(-3.5))

# Da error por no ser posible realizar la conversión
# print(int('convierteme a numero entero'))
# print(float('convierteme a float'))
