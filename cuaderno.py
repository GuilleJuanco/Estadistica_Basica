# Importa librerías
import pandas as pd
import numpy as np
import math
import scipy.stats as st
import matplotlib.pyplot as plt

#2.4

#Crea DataFrame
circunferencia=[68,100, 85, 133, 130, 165, 120, 120, 155, 117]
peso=[6, 6.3, 6, 6.3, 7, 8, 7, 8.1, 9, 6.6]
data={'circunferencia_cm': circunferencia, 'peso_gramos': peso}
df=pd.DataFrame(data)
#Calcular coeficientes regresión lineal manualmente.
n = len(df['peso_gramos'])
xy_sum = (df['peso_gramos'] * df['circunferencia_cm']).sum()
x_sum = df['circunferencia_cm'].sum()
y_sum = df['peso_gramos'].sum()
x_squared_sum = (df['circunferencia_cm'] ** 2).sum()
b1 = (n * xy_sum - x_sum * y_sum) / (n * x_squared_sum - x_sum ** 2)
b0 = (y_sum - b1 * x_sum) / n
#Calcular coeficientes regresión lineal usando NumPy
coeficientes = np.polyfit(circunferencia, peso, 1)
m, b = coeficientes
#Calcular Coeficiente de correlación lineal de Pearson

