# Codigos para abrir archivos : r con permisos de lectura
archivo = open('archivo.txt', 'r')
# Lee varias lineas de el archivo.txt
# print(archivo.read())
# Lee solo la primera linea del archivo
# print(archivo.readline())

# Recorriendo todas las lineas de un archivo
for linea in archivo:
  print(linea,end='')

archivo.close()