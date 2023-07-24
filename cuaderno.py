# Importa librerías
import pandas as pd
import numpy as np
import math
import scipy.stats as st
import matplotlib.pyplot as plt

#2.1

#Crea DataFrame
porcentajes={'Suiza': 0.30, 'España': 0.15, 'Italia': 0.10, 'Francia': 0.20, 'Austria': 0.10, 'Alemania': 0.10, 'Otro': 0.05}
df=pd.DataFrame([porcentajes]).T
df.reset_index(inplace=True)
df.columns = ['pais', 'porcentaje']
#Analizar descriptivamente los datos
medidas=df.describe().T #media, desviación estandar, min, max, cuantiles.
recorrido=df['porcentaje'].max() - df['porcentaje'].min()
media=df['porcentaje'].mean()
moda=df['porcentaje'].mode()[0]
mediana=df['porcentaje'].median()
varianza=df['porcentaje'].var()
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
