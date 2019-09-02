# -*- coding: utf-8 -*-
"""

Ejemlos diccionario

"""

dic1 = {'id_ciudad':125, 'ciudad':"Madrid", 'poblacion':3.21}

print(dic1['ciudad']) 

print(dic1['id_ciudad']) 

#Eliminar una clave del diccionario

dic1.pop('poblacion')

#agregar elemento

dic1['extension'] = 600


# Obtener claves y valores

dic1.keys()

dic1.values()

# lista de diccionarios
lis_dic1 = [{'id_ciudad':125, 'ciudad':"Madrid", 'poblacion':3.21},
            {'id_ciudad':126, 'ciudad':"Valencia", 'poblacion':1.12},
            {'id_ciudad':127, 'ciudad':"Murcia", 'poblacion':0.56},
            {'id_ciudad':128, 'ciudad':"Toledo", 'extension':100}
            ]

lis_dic1[2]['ciudad']

# EJER: Acceder a el nombre de la ciudad del segundo elemento de la lista




dic1 = {'id_cliente':125, 'nombre':"Pepe", 'canal':['Tienda física', 'web']}

dic1['canal'][0]

# recorrer un dic con un for
for clave in dic1.keys():
	print(clave)
	print(dic1[clave])








