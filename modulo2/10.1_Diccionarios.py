# DICCIONARIOS 
usuario = {
  "nombre"  : "JEFERSON",
  "apellido": "Dextre",
  "edad"    : 37,
  "colores" : ["Red","Blue","Green"]
}

print(type(usuario))
print(usuario)
print(usuario["nombre"])
print(usuario["colores"])
print(len(usuario["colores"]))

jugador = dict(equipo="AlianzaLima",salario=30000,equipos=['1','2','3'])
print(jugador)
print(jugador["equipo"])