# -*- coding: utf-8 -*-
"""

Conexión a MySQL desde Phyton

"""


# Conexion a mysql
# antes hacer el PIP o bien:    conda install -c anaconda mysql-connector-python 

import pandas as pd

import mysql.connector

connmysql = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  use_pure = True
)

print(connmysql)

cursordb = connmysql.cursor()

sql = "select cod_tarifa, cod_cliente, hc_consumo FROM dwh_consumo.hc_consumo"
cursordb.execute(sql)

res = cursordb.fetchall() #lista de tuplas

df = pd.DataFrame(res)

#use_pure = True  para forzar a usar la implementación de Phyton y no la de C 

""" Otra opción usando otra librería: pymysql
"""

import pymysql.cursors
import pandas as pd

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='dwh_consumo',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print(connection)

with connection.cursor() as cursor:
        sql = "select cod_tarifa, cod_cliente, hc_consumo FROM dwh_consumo.hc_consumo"
        cursor.execute(sql)
        res = cursor.fetchall()
        print(res)
        
df = pd.DataFrame(res)