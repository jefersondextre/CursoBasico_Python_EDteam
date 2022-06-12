# Sistema de Ventas
class Usuario:

  def __init__(self, nombre, edad):
    self.__nombre = nombre
    self.__edad = edad

  def __registrar(self):
    print(f'El usuario {self.__nombre} ha sido registrado')

  #Metodo definido en python para mostrar un texto con los parametros enviados al instanciar la clase
  def __str__(self):
    return f'La usuario se llama {self.__nombre} y su edad es de {self.__edad} años'

  
  def consultar_tipo(self):
    self.__registrar()
    print('Sin especificar')

#-----------------------------------------------------
usuario = Usuario('Jeferson',35)

# De esta forma yo puedo acceder a los valores desde fuera de la clase, no hay restricciones.
# print(usuario.nombre)
# print(usuario.edad)

# Para darle mayor seguridad de acceso
# Añado dos guiones_bajo antes del atributo o metodo para darle restricciones de acceso desde
# fuera de la clase.

# usuario.registrar()
usuario.consultar_tipo()
