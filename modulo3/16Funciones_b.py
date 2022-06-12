# Parametros por defecto
def mi_funcion(texto1,texto2='Este es el texto 2'):
    print(texto1, texto2, sep='\n')
    

mi_funcion('uno')
mi_funcion('uno',"Este es texto 2 modificado")
