
#! Funcion Normal
#! =================
numeros = [1,2,3,4,5]

def duplicar(lista):
  numeros_duplicados=[]
  for num in numeros:
    numeros_duplicados.append(num*2)  
  return numeros_duplicados 
  
duplicados=duplicar (numeros)  
print(duplicados)



#! Funcion MAP
#! =============== 
numeros=[1,3,5,7,9]

# def duplicar(numero):
  # return numero * 2


# map(funcion,lista)
duplicados2 = list(map(lambda numero: numero*2, numeros))
print(duplicados2)