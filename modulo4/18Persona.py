# Sistema de Ventas
class Usuario:
  # Metodo inicializador , self es un metodo que se python asigna refiriendose a la clase actual.
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def registrar(self):
    print(f'El usuario {self.nombre} ha sido registrado')

  #Metodo definido en python para mostrar un texto con los parametros enviados al instanciar la clase
  def __str__(self):
    return f'La usuario se llama {self.nombre} y su edad es de {self.edad} años'


# INSTANCIACION DE OBJETOS
persona = Usuario('Jeferson', 35)

persona.registrar()
