condicion = True

if condicion:
    print('Se cumple la condicion')
else:
    print('No se cumple la condicion')

numero1 = 4
numero2 = 2

suma = numero1 + numero2
if suma == 9:
    print('la Suma si da 9')
else:
    numero1 = input('Ingrese el primer numero: ')
    numero2 = input('Ingrese el 2do numero: ')
    suma = int(numero1)+int(numero2)

    if suma == 9:
        print('Lo lograste!!...')
    else:
        print('No se cumple la condicion')
