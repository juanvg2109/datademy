# -*- coding: utf-8 -*-
"""

Practicas fichero AXA HK

"""
import pandas as pd
import datetime as dt
import numpy as np


"""Ejemplo trabajo con fechas"""

fec_hoy = dt.datetime.now()

# Prueba lectura fechas
# Lectura desde fichero csv
df_f = pd.read_csv("C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\f_ventas_fec.txt",
                 sep=';', header='infer')

# Conversion de tipos
df_f.dtypes
df_f['f_venta2'] = pd.to_datetime(df_f['f_venta'])
df_f.dtypes
df_f['fh_venta2'] = pd.to_datetime(df_f['fh_venta'])



#especificar parseo de fechas en lectura
# con la clausula dtype en lectura tambien se puede especificar tipo
df_f = pd.read_csv("C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\f_ventas_fec.txt",
                 sep=';', header='infer', parse_dates=['f_venta', 'fh_venta'])

#diferencia en dias
df_f['dif'] = df_f['f_venta']  - fec_hoy #objeto intervalo
df_f['dif_dias']= df_f['dif']/np.timedelta64(1,'D')

#diferencia en meses 
df_f['dif_meses']=df_f['dif']/np.timedelta64(1,'M')











