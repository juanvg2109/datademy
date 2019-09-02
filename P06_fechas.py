# -*- coding: utf-8 -*-
"""
Fechas

@author: Equipo
"""

import datetime

fec = datetime.datetime.now()
print(fec)

print(fec.year)
print(fec.month)
print(fec.day)

fec1 = datetime.datetime(2019, 5, 1)
fec2 = datetime.date(2019, 5, 18)

fec_str = '2019-05-15'  
fec_d = datetime.datetime.strptime(fec_str, '%Y-%m-%d')

from datetime import date

fec_hoy = date.today() # fecha de hoy

fec_hoy.weekday()  # dia de la semana

fec_hoy2 = fec_hoy.strftime("%d/%m/%y")  #cambio de formato

