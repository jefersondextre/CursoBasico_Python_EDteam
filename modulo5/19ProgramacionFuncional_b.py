

# ! Funcion normal
# ! ===============
def duplicar(num):
  num=num *2
  return num

duplicado= duplicar(2)
print(duplicado)

#! FUNCION lambda
#! ==============
duplicado2=lambda num: num*2
print(duplicado2(3))



#! FUNCION NORMAL
#! ===============

def suma(num1,num2):
  return num1+num2

valor_sumado= suma(2,4)
print(valor_sumado)



#! FUNCION LAMBDA
#! ===============

valor_sumado=lambda num1,num2: num1 + num2
print(valor_sumado(3,5))