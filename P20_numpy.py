# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:30:28 2019
ejemplos numpy

"""

"""
NumPy es una librería Python package. Viene de 'Numerical Python'. 
Es una librería para operar con arrays multidimensionales.
NumPy es usada a menudo con paquetes como SciPy (Scientific Python) y Matplotlib

"""

import numpy as np
import pandas as pd

# todos del mismo tipo, normalmente numeros, soporta una variedad
#de tipos (numéricos) muy alta
lis1 = [1,2,3,4,5]

arrnp1 = np.array(lis1)

type(lis1)
type(arrnp1)

# buscar elementos
arrnp1[0]

arrnp1[0:2]

arrnp1[[0,2,4]]

arrnp2 = np.array([[0, 1, 2], [3, 4, 5]]) # array 2 x 3

arrnp2b = arrnp2.reshape(6)
arrnp2b = arrnp2.reshape(3,2)


#pasar de df a array numpy
clientes = {'nombre': ['Jorge', 'Luis', 'Pilar', 'Ana'],
            'edad': [33, 25, 44, 37],
            'ciudad': ['Valladolid', 'Madrid', 'Madrid', 'Cuenca']   
            }

df_clientes = pd.DataFrame(clientes)
arrdf = df_clientes.values

arrnp3 = np.arange(10)

# media y desv estandar
arrnp3.mean()

arrnp3.std()

arrnp2.shape

arrnp3.dtype

arrnp4 = np.array([10,11,12])
arrnp5 = np.array([3,10,6])

# operaciones aritméticas (elemento a elemento)
res1 = arrnp4 - arrnp5
res2 = arrnp4 + arrnp5
res3 = arrnp4*arrnp5

# aleatorios
arrnp6 = np.random.random(10)
# esta asignación es por referencia
arrnp7 = arrnp6
arrnp6[7] = 50



# esta no (copia)
arrnp8 = arrnp6.copy()
arrnp9 = np.concatenate([arrnp6, arrnp8])

# Añadimos el elemento 200 al array en el  puesto del índice 5
arrnp8b = np.insert(arrnp8, 5, 200)

# filtros
res4 = arrnp8[ arrnp8 > 5]
#union vertical
arr1 = np.array([1, 2, 3])
tab1 = np.array([[9, 8, 7],
                 [6, 5, 4]])

# apila verticamente el array
tab2 = np.vstack([arr1, tab1])

# apilado horizontal
arr2 = np.array([[20],
              [21]])
tab3 = np.hstack([tab1, arr2])

# dividir un array en varios. Se pasa como argumento los puntos de corte
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])

# array de zcros o de unos
arrnp10 = np.zeros(5)
arrnp11 = np.ones(5)

# array partiendo de un iterable
arrnp12 = np.fromiter(range(10), dtype = int) 

arrnp14 = np.linspace(0,30,8)   # Array de 8 números, de 0 a 30 ambos incluidos

# operaciones I/O

np.savetxt("C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\outnp.txt",arrnp12) 
arrnp13 = np.loadtxt("C:\\trabajo\\cursos estandar\\Phyton\\ficheros\\outnp.txt") 

# Calculo matricial

arr1 = np.array([[1,2,3], [4,5,6], [7,8,9]])

mat1 = np.mat(arr1)  # Convertimos array a matriz

mat2 = mat1*mat1 #  producto matricial

mat3 = mat2.T # matriz traspuesta

mat4 =  mat3.diagonal()  #diagonal





