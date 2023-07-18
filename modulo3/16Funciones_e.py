# Retornar valores en tupla

def asignar_valores(x,y):
    x=x+1
    y= y+1
    return x,y


# print(asignar_valores(4,5))





'''
funcion =>  Una funcion siempre devuelve un valor (return)
procedimientos => No devuelve un valor

Resumen: Si la funcion no retorna ningun valor igual devuelve un None de forma implicita al no establecer algun return.
scope = Es el alcance que tiene una variable dentro del código.
'''

# variable global
name="Kevin"

def saludo():
    print("hola Jeferson Dextre")
    
# saludo()
# print(saludo())


def func():
    # name = "Jeff"
    global name
    name = name + " hola"
    print(name)

func()