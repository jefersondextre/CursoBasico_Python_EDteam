def mostrar_mensaje(mensaje):
  return f'Su mensaje es {mensaje}'

mensaje_mostrado = mostrar_mensaje('Hola')
print(mensaje_mostrado)



#! Funcion Lambda
mensaje_mostrado = lambda mensaje: f'Su mensaje es {mensaje}'
print(mensaje_mostrado('Bienvenido'))



# ! Funcion normal
def numero_par(num):
  return num % 2 == 0

es_par= numero_par(3)
print(es_par)

# ! funcion lambda
espar= lambda num2 : num2 %2 ==0

print(espar(10))