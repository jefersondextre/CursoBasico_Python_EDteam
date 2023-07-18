# try_except.by
'''
try : Evalua una porcion de codigo
except : manejamos el pasible error
else : se ejecuta cuando no hay un error
finally : se ejeecuta independientemente de lo que suceda en try o exept
 
'''

try:
    # print("Edteam",hola)
    raise Exception ("Error creado  a proposito")
except Exception:
    print("Hubo un error")
else:
    print("No hubo error")
finally:
    print("Esto siempre se ejecuta")