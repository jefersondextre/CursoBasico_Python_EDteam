numero_ingresado = int(input('Ingrese un numero:'))

# if numero_ingresado == 1:
#     print('Ingresaste el numero 1')
# else:
#     if numero_ingresado == 2:
#         print('Ingresaste el numero 2')
#     else:
#         if numero_ingresado == 3:
#             print('Ingresaste el numero 3')
#         else:
#             print('No ingreaste los numeros esperados.')

if numero_ingresado == 1:
    print('Ingresaste el numero 1')
elif numero_ingresado == 2:
    print('Ingresaste el numero 2')
elif numero_ingresado == 3:
    print('Ingresaste el numero 3')
else:
    print('No ingreaste los numeros esperados.')

# Otra forma de ingresar condicionales
if numero_ingresado == 1 or numero_ingresado == 2 or numero_ingresado == 3:
    print('Ingresaste el numero correcto')
else:
    print('No ingreaste los numeros esperados.')
