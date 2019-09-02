# -*- coding: utf-8 -*-
"""
Ejemplos pandas

"""

# Creación de un dataframe partiendo de un diccionario

import pandas as pd

clientes = {'nombre': ['Jorge', 'Luis', 'Pilar', 'Ana'],
            'edad': [33, 25, 44, 37],
            'ciudad': ['Valladolid', 'Madrid', 'Madrid', 'Cuenca']   
            }

df_clientes = pd.DataFrame(clientes)

df_clientes.shape
df_clientes.dtypes

# especificando nombres de las columnas
df_clientes = pd.DataFrame(clientes, columns = ['ciudad', 'nombre', 'edad'])


# Crear un dataframe partiendo de una lista y especificando
# el nombre de las columnas

l_clientes = [['Jorge', 33, 'Valladolid'],
              ['Luis', 25, 'Madrid'],
              ['Pilar', 44, 'Zaragoza'],
              ['Ana', 37, 'Cuenca']] 

df_clientes = pd.DataFrame(l_clientes, 
    columns=['nombre', 'edad', 'ciudad']) 

"""EJER crear un dataframe con las siguientes características
columnas: curso, duracion
valores:
        'SQL', 20
        'Phyton', 25
        'Marketing Digilal', 15
        """

# serie de Pandas
        
serie1 = pd.Series(index=['Ene', 'Feb', 'Mar', 'Abril', 'Mayo', 'Junio'] , 
                   data =[23,41,28,32,27,33])

#crear el df partiendo de un dic que tiene series
# cuando son series no obliga a que tengan todos la misma longitud

customer = {'edad' : pd.Series(index=['c1', 'c2', 'c3'] , data =[23,41,28]),
               'consumo' : pd.Series(index=['c1', 'c2'] , data =[100,141])}

df_cus = pd.DataFrame(customer) 

# Lectura desde fichero csv
df_ventas = pd.read_csv("C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\f_ventas1.txt",
                 sep=';', header='infer')

# Se pueden indicar los Valores que quiero que sean nulos en 
# una lectura: na_values
data = pd.read_csv("C:\\temp\\pandas\\small.csv",
                   na_values = ["?", "none"], sep = ",")


df_ventas.shape
df_ventas.count()
df_ventas.dtypes


ruta = "C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\"
nomfich = "f_ventas1.txt"

df_ventas = pd.read_csv(ruta+nomfich,
                 sep=';', header='infer')

# Lectura desde fichero Excel
df_ventas = pd.read_excel("C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\f_ventas1.xlsx")

#dimensión, columnas y tipos
df_ventas.shape
df_ventas.columns
df_ventas.dtypes

# acceder a una columna:
print(df_clientes['nombre'])
print(df_clientes.nombre)

df_clientes['ciudad'] = "Lugo"
df_clientes['ciudad'] = ["Lugo","Murcia","León","Soria"]

df_clientes['ingresos'] = [40,30,35,28]
df_clientes['costes'] = [10,8,11,9]
df_clientes['margen'] = df_clientes['ingresos'] - df_clientes['costes']

df_clientes['año'] = 2019
#eliminar columna
del df_clientes['año']
df_clientes.drop(['año'], axis=1)


# eliminar filas
df_clientes.drop([1, 2],axis=0)

#conversion de tipos

df_clientes['edad_s']=df_clientes['edad'].astype(str)
df_clientes.dtypes # comprobamos los tipos

#Función apply para aplicar transformaciones
# bajo < 10, medio (10-25), alto ( > 25)
def rangos(val):
    if val <= 10:
        rango='bajo'
    elif val > 10 and val <= 25:
        rango = 'medio'
    else:
        rango='alto'
    return(rango)

df_clientes['rango_margen']=df_clientes['margen'].apply(rangos)

# lo mismo, pero con función lambda
f = lambda x : 'alto' if x >= 25 else 'bajo'

df_clientes['rango_margen']=df_clientes['margen'].apply(f)
df_clientes['rango_margen3']=df_clientes['margen'].apply(lambda x : 'alto' if x >= 25 else 'bajo' )

#tratar todas las columnas en un bucle:

for col in df_clientes.columns:
    print(col)
    if col == 'ciudad':
        df_clientes[col] = df_clientes[col] + " ESP"

"""El método loc permite acceder por nombre columna y el método iloc 
accede por el índice y posición."""

#Ojo el paso es por referencia
df_clientes3 = df_clientes
df_clientes['nombre'] = ['Jorge P.', 'Luis', 'Pilar', 'Ana']
df_clientes3 = df_clientes.copy()

# fila 0 columna nombre. 
df_clientes2 = df_clientes.loc[0,'nombre']


# filas 0 a 2 columnas nombre y ciudad
df_clientes2 = df_clientes.loc[0:2,['nombre', 'ciudad']]

