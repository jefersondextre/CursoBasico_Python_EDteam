mi_lista = [1, 2, 3, 4, 5]
print(mi_lista[3])
# Modificando elemento de una posicion definida
mi_lista[1] = 0
print(mi_lista)


lista_estudiantes = ['Pablo', 'jose', 'juan', 'luis']
# Accediendo al ultimo elemento de la lista
print(lista_estudiantes[-1])
# impresion de valores por rangos : posicion 1 hasta la posicion 2
print(lista_estudiantes[1:3])
print(lista_estudiantes[0:3])
print(lista_estudiantes[:3])
print(lista_estudiantes[1:-1])
print(lista_estudiantes[1:])

lista_combinada = ['hola', 0, 12.3, True, 'Bienvenido', True]
print(lista_combinada)

nuevaLista = [[1, 2, 3], [4, 5, 6], [7, 8, 9], lista_combinada]
print(nuevaLista[1][1])
print(nuevaLista)

# Modificando Listas con Métodos Predefinidos
# Añadiendo al inicio de la lista
lista_combinada.insert(0, 'Dato 1')
print(lista_combinada)

# Añadiendo elemento al final de la lista
lista_combinada.append('Nuevo Dato')
print(lista_combinada)

# Eliminando el ultimo elemento de la lista
lista_combinada.pop()
print(lista_combinada)

lista_combinada.pop(1)
print('Eliminando hola la posicion 1 ', lista_combinada)

# Eliminando por el valor
lista_combinada.remove('Bienvenido')
print(lista_combinada)

# Conocer cuantos elementos tiene una lista
print(len(lista_combinada), ' elementos en la lista')

# Contar cuantas veces se repite un elemento en la lista
print('se repite ', lista_combinada.count(True), ' veces')

# Bucar la posicion del elemento
print(lista_combinada.index(12.3))




 