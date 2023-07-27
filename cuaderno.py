# Importa librerías
import pandas as pd
import numpy as np
import math
import scipy.stats as st
import matplotlib.pyplot as plt

#2.5

#Crea DataFrame
bebe=[160, 180, 300, 380]
adulto=[400, 450, 800, 1350]
data={'volumen_bebe': bebe, 'volumen_adulto': adulto}
df=pd.DataFrame(data)
#Calcular coeficientes regresión lineal manualmente.
n = len(df['volumen_adulto'])
xy_sum = (df['volumen_adulto'] * df['volumen_bebe']).sum()
x_sum = df['volumen_bebe'].sum()
y_sum = df['volumen_adulto'].sum()
x_squared_sum = (df['volumen_bebe'] ** 2).sum()
b1 = (n * xy_sum - x_sum * y_sum) / (n * x_squared_sum - x_sum ** 2)
b0 = (y_sum - b1 * x_sum) / n
#Calcular coeficientes regresión lineal usando NumPy
coeficientes = np.polyfit(bebe, adulto, 1)
m, b = coeficientes
#Calcular Coeficiente de correlación lineal de Pearson
media_x = np.mean(bebe)
media_y = np.mean(adulto)
dif_x = np.array(bebe) - media_x
dif_y = np.array(adulto) - media_y
#Numerador
numerador = np.sum(dif_x * dif_y)
#Denominador
denominador_x = np.sqrt(np.sum(dif_x ** 2))
denominador_y = np.sqrt(np.sum(dif_y ** 2))
#Calcula r
r = numerador / (denominador_x * denominador_y)

