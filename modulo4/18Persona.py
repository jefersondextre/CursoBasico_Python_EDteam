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


# HERENCIA : Tomar metodos y atributos de una superclase y que tambien pueda ser usados por otras clases
persona = Usuario('Jeferson', 35)
persona.registrar()

class Cliente(Usuario):
  # pass se usa cuando no vamos a hacer nada o ejecutar algo
  pass

# Instanciamos Cliente y usamos sus metodos heredados de Usuario

cliente = Cliente('Antonio',60)
cliente.registrar()

class Vendedor(Usuario):
  pass

vendedor=Vendedor('Pepe',46)
vendedor.registrar()

# Asi podemos crear varias clases que vendrian a ser las subclases
