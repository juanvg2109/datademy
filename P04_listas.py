# -*- coding: utf-8 -*-
"""
Ejemplos listas

"""
#lista con elementos de diferente tipo

lista1 = [1, "Madrid", 4.67, True]

a,b,c,d = lista1

numelem = len(lista1)

elem1 = lista1[0] # primer elemento

lista2 = lista1[0:2]  # desde el 0, 2 elementos

a, b = lista1[0:2]

elem2 = lista1[-1]   # ultimo elemento

lista1[0] = "5"  # puedo hacer asignaciones, son mutables. Esto no lo podía hacer en las cadenas

# insertar elementos: 

# inserta 8 en posición 2
lista1[2:1] = [8]   

#inserta 10, 11 a partir de la posición 3

lista1[3:2] = [10,'hola'] 

# borrar elementos desde pos inicial a pos final

lista1[1:2] = [] 

# eliminar ultimo elemenro de la lista


lista1.pop()

# eliminar por indice

lista1.pop(3)

# añadir elementos al final de la lista

lista1.append("ZZ")

#añade los elementos de la sublista en la lista principal

lista1.extend(["n1", "n2", "n3"])

# Inserta el valor 100 en la posición 5

lista1.insert(5,100)

# Elimina el valor 100

lista1.remove(100)

#Devuelve la posición del valor x en la lista

pos = lista1.index("Madrid")

# Ordenar la lista

lista2 = ['p','m', 'a','y', 'j', 'f','e', 'v','r','b']

lista2.sort()

# ejemplo paso por referencia

lis1 = [1,2,3,4,5]

lis2 = lis1

lis1[2] = 10

sum(lis1)

# ejemplo paso por valor

lis1 = [1,2,3,4,5]

lis2 = lis1.copy()

lis1[2] = 10

# comprobacion de que el objeto cambia
# en asignaciones a enteros respecto a listas
# id es el identificador de objeto

a = 4
id(a)
a = 5
id(a)
lis = [1,0,2,3]
id(lis)
lis[1] = 30
id(lis)


# listas de listas
lis1 = [['a1', 'b1', 'c1'],['a2','b2','c2'],['a3','b3','c3']]

a = lis1[0][0]

lis1[0][0:2]

lis1[:][1]

lis1[-1][-1]

lis1[1][1]


# EJER: obtener los 2 primeros elementos 
# del ultimo elemento de la lista principal   ['a3','b3']

lis1[-1][0:2]

# List comprehension

# lista de 5 millones elementos
nums = list(range(1,5000000,1))
nums2 = []
for i in nums:
    nums2.append(i**2)
    
#Los mismo con list comprehension:
nums2 = [i**2 for i in nums]

from time import time
# también se puede hacer con librería timeit

start_time = time()
nums2 = []
for i in nums:
    nums2.append(i**2)
elapsed_time = time() - start_time
print("Tiempo ejecución: %.10f seconds." % elapsed_time)


start_time = time()
nums2 = []
#Los mismo con list comprehension:
nums2 = [i**2 for i in nums]
elapsed_time = time() - start_time
print("Tiempo ejecución: %.10f seconds." % elapsed_time)




