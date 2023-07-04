# Importa librerías
import pandas as pd
import numpy as np
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

# Histograma ejemplo 2.1 pag.55

colesterol= [10.6, 12.5, 11.1, 9.2, 11.5, 9.9, 11.9, 11.6, 14.9, 12.5, 12.5, 12.3, 12.2, 10.8, 16.5, 15.0, 10.3, 12.4, 9.1, 7.8, 11.3, 12.3, 9.7, 12.0, 11.8, 12.7, 11.4, 9.3, 8.6, 8.5, 10.1, 12.4, 11.1, 10.2]
df=pd.DataFrame(colesterol, columns=['colinesterasa'])
df = df.rename_axis('individuo')
#df.describe().T #Para obtener total, media, std, minimo, maximo y cuartiles
# Intervalos
df['intervalos'] = pd.cut(df['colinesterasa'], bins=6)
df_intervalos=df.groupby('intervalos').count()
# Crea Histograma
# Create a histogram
df_intervalos.plot(kind='bar', legend=False)
plt.xlabel('Intervalos')
plt.ylabel('Frecuencia')
plt.title('Histograma de Intervalos')
plt.show()
'''Los resultados varían del libro'''