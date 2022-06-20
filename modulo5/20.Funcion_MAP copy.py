
#! Funcion Normal
#! =================
# numeros = [1,2,3,4,5]

# def duplicar(lista):
#   numeros_duplicados=[]
#   for num in numeros:
#     numeros_duplicados.append(num*2)  
#   return numeros_duplicados 
  
# duplicados=duplicar (numeros)  
# print(duplicados)



#! Funcion MAP
#! =============== 
lista1 =[1,3,5,7,9]
lista2 =[1,1,1,1,1,1,1]

# map(funcion,lista)
suma = list(map(lambda lista1,lista2: lista1+lista2, lista1,lista2))
print(suma)