# Importa librerías
import pandas as pd
import numpy as np
import math
import scipy.stats as st
import matplotlib.pyplot as plt

# PieChart y BarPlot ejemplo 2.2 pag.50

# Listas con caracteres y valores
opciones= ['Rehusaron cirugía', 'Rehusaron radiación', 'Empeoraron por una enfermedad ajena al cáncer', 'Otras causas']
npersonas= [26, 3, 10, 1]
# Diccionario para crear DataFrame
data={'situacion': opciones, 'frecuencia_total': npersonas}
# DataFrame con pandas
df=pd.DataFrame(data)
# Calcula frecuencia total
frecuencia_total = df['frecuencia_total'].sum()
# Calcula frecuencia relativa
df['frecuencia_relativa'] = df['frecuencia_total'] / frecuencia_total
# Calcula frecuencia absoluta acumulada
df['frecuencia_total_acumulada'] = df['frecuencia_total'].cumsum()
# Calcula frecuencia relativa acumulada
df['frecuencia_relativa_acumulada'] = df['frecuencia_relativa'].cumsum()
#df[['frecuencia_total']].describe().T #Para obtener total, media, std, minimo, maximo y cuartiles
# Crea PieChart sobre caracter frecuencia_total
df.plot(kind='pie', y='frecuencia_total', labels=df['situacion'], autopct='%1.1f%%', figsize=(6, 9))
plt.axis('equal')
plt.title('Distribución Frecuencia Total')
plt.show()
# Crea BarPlot sobre caracter frecuencia_total
df.plot(kind='bar', x='situacion', y='frecuencia_total')
plt.xlabel('Opciones')
plt.ylabel('Frecuencia Total')
plt.title('Distribución Frecuencia Total')
plt.show()

# Histograma ejemplo 2.1 pag.53

colesterol= [10.6, 12.5, 11.1, 9.2, 11.5, 9.9, 11.9, 11.6, 14.9, 12.5, 12.5, 12.3, 12.2, 10.8, 16.5, 15.0, 10.3, 12.4, 9.1, 7.8, 11.3, 12.3, 9.7, 12.0, 11.8, 12.7, 11.4, 9.3, 8.6, 8.5, 10.1, 12.4, 11.1, 10.2]
df=pd.DataFrame(colesterol, columns=['colinesterasa'])
df = df.rename_axis('individuo')
#df.describe().T #Para obtener total, media, std, minimo, maximo y cuartiles
# Intervalos
# Define the interval values
intervalos = [7.5, 9, 10.5, 12, 13.5, 15, 16.5]
df['intervalos'] = pd.cut(df['colinesterasa'], bins=intervalos)
df_intervalos = df.groupby('intervalos').size()
# Crea Histograma
# Create a histogram
df_intervalos.plot(kind='bar', legend=False)
plt.xlabel('Intervalos')
plt.ylabel('Frecuencia')
plt.title('Histograma de Intervalos')
plt.show()
'''Los resultados varían del libro'''

# Diagrama de barras ejemplo 2.3 pag.54

# Listas con caracteres y valores
hijos= [ 0, 1, 2, 3, 4]
frecuencia= [5, 6, 8, 4, 2]
# Diccionario para crear DataFrame
data={'numero_hijos': hijos, 'frecuencia_total': frecuencia}
# DataFrame con pandas
df=pd.DataFrame(data)
# Diagrama de barras
plt.bar(df['numero_hijos'], df['frecuencia_total'])
plt.xlabel('Numero de Hijos')
plt.ylabel('Frecuencia Total')
plt.title('Diagrama de barras de Numero de Hijos')
plt.show()

# Histograma ejemplo 2.1 pag.55

colesterol= [10.6, 12.5, 11.1, 9.2, 11.5, 9.9, 11.9, 11.6, 14.9, 12.5, 12.5, 12.3, 12.2, 10.8, 16.5, 15.0, 10.3, 12.4, 9.1, 7.8, 11.3, 12.3, 9.7, 12.0, 11.8, 12.7, 11.4, 9.3, 8.6, 8.5, 10.1, 12.4, 11.1, 10.2]
df=pd.DataFrame(colesterol, columns=['colinesterasa'])
df = df.rename_axis('individuo')
#df.describe().T #Para obtener total, media, std, minimo, maximo y cuartiles
# Intervalos
df['intervalos'] = pd.cut(df['colinesterasa'], bins=6)
df_intervalos=df.groupby('intervalos').count()
# Crea Histograma
df_intervalos.plot(kind='bar', legend=False)
plt.xlabel('Intervalos')
plt.ylabel('Frecuencia')
plt.title('Histograma de Intervalos')
plt.show()
'''Los resultados varían del libro'''

#Diagrama de hojas y ramas ejemplo 2.1 pag.56

