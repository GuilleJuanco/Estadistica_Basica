# Importa librerías
import pandas as pd
import numpy as np
import math
import scipy.stats as st
import matplotlib.pyplot as plt

#Ejemplo 3.10 pag.102.
dic={'a': [0.3, 0.2], 'b': [0.1, 0.4], 'c': [0.6, 0.05]}
prob=dic['a'][0] * dic['a'][1] + dic['b'][0] * dic['b'][1] + dic['c'][0] * dic['c'][1]