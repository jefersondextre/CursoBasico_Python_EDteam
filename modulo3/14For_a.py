# Recorriendo listas y tuplas
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for variable in numeros:
    print(variable)

# Recorriendo un diccionario
numeros_telefonicos = {
    'contacto1': 9970633,
    'contacto2': 9955554,
    'contacto3': 5570333
}

for clave, valor in numeros_telefonicos.items():
    print('La clave es: ' + str(clave) + ' y el valor es: '+str(valor))


