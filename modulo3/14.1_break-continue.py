'''
CONTINUE  => PERMITE SALTAR A LA SIGUIENTE POSICION CONTINUANDO LA ITERACION.
BREAK     => SE ROMPE EL CICLO DE ITERACION.
ELSE      => EJECUTA UNA PORCION DE CODIGO CUANDO TERMINA EL CICLO
'''
# frameworks = ["Flask","Django","FastApi","Pyramid"]
# continue
# for f in frameworks:
#     if f == "Flask":
#       print("Es Flask")    
        # continue
#     print(f)  


# break
# for f in frameworks:
#     if f == "Flask":
#       print("Es Flask")    
#       break
#     print(f)  
  
# else  
# for f in frameworks:
#     if f == "Flask":
#       print("Es Flask")    
#       # continue
#     print(f)  
# else:
#     print("El ciclo termino")    
    

# While : Aunuqe el continue estaba dentro de la condicional 
# afecto a todo el codigo que estaba 
# por fuera de la condicional
numero = 1 
while numero < 10 :
    if numero == 5:
        print("Es 5")    
        # continue
    print(numero)
    numero +=1
else:
    print("El ciclo termino")   