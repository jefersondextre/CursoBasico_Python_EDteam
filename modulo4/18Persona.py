# Sistema de Ventas
class Usuario:

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def registrar(self):
    print(f'El usuario {self.nombre} ha sido registrado')

  #Metodo definido en python para mostrar un texto con los parametros enviados al instanciar la clase
  def __str__(self):
    return f'La usuario se llama {self.nombre} y su edad es de {self.edad} años'

  
  def consultar_tipo(self):
    print('Sin especificar')

#-----------------------------------------------------
usuario = Usuario('Jeferson',35)

# De esta forma yo puedo acceder a los valores desde fuera de la clase, no hay restricciones.
print(usuario.nombre)
print(usuario.edad)
