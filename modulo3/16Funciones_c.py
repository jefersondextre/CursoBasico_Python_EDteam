# Parametros por defecto
# Pasando parametros como lista
def mi_funcion(texto1,texto2,*otrosparametros):
    print(otrosparametros)
    print(texto1, texto2, sep='\n')
    
    

# mi_funcion('uno')
mi_funcion('este es el texto 1','Este es texto 2',1,2,3,4 )

def fibonacci(n):
    """Esta es una funcion que nos devuelve la
    serie de Fibonacci
        
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    a,b = 0,1
    while a < n:
        print(a, end=" ")
        a,b = b,a+b
    print()
    
# fibonacci(2000)
# fibonacci(1000)

# retornando variaos valores
def operaciones_matematicas(numero1,numero2):
    suma_resultado= numero1 + numero2
    resta_resultado= numero1 - numero2
    multiplicacion_resultado = numero1 * numero2
    division_resultado = numero1 / numero2
    return  suma_resultado, \
            resta_resultado, \
            multiplicacion_resultado,\
            division_resultado
            

# print(operaciones_matematicas(20,30))   Esto me retorna en una tupla
# aqui posteriormente retorno los valores y almaceno en variables independientes
suma, resta, multiplicacion,division = operaciones_matematicas(20,33)
print(suma)
print(resta)
print(multiplicacion)
print(division)