# Parametros por defecto
# pasando parametros como diccionarios
def mi_funcion(texto1,texto2,**otrosparametros):
    print(otrosparametros)
    print(otrosparametros['nombre'])
    # print(texto1, texto2, sep='\n')
    
    

# mi_funcion('uno')
mi_funcion('este es el texto 1','Este es texto 2',nombre='Pablo',apellidos="Ordoñez" )
