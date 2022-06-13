# Funciones LAMBDA o ANONIMAS
# Funcion normal
def suma(num1,num2):
  return num1+num2

valor_sumado= suma(2,4)
print(valor_sumado)



# Funcion Lambda
valor_sumado=lambda num1,num2: num1 + num2
print(valor_sumado(3,5))