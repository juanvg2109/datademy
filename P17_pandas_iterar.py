# -*- coding: utf-8 -*-
"""
Ejemplos iterar dataframes

"""

import pandas as pd
# Lectura desde fichero Excel
df_ventas = pd.read_excel("C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\f_ventas1.xlsx")

df_ventas.head(3)

# Iterar con iterrows. Obtener siguiente elemento

next(df_ventas.iterrows())


# recorrer el dataframe
for index, row in df_ventas.iterrows():
     print(index, row)
     
     
for index, row in df_ventas.head(3).iterrows():
     print(index, row)
     
for index, row in df_ventas.head(3).iterrows():
     print(row['producto'])


