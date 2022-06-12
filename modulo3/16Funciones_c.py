# Parametros por defecto
# Pasando parametros como lista
def mi_funcion(texto1,texto2,*otrosparametros):
    print(otrosparametros)
    print(texto1, texto2, sep='\n')
    
    

# mi_funcion('uno')
mi_funcion('este es el texto 1','Este es texto 2',1,2,3,4 )
