# -*- coding: utf-8 -*-
"""
Ejemplos matplotlib
"""
import pandas as pd
import matplotlib.pyplot as plt
# Lectura desde fichero Excel
df_ventas = pd.read_excel("C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\f_ventas1.xlsx")

plt.bar(x=df_ventas['oficina'], height=df_ventas['unidades'])

plt.pie(df_ventas['unidades'], labels=df_ventas['oficina'])

plt.show()

plt.boxplot(x=df_ventas['unidades'])  # diagrama boxplot



