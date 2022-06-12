# Sistema de Ventas
class Usuario:

  def __init__(self):
    self.__nombre = 'Ana'
    self.__edad = 23

  # GETTERS 
  def getNombre(self):
    return self.__nombre

  def getEdad(self):
    return self.__edad

  # SETTERS
  def setNombre(self,nombre):
    if nombre == 'Ana':
      self.__nombre=nombre
    else:
      return 'No puede asignar ese nombre' 

  def setEdad(self,edad):
    if edad == 23:
      self.__edad=edad
    else:
      return 'No puede asignar esa edad' 

  def __registrar(self):
    print(f'El usuario {self.__nombre} ha sido registrado')

  #Metodo definido en python para mostrar un texto con los parametros enviados al instanciar la clase
  def __str__(self):
    return f'La usuario se llama {self.__nombre} y su edad es de {self.__edad} años'

  
  def consultar_tipo(self):
    self.__registrar()
    print('Sin especificar')

#-----------------------------------------------------
# usuario = Usuario('Jeferson',35)

# De esta forma yo puedo acceder a los valores desde fuera de la clase, no hay restricciones.
# print(usuario.nombre)
# print(usuario.edad)

# Para darle mayor seguridad de acceso
# Añado dos guiones_bajo antes del atributo o metodo para darle restricciones de acceso desde
# fuera de la clase.

# usuario.registrar()
# usuario.consultar_tipo()

usuario=Usuario()
# Accedo usando los getter y setter para enviar y acceder atributos privados
print(usuario.getNombre())
print(usuario.getEdad())

# setter con validacion
print(usuario.setNombre('Luis'))
print(usuario.setEdad(56))

# settear con datos correctos
print(usuario.setNombre('Ana'))
print(usuario.setEdad(23))


