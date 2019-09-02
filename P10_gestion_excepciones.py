# -*- coding: utf-8 -*-
"""
EJEMPLOS gestión de errores
"""
cadena = "hola"

try: 
    a = cadena[10] 
except  IndexError: #error q se produce
    print("Error en la asignación de a") 
finally: 
    print("Fin del bloque")



a = 10
b = 0

try: 
    c = a/b
except  ZeroDivisionError: #error q se produce
    print("Error en la asignación de c") 
finally: 
    print("Fin del bloque")