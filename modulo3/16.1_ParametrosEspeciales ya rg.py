
# Puedo definir un valor por default a un parámetro
def suma(n1,n2,n3=10):
    print(n1 + n2+n3)

# una vez que enviamos nuestros argumentos con la variable , 
# en el siguiente argumento ya no puedo dejar de llamarlo 
# sin el nombre del parametro.
suma(1,n2=3,n3=5)


# Los parametros con valores por default debe ir siempre a la derecha
def sumados(n1,n2,n4,n6,n3=None,n5=10,):
    if n3 is not None:
        print(n1+n2+n3)
    else:
        print(n1+n2)
        
sumados(n1=2,n2=3,n3=10)


# Como trabajar muchos parametros indefinidos
