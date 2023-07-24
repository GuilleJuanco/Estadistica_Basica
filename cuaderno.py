# Importa librerías
import pandas as pd
import numpy as np
import math
import scipy.stats as st
import matplotlib.pyplot as plt

#2.2

#Crea DataFrame
iva={'España': 0.16, 'Italia': 0.20, 'Belgica': 0.06, 'Holanda': 0.06, 'Alemania': 0.07, 'Portugal': 0.17, 'Luxemburgo': 0.06, 'Finlandia': 0.22}
df=pd.DataFrame([iva]).T
df.reset_index(inplace=True)
df.columns = ['pais', 'iva']
#Analizar descriptivamente los datos
medidas=df.describe().T #media, desviación estandar, min, max, cuantiles.
recorrido=df['iva'].max() - df['iva'].min()
media=df['iva'].mean()
moda=df['iva'].mode()[0]
mediana=df['iva'].median()
'''En el ejercicio anterior hemos determinado como Varianza la Cuasivarianza 
ya que NumPy así lo establece, esta vez calcularemos la varianza y desviación
típica manualmente'''
diferencia_cuadrados = [(x - media) ** 2 for x in df['iva']]
sumatoria_cuadrados = sum(diferencia_cuadrados)
varianza = sumatoria_cuadrados / len(df['iva'])
stddev=math.sqrt(varianza)
#Variación de Pearson
Vp = (stddev / media) * 100
#Asimetría de Pearson
Ap = (media - moda) / stddev
#Asimetría de Fisher
Af = (media - mediana) / stddev
#Resultados
print(medidas)
print("Recorrido:", recorrido,'Media:', media, "Moda:", moda, 'Mediana:', mediana, 'Varianza:', varianza, 'Desviación estandar:', stddev, 'Vp:', Vp, 'Ap:', Ap, 'Af:', Af)