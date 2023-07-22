#  opcion al trabajar con parametros indefinidos
def func(n1,n2,n3,n4,n5,n6):
    return n1+n2+n3+n4+n5+n6

suma = func(1,2,3,4,5,6)
# print(suma)

# Forma simple
def func(*args):
    for item in args:
        print(item)
        
        
# func("EDteam","Hola mundo",1,2,3,4,5,6,7,8,9,7,11)

#  Forma correcta
def func2(name,saludo="hola",*args):
    print(args)  # Estoy llamando a la tupla
    for item in args:
        print(item)  # Estoy llamando a cada uno de los elementos iterados de la tupla
    print(name,saludo)    

# func2("EDteam","Hola mundo",1,2,3,4,5,6,7,8,9,10)




# Enviando una estructura compleja como un diccionario: 
# KARGS
days = {
    "dia1":"Lunes",
    "dia2":"martes"
}
def func3(**kargs):
    print(kargs)

func3(**days)

# =======================
def func4(*args,**kargs):
    print(args)
    print(kargs)


# func4(1,2,3,4,5,6,7,**days)