# -*- coding: utf-8 -*-
"""
ejemplos lectura de fichero

"""

f = open("C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\f_ventas1.txt",'r') 
for line in f: 
    campos = line.split(";")
    print(line) 
f.close()

lis_f = []
f = open("C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\f_ventas1.txt",'r') 
for line in f: 
    lis_f.append(line.split(";"))
    print(line) 
f.close()

f = open('C:\\temp\\py\\f_ventas1.txt','r') 
for line in f: 
    campos = line.split(";")
    print(line) 
f.close()

with open('C:\\temp\\py\\f_ventas1.txt','r') as f: 
    for line in f: 
        print(line)
#No necesario cerrar fichero en este caso


