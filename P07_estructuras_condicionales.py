# -*- coding: utf-8 -*-
"""
Ejemplos estructuras condicionales

@author: Equipo
"""

edad = 15

# if con 2 ramas
if edad < 18:
    print("menor de edad")
else:
    print("mayor de edad")





# if con varias ranas
if edad < 13: 
    print( "niño" ) 
elif edad < 18: 
    print( "adolescente" )
elif edad < 35: 
    print( "joven" ) 
elif edad < 55: 
    print( "mediana edad" ) 
elif edad < 75:
    print( "mayor" )
else: print("anciano")


#EJER crear los siguientes rangos sobre la variable importe
# 1 (0 - <=1000)  2(>1000 - <= 2000)   3 (>2000)


imp = 1500

# if con 2 ramas
if imp <= 1000:
    print("1")
    rango = "1"
elif imp > 1000 and imp <= 2000:
    print("2")
    rango = "2"
else:
    print("3")
    rango = "3"






