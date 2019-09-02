# -*- coding: utf-8 -*-
"""
Ejemplo de funciones
"""

def comparar_cadenas(cad1, cad2):
    """se comparar 2 cadenas de texto pasadas
       como argumento. Devuelve True o False según
       sean iguales o distintas"""
    if cad1.upper().strip() == cad2.upper().strip():
        print("Cadenas iguales")
        return True
    else:
        print("Cadenas distintas")
        return False
    

c1 = "Madrid "
c2 = " MADRID"
res = comparar_cadenas(c1,c2)

c1 = "Madrid"
c2 = "Murcia"
res = comparar_cadenas(c1,c2)

# orden en la llamada
res = comparar_cadenas(cad2=c2, cad1=c1)


#EJER: crear una función que reciba 2 valores enteros y devuelva el mayor

# funciones lambda

lis1 = [1,2,3,4]
lis2 = list(map(lambda x:x+5, lis1))
lis3 = list(map(lambda x:x*2, lis1))

lis1 = [0, 2, 5, 8, 10, 23, 31, 40]
lis2 = list(filter(lambda x: x % 2 == 0, lis1))

# aplicar un map para restar 2 listas
lis1 = [3,5,8,10]
lis2 = [1,6,7,9]
lis3 = list(map(lambda x, y: x-y, lis1, lis2))

# aplicar un reduce para sumar todos los elementos
from functools import reduce
res = reduce((lambda x, y: x + y), lis1)


