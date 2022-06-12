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

  # POLIMORFISMO
  def consultar_tipo(self):
    print('Sin especificar')

#-----------------------------------------------------
class Empleado:
  def __init__(self,area_trabajo):
    self.area_trabajo = area_trabajo
  
  def generar_reporte(self):
    print(f'Generando reporte del empleado del area de {self.area_trabajo}')
  # --------------------------------------------------
class Cliente(Usuario):
  def __init__(self, nombre,edad,numero_compras):
    # self.nombre = nombre
    # self.edad=edad
    # Usuario.__init__(self,nombre,edad)
    super().__init__(nombre,edad)
    self.numero_compras = numero_compras

  def ver_compras(self):
    print(f'El numero de compras del cliente {self.nombre} es {self.numero_compras}')
    
  def consultar_tipo(self):
    print('El tipo de Usuario es Cliente..')
    
  # --------------------------------------------------
class Vendedor(Usuario, Empleado):
  def __init__(self, nombre, edad,area_trabajo, numero_ventas):
    # super().__init__(nombre, edad)
    Usuario.__init__(self, nombre, edad)
    Empleado.__init__(self, area_trabajo)
    self.numero_ventas = numero_ventas

  def ver_ventas(self):
    print(f'El numero de ventas del vendedor {self.nombre} es {self.numero_ventas}')
  
  def consultar_tipo(self):
    print('El tipo de usuario es Vendedor : ')



usuario = Usuario('Jorge',24)
cliente = Cliente('Jeferson',35,12)
vendedor = Vendedor('Pablo',45,'Marketing',200)
# Asi podemos crear varias clases que vendrian a ser las subclases


# Aqui estamos creando un for y recorremos cada uno d elos objetos en una lista de objetos y las mostramos  
for objeto in (usuario, cliente, vendedor):
    objeto.consultar_tipo()
