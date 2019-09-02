# -*- coding: utf-8 -*-
"""
Exportar dataframe

"""
import pandas as pd

l_clientes = [['Jorge', 33, 'Valladolid'],
              ['Luis', 25, 'Madrid'],
              ['Pilar', 44, 'Zaragoza'],
              ['Ana', 37, 'Cuenca']] 

df_clientes = pd.DataFrame(l_clientes, 
    columns=['nombre', 'edad', 'ciudad']) 

# exportacion a csv
df_clientes.to_csv("C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\export.csv", 
                   sep=';', index=False)
#exportación a Excel
df_clientes.to_excel("C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\expexcel.xlsx", index=False)

#exportacion a JSON
df_clientes.to_json("C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\expjson.json")