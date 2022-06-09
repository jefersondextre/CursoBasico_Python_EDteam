
try:
    numero1 = input('Ingrese el numero 1: ')
    numero2 = input('Ingrese el numero 2: ')
    division = int(numero1)/int(numero2)
    print(division)
except ZeroDivisionError:
    print('Ha ocurrido un error, No se puede dividir para  cero')
except:
    print('Ingrese los numeros correctos')
finally:
    print('Ha finalizado el programa')
# Hay diferentes tipos de errores
# --------------------------------------
# ZeroDivisionError : error por Divison por cero.
# NameError : error por no declarar la variable.
#
