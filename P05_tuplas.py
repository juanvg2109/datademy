# -*- coding: utf-8 -*-
"""
ejemplos de tuplas

@author: Equipo
"""
# definición de tupla
tup1 = (1, "Madrid", 4.67, True)

numelem = len(tup1)

a = tup1[2]

# No se pueden hacer asignaciones en tuplas

tup1[3] = 8

#Una tupla se puede “dividir” en varias variables

a,b,c,d = tup1
