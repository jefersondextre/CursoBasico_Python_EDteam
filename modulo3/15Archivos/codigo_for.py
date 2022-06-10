# parametros del metodo open para escribir archivos : r con permisos de lectura, w permisos de escritura,a permisos de escritura sin borrar lo anterior.
# Recorriendo lineas con for 
archivo = open('archivo.txt', 'w')  
for linea in range(1,11):
    archivo.write('\nTexto: '+str(linea))

# Recorriendo todas las lineas de un archivo
archivo.write('\nNueva linea')
archivo.write('\nNueva linea 2')

archivo.close()