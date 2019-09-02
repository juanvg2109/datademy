# -*- coding: utf-8 -*-
"""
ejemplos calidad del dato con pandas
"""

import pandas as pd

l_clientes = [['Jorge', 33, 'Valladolid'],
              ['Luis', 25, 'Madrid'],
              ['Pilar', 44, 'Zaragoza'],
              ['Ana', 37, 'Cuenca']] 

df_clientes = pd.DataFrame(l_clientes, 
    columns=['nombre', 'edad', 'ciudad']) 

#pivotar

df_clientes2 = df_clientes.pivot_table(values='edad',  
                          index='nombre', 
                          columns='ciudad') 

# detectar nulos
df_clientes2['Madrid'].isnull()

df_clientes2['Madrid'].notnull()

df_clientes2['Madrid'].isna()

df_clientes2['Madrid'].isnull().sum() #contar nulos

df_clientes2['Madrid'].isnull().mean()     #porcentaje de nulos

df_clientes2[df_clientes2['Madrid'].isnull()] #filas con nulos 

df_clientes2[df_clientes2['Madrid'].notnull()] #filas sin nulos 


# Eliminar nulos

# elimina columnas en las que todos los valores son nulos
df_clientes3 = df_clientes2.dropna(axis=1, how='all') 
# elimina columnas en las que agún valor es nulo
df_clientes3 = df_clientes2.dropna(axis=1, how='any') 
# elimina filas en las que todos los valores son nulos
df_clientes3 = df_clientes2.dropna(axis=0, how='all') 
# elimina filass en las que agún valor es nulo
df_clientes3 = df_clientes2.dropna(axis=0, how='any') 

df_clientes2.dropna(inplace = True) 


# Sustituir nulos
# sustituir por un valor determinado
df_clientes3 = df_clientes2.fillna(0) 
df_clientes2['Madrid'] = df_clientes2['Madrid'].fillna(0) 
# reemplazar por el valor anterior(backfill) op por el siguiente (ffill)
df_clientes3 = df_clientes2.fillna(method='backfill') 
df_clientes3 = df_clientes2.fillna(method='ffill') 
# reemplazar por el valor medio de la columna
df_clientes3 = df_clientes2.fillna(df_clientes2.mean()) 
df_clientes2['Madrid'] = df_clientes2['Madrid'].fillna(df_clientes2['Madrid'].mean()) 


# Eliminar duplicados

l_clientes = [[1,'Jorge', 33, 'Valladolid'],
              [2,'Luis', 25, 'Madrid'],
              [3,'Pilar', 44, 'Zaragoza'],
              [4,'Ana', 37, 'Cuenca'],
              [2,'Luis', 25, 'Madrid'],
              [2,'Ramón', 29, 'Lugo']
              ] 

df_clientes = pd.DataFrame(l_clientes, 
    columns=['id','nombre', 'edad', 'ciudad']) 


res = df_clientes.duplicated()  #busca duplicados por todos los campos
df_clientes.duplicated(subset='id')  #busca duplicados por un campo determinado

#selecconar duplicados
dups = df_clientes[df_clientes.duplicated()]
#eliminar duplicados por todas las columnas
df_clientes2 = df_clientes.drop_duplicates()

#eliminar duplicados por un campo determinado
dups = df_clientes[df_clientes.duplicated(subset='id')]
df_clientes2 = df_clientes.drop_duplicates(subset='id', keep='first')








