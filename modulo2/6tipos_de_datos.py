# Cadenas de caracteres -> class str
# ------------------------
mensaje = 'Esto es un texto de prueba'
print(type(mensaje))

letra = 'a'
print(type(letra))

numero_5 = '5'
print(type(numero_5))
# Numericos
# - Enteros -> class int
# ------------------------
numero = 5
print(type(numero))
numero = -5
print(type(numero))

# - Flotantes -> class Float
# ------------------------
n_decimal = 2.45
print(type(n_decimal))

suma_decimal = 2.1 + 3.2
print(type(suma_decimal))
calculo = 1/5
print(type(calculo))

# - Complejos -> class complex
# ------------------------
complejo = 1+2j
print(type(complejo))
print(type(complejo.real))
print(type(complejo.imag))

# - Booleanos -> class bool
# ------------------------
curso_aprobado = True
nivel_dificil = False
print(type(curso_aprobado), type(nivel_dificil))

suma = 4+5 == 10
print(suma)
print(type(suma))

resta = 4-10 == 6
print(resta)

operador= 2.3-0.3
print(operador)
# ------------------------ 