df_clientes2 = df_clientes.loc[[1,3],['nombre', 'ciudad']]
# todas las filas columnas nombre y ciudad
df_clientes2 = df_clientes.loc[:,['nombre', 'ciudad']]

# fila 0 columna 0 nombre
df_clientes2 = df_clientes.iloc[0,0]
# filas 0 a 2 columnas 0 y 1 nombre y ciudad
df_clientes2 = df_clientes.iloc[0:2,[0,1]]
# todas las filas  0 y 1 nombre y ciudad
df_clientes2 = df_clientes.iloc[:,0:2]

# filtrar columnas de un tipo (string)
df_clientes2 = df_clientes.loc[: ,  df_clientes.dtypes == object]



df_clientes.head(2) # dos primeras filas
df_clientes.tail(2) # dos ultimas filas
#obtener solo algunos campos
df_clientes.head(2)['nombre']
df_clientes.head(2)[['nombre','edad']]

#df_clientes.take([0, 3])  # filas 0 y 3
df_clientes.sample(2) # muestra de 2 filas

df_clientes.shape # tamaño del df en filas y cols

# filtrado por condición
df = df_clientes[df_clientes.nombre=="Ana"]
df_clientes[df_clientes.margen >=20].sample(1)
df_clientes[df_clientes.ingresos.isin([10,30,40])]
df_clientes[df_clientes.ciudad=="Madrid"][['nombre','edad']]

# Ordenar tabla

df_clientes.sort_values(by = 'nombre') # ordenar por nombre
df = df_clientes.sort_values(by = 'margen', ascending = False) # descendente
df_clientes.sort_values(by = 'nombre')[['nombre','ciudad']]

df_clientes.sort_index() # ordenar por indice

# Obtener un ranking:
df_clientes["rank"] = df_clientes["margen"].rank(ascending=False) 

#Renombrado de columnas:
df_clientes2 = df_clientes.rename(columns={"rank": "ranking"})

#Crear rangos:
bins = [0, 5, 10, 15, 20]
df_ventas['rangos_unid'] = pd.cut(df_ventas['unidades'], bins,
         labels=False)



# método filter seleccionar columnas
df_clientes.filter(["nombre", "ciudad"]) 

# métoodo query

df_clientes.query('ciudad == "Lugo ESP" & margen > 20')

# filtro por índice
df_clientes[df_clientes.index==1]

# Reindexar:
df_clientes2 = df_clientes.set_index(df_clientes['nombre'])

# al indexar por nombre ahora puedo utilizarlo en las busquedas
#por fila en método loc
df_clientes4 = df_clientes2.loc[['Jorge', 'Luis'],['nombre', 'ciudad']]



# trasponer
df_clientes2 = df_clientes.T

#pivotar

df_clientes2 = df_clientes.pivot_table(values='edad',  
                          index='nombre', 
                          columns='ciudad') 

#Estadísticos:
df_clientes.describe()
df_clientes['edad'].describe()
df_clientes['edad'].mean()
df_clientes['ingresos'].cumsum()
df_clientes['ingresos'].sum()
df_clientes['ciudad'].count()
df_clientes.count()
df_clientes['ciudad'].hist()

# estadísticas incluyendo strings
df_clientes.describe(include = "object")


#agregados
# sumatorio y valor medio por oficina
df_ventas.groupby(['oficina']).sum()
df_ventas.groupby(['oficina']).sum().unidades
df_ventas.groupby(['oficina']).unidades.sum()
df_ventas.groupby(['oficina']).mean().round(1)

df_ventas.groupby(['oficina','producto']).sum()

df_ventas.groupby('oficina').unidades.agg(['min', 'max'])

df_clientes.groupby(['ciudad']).sum()
df_clientes.groupby(['ciudad']).sum().ingresos



grupos = df_ventas.groupby(['oficina','producto'])

for n, grupo in grupos:
    print(n)
    print(grupo)

df_ventas.groupby(['oficina','producto']).first() # el primero de cada grupo


# Exportar a fichero

df_ventas.to_csv("C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\export.txt")

#Paso por referencia

df_clientes2 = df_clientes

df_clientes3 = df_clientes.copy()

df_clientes['nuevo2'] = 10


customer = {'id' : pd.Series(index=['p1', 'p2', 'p3'] , data =['0010','0041','1040']),
            'Smoke' : pd.Series(index=['p1', 'p2', 'p3'], data =['Yes','No', 'Yes']),
            'Drink' : pd.Series(index=['p1', 'p2', 'p3'], data =['Yes','Yes', 'No'])}

df_cus = pd.DataFrame(customer) 

df_cus = pd.get_dummies(data=df_cus, columns=['Smoke', 'Drink'])

#pasar el df a numpy array
arrdf = df_clientes.values

#pasar de df a lista de diccionarios
lisdoc = df.to_dict(orient='records')



