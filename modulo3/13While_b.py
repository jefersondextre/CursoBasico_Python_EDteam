contador = 0

while True:
    contador = contador + 5
    if contador == 1000:
        break
    elif contador == 990:
        print('Este numero no se muestra')
        continue
    else:
        print(contador)
print('El ciclo finalizó!.')
