try:
    numero = 2
    texto = 'Bienvenidos'
    suma = numero + texto
except TypeError as error:
    print('ERROR: El error es ' + str(error))
