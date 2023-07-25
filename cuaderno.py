# Importa librerías
import pandas as pd
import numpy as np
import math
import scipy.stats as st
import matplotlib.pyplot as plt

#2.3

#Crea DataFrame
gang_size=[[3, 6], [6, 11], [11, 16], [16, 21], [21, 26], [26, 31], [31, 41], [41, 51], [51, 76], [76, 101], [101, 201], [201, 501], [501, 1000]]
frecuencia_abs=[37, 198, 191, 149, 79, 46, 55, 51, 26, 25, 25, 11, 2]
punto_medio=[(l[0] + l[1]) / 2 for l in gang_size]
long_intervalo=[(l[1]-l[0]) for l in gang_size]
frecuencia_std=[(f/li) for f, li in zip(frecuencia_abs, long_intervalo)]
# Diccionario para crear DataFrame
data={'tamaño': gang_size,'pm': punto_medio, 'long_int': long_intervalo, 'frecuencia_absoluta': frecuencia_abs, 'frecuencia_estandar': frecuencia_std}
# DataFrame con pandas
df=pd.DataFrame(data)
#Análisis descriptivo
recorrido=df['pm'].max() - df['pm'].min()
media=(df['pm'] * df['frecuencia_absoluta']).sum() / df['frecuencia_absoluta'].sum()
moda=df.loc[df['frecuencia_estandar'].idxmax(), 'tamaño'][0] + (df.at[df['frecuencia_estandar'].idxmax() + 1, 'frecuencia_estandar'] * (df.loc[df['frecuencia_estandar'].idxmax(), 'tamaño'][1] - df.loc[df['frecuencia_estandar'].idxmax(), 'tamaño'][0])) / (df.at[df['frecuencia_estandar'].idxmax() - 1, 'frecuencia_estandar'] + df.at[df['frecuencia_estandar'].idxmax() + 1, 'frecuencia_estandar'])
#Esta vez, para la mediana, voy a escoger los datos directamente de la tabla manualmente en vez de crear variables con forma de función.
df['frecuencia_acumulada'] = df['frecuencia_absoluta'].cumsum()
mitad=df['frecuencia_acumulada'].max()/2
#n/2 es igual a 447.5 por lo que cj-1 es 16, Nj-1 es 426, nj es 149 y aj es 5.
mediana=(447.5 / 149 - 426 / 149) * 5 + 16
#Cuartiles. De forma manual. n=895, 
primercuartil = (((1/4) * 895) / 198 - 37 / 198) * 5 + 6
sextodecil=(((6/10) * 895) / 149 - 426 / 149) * 5 + 16
#Varianza
diferencia_cuadrados = [(puntomed - media) ** 2 * frecuencia for puntomed, frecuencia in zip(df['pm'], df['frecuencia_absoluta'])]
sumatoria_cuadrados = sum(diferencia_cuadrados)
varianza = sumatoria_cuadrados / sum(df['frecuencia_absoluta'])
stddev=math.sqrt(varianza)
#Coeficiente variación Pearson y Fisher.
