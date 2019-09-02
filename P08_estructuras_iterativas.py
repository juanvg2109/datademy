# -*- coding: utf-8 -*-
"""

Ejemplo de bucles 

"""

lista1 = [1,2,3,4,5,6,7,8]

acum = 0
for val in lista1:
    print(val)
    acum = acum + val
print(acum)
# Ejemplos de instruccionesbreak y continue
    
lista2 = [2,4,5,6,7,8,10]
for val in lista2:
    if val%2 > 0: #si no es par salta al siguiente
        continue
    print(val) 

for val in lista2:
    if val%2 > 0: #si no es par interrumpe el bucle
        break
    print(val) 
    
#EJER: recorrer la lista1 y quedarse solo co valores > 5

#función range

for i in range(1,20,2):  
    # el bucle imprime 1 3 5 7 9 
    print(i)
    
    
for i in range(0,-10,-1):  
    print(i)
    
    
lis1 = list(range(1,10,2))

    
# EJER: crear un rango de valores entre 100 y 200 que incremente de 5 en 5
    
# bucles anidados
    
listac = ["Madrid", "Murcia", "Valladolid"]
for ciudad in listac:
    print(ciudad)
    for c in ciudad:
        print(c)

#insertar y recorrer elementos de una lista con bucles    
lisran =[]
for val in range(5000, 7000, 1):
        lisran.append(val)

len(lisran)

for val in lisran:
    if val%5 == 0:
        print(val)
    
    
# bucles que recorren 2 valores. 
# La función enumerate genera un índice

for i, val in enumerate(listac): # La función enumerate genera un índice
    print(i,val)
    
# estructuras de tipo while
        
a = 1        
while a <= 10:
    print(a)
    a+=1
    
# Comparamos recorrer una lista o un generador
# 20000 elementos
from time import time #importamos la función time para capturar tiempos
    
lis1 = list(range(0,50000,1))

tiempo_inicial = time() 
for i in lis1: 
    i = i*2
    print(i)
 
tiempo_final = time() 
tiempo_ejecucion = tiempo_final - tiempo_inicial
print(tiempo_ejecucion)


tiempo_inicial = time() 
for i in range(0,50000,1):  
    i = i*2
    print(i)

tiempo_final = time() 
tiempo_ejecucion = tiempo_final - tiempo_inicial
print(tiempo_ejecucion)