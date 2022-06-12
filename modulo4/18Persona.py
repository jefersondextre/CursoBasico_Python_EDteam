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


class Cliente(Usuario):
  def __init__(self, nombre,edad,numero_compras):
    # self.nombre = nombre
    # self.edad=edad
    # Usuario.__init__(self,nombre,edad)
    super().__init__(nombre,edad)
    self.numero_compras = numero_compras

  def ver_compras(self):
    print(f'El numero de compras del cliente {self.nombre} es {self.numero_compras}')
    
cliente = Cliente('Jose',30,100)
cliente.ver_compras()


class Vendedor(Usuario):
  def __init__(self, nombre, edad, numero_ventas):
    super().__init__(nombre, edad)
    self.numero_ventas = numero_ventas

  def ver_ventas(self):
    print(f'El numero de ventas del vendedor {self.nombre} es {self.numero_ventas}')

vendedor=Vendedor('Pepe',46,250)
vendedor.ver_ventas()

# Asi podemos crear varias clases que vendrian a ser las subclases
