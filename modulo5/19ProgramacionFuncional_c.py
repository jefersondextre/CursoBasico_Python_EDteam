def mostrar_mensaje(mensaje):
  return f'Su mensaje es {mensaje}'

mensaje_mostrado = mostrar_mensaje('Hola')
print(mensaje_mostrado)



#! Funcion Lambda
mensaje_mostrado =lambda mensaje: f'Su mensaje es {mensaje}'
print(mensaje_mostrado('Bienvenido'))
