# SETS  o CONJUNTOS Es un TIPO de coleccion desordenada ya que sus elementos no se muestras en el
#  orden en que los ingresamos

conjunto = set()
print(type(conjunto))

conjunto = {1, 2, 3}
print(conjunto)
conjunto.add('p')
conjunto.add('a')
conjunto.add('elemento nuevo')
print(conjunto)

# comprobando si existe un elemento en el conjunto
existe = 'p' in conjunto
print(existe)

# No se puede añadir un elemento repetido a un conjunto
lista_convertida = list(conjunto)
lista_convertida.append(2)

conjunto.add(2)

print(lista_convertida)
print(conjunto)

# Muestra cada caracter del texto como un elemento de mi conjunto
texto = 'Se convertira a conjunto'
print(set(texto))

# Eliminar elementos de un conjunto
conjunto.discard(1)
print(conjunto)

# Vaciar todo el conjunto completo
conjunto.clear()
print(conjunto)
