name="Jeferson"
number1=2
frutas = ["manzana","peraa","uva","melocoton"]
print(frutas)
print(type(frutas))
numeros = [1,2,3,4,50]
print(numeros)
varios = [True,"Manzana",20,33.33,-300]
print(varios)

# print(frutas[0])
# print(frutas[1])
# print(frutas[2])
print(frutas[-1])
print(frutas[-3])

# frutas2 = frutas[1:3]
frutas2 = frutas[:]
print(frutas2)
print(frutas + numeros)
new_list= frutas + numeros
print(new_list)
frutas[1]= "pera"
frutas[-2]= "piña"
frutas[1:4]=["uno","dos","tres","cuatro"]
numeros = frutas[1:4]
print(frutas)
print(numeros)
numeros.append(4)
print(numeros)
numeros.append(4*5)
print(numeros)
print(len(frutas))

new_list = [frutas, numeros]
print(new_list)
