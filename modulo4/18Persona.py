class Persona:
  # Metodo inicializador , self es un metodo que se python asigna refiriendose a la clase actual.
  def __init__(self,nombre,edad):
    self.nombre = nombre
    self.edad=edad
  
  # Metodos que muestran informacion
  def caminar(self):
    print(f'{self.nombre} esta caminando')

  def correr(self):
    print(f'{self.nombre} esta corriendo')
    
  #Metodo definido en python para mostrar un texto con los parametros enviados al instanciar la clase
  def __str__(self):
    return f'La persona se llama {self.nombre} y su edad es de {self.edad} años'




# INSTANCIACION DE OBJETOS
persona = Persona('Jeferson',35)
print(persona)
# persona.caminar()
# persona.correr()
# print(persona.nombre)
# print(persona.edad)
persona.caminar()

persona2 = Persona('Dany',28)
persona2.correr()
persona3=Persona('Pedro',25)
persona3.caminar()