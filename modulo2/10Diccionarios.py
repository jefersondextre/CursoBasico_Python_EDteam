# DICCIONARIOS SON COMO ARRAYS DE OBJETOS
mi_diccionario = {'hola': 'hello',
                  'rojo': 'red',
                  'libro': 'book'
                  }
print(type(mi_diccionario))
print(mi_diccionario)
# Modificando elementos por su clave
mi_diccionario['rojo'] = 'blue'
print(mi_diccionario)

# Eliminar
del(mi_diccionario['libro'])
print(mi_diccionario)

estudiante = {
    'Nombre': 'Juan',
    'Apellido': 'Rodriguez',
    'edad': 23,
    'Curso': 'Python'
}
print(estudiante)
# Agregando mas datos
estudiante = {
    'Nombre': 'Juan',
    'Apellido': 'Rodriguez',
    'edad': 23,
    'Cursos': {
        'nombre_curso': 'Python',
        'nivel': 'Basico'
    }
}
print(estudiante)
estudiante1 = {
    'Nombre': 'Jeferson',
    'Apellido': 'Rodriguez',
    'edad': 23,
    'Cursos': [
        {
            'nombre_curso': 'Python1',
            'nivel': 'Basico'
        },
        {
            'nombre_curso': 'Javascript1',
            'nivel': 'Intermedio'
        },
        {
            'nombre_curso': 'Php1',
            'nivel': 'Avanzado'
        }
    ]
}
print(estudiante1)
estudiante2 = {
    'Nombre': 'Jose',
    'Apellido': 'Rodriguez',
    'edad': 25,
    'Cursos': [
        {
            'nombre_curso': 'Python',
            'nivel': 'Basico'
        },
        {
            'nombre_curso': 'Javascript',
            'nivel': 'Intermedio'
        },
        {
            'nombre_curso': 'Php',
            'nivel': 'Avanzado'
        }
    ]
}
print(estudiante2)
print('######### 2 Diccionarios dentro de una lista ########')
# Añadiendo 2 diccionarios a una lista
estudiantes_listas = []
estudiantes_listas.append(estudiante1)
estudiantes_listas.append(estudiante2)
print(estudiantes_listas)
# Accediendo a un elemento del diccionario desde la lista
print('##### Accediendo a un elemento del diccionario 1 desde la lista  #####')
print(estudiantes_listas[0]['Nombre'])


print('##### Accediendo a los cursos del diccionario 2 desde la lista  #####')
print(estudiantes_listas[1]['Cursos'])
