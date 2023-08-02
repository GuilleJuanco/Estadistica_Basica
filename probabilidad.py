# Importa librerías
import pandas as pd
import numpy as np
import math
import scipy.stats as st
import matplotlib.pyplot as plt

#Ejemplo 3.3 pag.96.
dic={'azules': [0.05], 'verdes': [0.02], 'castaños': [0.69], 'negros': [0.24]}
prob=dic['azules'][0] + dic['verdes'][0]

#Ejemplo 3.10 pag.102.
dic={'a': [0.3, 0.2], 'b': [0.1, 0.4], 'c': [0.6, 0.05]}
prob=dic['a'][0] * dic['a'][1] + dic['b'][0] * dic['b'][1] + dic['c'][0] * dic['c'][1]

#Ejercicio 3.1 pag.103
#Ecuación resuelta manualmente
'''
p ** 2 - (1 - p) ** 2 = 1/9
p ** 2 - (1 - 2p + p ** 2) = 1/9
p ** 2 - 1 + 2p - p ** 2 = 1/9
-1 + 2p = 1/9
2p = 1/9 + 9/9 
p = 10/9 / 2
p = 5/9
'''

#Ejercicio 3.2 pag.103
pa=1/4
pb=1/10
pc=1/40
AUB = pa + pb - (pa * pb)
AUC = pa + pc - (pa * pc)

#Ejercicio 3.3 pag.103
pa=0.4
pb=0.6
pc=0.85
p= pa * pb * pc

#Ejercicio 3.4 pag.103
pa = 4/40
pb = 4/40
pba = 3/39

#a)
p1 = pa * pb
#b)
p2 = pa * pba