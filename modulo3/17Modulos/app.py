import paquete.mi_modulo
import os,sys,time
''' Modulos predefinidos 
os  Permite acceder  a funciones del Sistema operativo
sys permite acceder a funciones del interprete de python
time me permit manipular fechas y horas
'''
from time import asctime
print(asctime())

from paquete.mi_modulo import mensaje
print(mensaje())
# print(mi_modulo)
# print(time.asctime())


print(paquete.mi_modulo)
print(paquete.mi_modulo.mensaje())
# print(time.asctime())
