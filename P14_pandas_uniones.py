# -*- coding: utf-8 -*-
"""
Uniones de tablas

"""


import pandas as pd

ruta="C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\"
fichA = "f_ventas_A.xlsx"
fichB= "f_ventas_B.xlsx"
fichC= "f_ventas_C.xlsx"
fichP = "precios.xlsx"

df_ventasA = pd.read_excel(ruta+fichA)

df_ventasB = pd.read_excel(ruta+fichB)

df_ventasC = pd.read_excel(ruta+fichC)

df_precios = pd.read_excel(ruta+fichP)

# unir 2 dataframes
df_ventas_t = pd.concat([df_ventasA, df_ventasB])

df_ventas_t = df_ventasA.append(df_ventasB)


df_ventas_t = df_ventas_t.reset_index() #rehacemos el índice

# unir 2 dataframes
df_ventas_t = pd.concat([df_ventasA, df_ventasC], sort=False)

# unir por columnas

df_ventas_u = pd.merge(left=df_ventas_t, right=df_precios,
                      how='left', left_on='producto', right_on='producto')

df_ventas_u[df_ventas_u['precio'].isnull()]