colesterol= [10.6, 12.5, 11.1, 9.2, 11.5, 9.9, 11.9, 11.6, 14.9, 12.5, 12.5, 12.3, 12.2, 10.8, 16.5, 15.0, 10.3, 12.4, 9.1, 7.8, 11.3, 12.3, 9.7, 12.0, 11.8, 12.7, 11.4, 9.3, 8.6, 8.5, 10.1, 12.4, 11.1, 10.2]
n = len(colesterol)
col_ordenado = np.sort(colesterol)
y = np.arange(1, n + 1) / n

plt.step(col_ordenado, y, where="post", linestyle="-")
plt.xlabel("Valores Col Ordenados")
plt.ylabel("Proporcion")
plt.title("Diagrama de hojas y ramas")
plt.show()

#Diagrama de cajas del ejemplo 2.1 pag.69 (Enunciado en libro dice 2.2 pero es un typo)

colesterol= [10.6, 12.5, 11.1, 9.2, 11.5, 9.9, 11.9, 11.6, 14.9, 12.5, 12.5, 12.3, 12.2, 10.8, 16.5, 15.0, 10.3, 12.4, 9.1, 7.8, 11.3, 12.3, 9.7, 12.0, 11.8, 12.7, 11.4, 9.3, 8.6, 8.5, 10.1, 12.4, 11.1, 10.2]
df=pd.DataFrame(colesterol, columns=['colinesterasa'])
df = df.rename_axis('individuo')
print(df.describe().T) # Para obtener total, media, std, minimo, maximo y cuartiles
mediana = np.median(colesterol) # Para obtener mediana
varianza = np.var(colesterol) #Para obtener varianza
print('mediana:', mediana, 'varianza:', varianza) # Printea
# Crea Boxplot
plt.boxplot(df['colinesterasa'], vert=False)
plt.xlabel('Valor')
plt.ylabel('colinesterasa')
plt.title('Diagrama de cajas')
plt.show()

#Nube de puntos del ejemplo 2.9 pag.77

# Crea listas con datos
horas=[21, 32, 15, 40, 27, 18, 26, 50, 33, 51, 36, 16, 19, 22, 16, 39, 56, 29, 45, 25]
marca=[13.2, 12.6, 13, 12.2, 15, 14.8, 14.8, 12.2, 13.6, 12.6, 13.1, 14.9, 13.9, 13.2, 15.1, 14.1, 13, 13.5, 12.7, 14.2]
# Crea gráfico
plt.scatter(horas, marca)
plt.xlabel('Horas')
plt.ylabel('Marca')
plt.title('Nube de puntos')
plt.grid(True)
plt.show()

# Calcular regresión lineal ejemplo 2.9 pag.80

horas = [21, 32, 15, 40, 27, 18, 26, 50, 33, 51, 36, 16, 19, 22, 16, 39, 56, 29, 45, 25]
marca = [13.2, 12.6, 13, 12.2, 15, 14.8, 14.8, 12.2, 13.6, 12.6, 13.1, 14.9, 13.9, 13.2, 15.1, 14.1, 13, 13.5, 12.7, 14.2]
#Calcula coeficientes regresión lineal
coeficientes = np.polyfit(horas, marca, 1)
m, b = coeficientes
#Crea gráfico
plt.scatter(horas, marca, label='Entradas de Datos')
plt.xlabel('Horas')
plt.ylabel('Marca')
plt.title('Nube de puntos con linea de Regresión Lineal')
#Añade linea de regresión lineal
plt.plot(horas, m * np.array(horas) + b, color='red', label='Regresión Lineal')
plt.legend()
plt.grid(True)
plt.show()

# Ejercicios de autoevaluación.

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
#Coeficiente variación Pearson y Asimetrías.
#Variación de Pearson
Vp = (stddev / media) * 100
#Asimetría de Pearson
Ap = (media - moda) / stddev
#Asimetría de Fisher
Af = (media - mediana) / stddev
#Resultados
print("Recorrido:", recorrido,
      'Media:', media, 
      "Moda:", moda, 
      'Mediana:', mediana, 
      'Varianza:', varianza, 
      'Desviación estandar:', stddev, 
      'Vp:', Vp, 
      'Ap:', Ap, 
      'Af:', Af)

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
media_x = np.mean(circunferencia)
media_y = np.mean(peso)
dif_x = np.array(circunferencia) - media_x
dif_y = np.array(peso) - media_y
#Numerador
numerador = np.sum(dif_x * dif_y)
#Denominador
denominador_x = np.sqrt(np.sum(dif_x ** 2))
denominador_y = np.sqrt(np.sum(dif_y ** 2))
#Calcula r
r = numerador / (denominador_x * denominador_y)

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