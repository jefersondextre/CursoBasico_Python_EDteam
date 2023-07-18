def mi_funcion(param1,param2):
    print(param1,' esta es mi primera funcion en python', param2)
    

# mi_funcion('Hola', 20)
# Intercambiar el orden los parametros.
# mi_funcion(param2='Hola',param1= 20)



# la variable world no existe por fuera de la funcion
word = "hola "
def imprimir(letra):
    word += letra
    print(word)

imprimir('juan')
