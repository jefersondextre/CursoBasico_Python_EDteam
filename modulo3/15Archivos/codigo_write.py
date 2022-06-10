# Codigos para escribir archivos : r con permisos de lectura, w permisos de escritura,a permisos de escritura sin borrar lo anterior.
archivo = open('archivo.txt', 'a')  
# Lee varias lineas de el archivo.txt
# print(archivo.read())
# Lee solo la primera linea del archivo
# print(archivo.readline())

# Recorriendo todas las lineas de un archivo
archivo.write('\nNueva linea')
archivo.write('\nNueva linea 2')

archivo.close()