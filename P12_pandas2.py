# -*- coding: utf-8 -*-
"""
# -*- coding: utf-8 -*-

Ejemplos pandas

"""
import pandas as pd

# Crear un dataframe desde una lista de diccionarios

dic = {'ciudad': 'Madrid', 'ventas': 100, 'centro': 'C1', 'año': 2018}

lis_dic = [
        {'ciudad': 'Madrid', 'ventas': 100, 'centro': 'C1', 'año': 2018},
        {'ciudad': 'Valencia', 'ventas': 100, 'año': 2018},
        {'ciudad': 'Murcia', 'ventas': 100, 'centro': 'C6', 'año': 2018},
        { 'ventas': 100, 'centro': 'C6', 'año': 2018}        
        ]

df = pd.DataFrame(lis_dic)

lis_dic2 = [
        {'ciudad': 'Madrid', 'ventas': 100, 'centro': ['C1','C2'], 'año': 2018},
        {'ciudad': 'Valencia', 'ventas': 100, 'año': 2018},
        {'ciudad': 'Murcia', 'ventas': 100, 'centro': ['C3','C4','C5'], 'año': 2018},
        { 'ventas': 100, 'centro': ['C6'], 'año': 2018}        
        ]

df2 = pd.DataFrame(lis_dic2)