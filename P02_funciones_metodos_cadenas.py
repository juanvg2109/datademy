# -*- coding: utf-8 -*-
"""
Ejemplo de funciones y métodos
sobre cadenas de caracteres
"""


ciudad = "Madrid"
pais = "España"

cad = """Ejemplo de cadena de varias
        lineas"""

a = len(ciudad)         #longitud de la cadena
c = ciudad + pais      #concatenar cadenas

c1 = ciudad[0]            #posición 1 (empieza en 0)
c2 = ciudad[0:3]         #desde la posición 0 a la 3 sin contar la 3
ciudad[0] = "P"      # da error al ser las cadenas inmutables
ciudad = "Padrid"

res1=ciudad.lower() #pasa a minusculas
res2=ciudad.upper() #pasa a masyusculas

nombre_curso = "  Introducción a Phyton   "
nombre_curso = nombre_curso.strip()  #elimina blancos extremos

lista_cursos1 = "Java, Phyton, R, SQL"

lista_cursos2 = lista_cursos1.split(",") #divide en subcadenas

cur1, cur2, cur3, cur4 = lista_cursos1.split(",")

lista_cursos3 = cur1 + "," + cur2 +  "," + cur3 + "," + cur4

# concatenar métodos
lista_cursos2 = lista_cursos1.upper().split(",")

pos = lista_cursos1.find("SQL") #busca una subcadena
pos = lista_cursos1.find("SOL") #busca una subcadena

#reemplaza una subcadena por otra
lista_cursos3 = lista_cursos1.replace("SQL", "HTML")

#Uso de formar


plantilla_curso = 'El curso: {curso}, tiene una duración de: {duracion}'

curso = "SQL"
duracion = 30

cad_curso = plantilla_curso.format(curso=curso, duracion=duracion)



























