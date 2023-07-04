# Importa librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Pie Chart ejemplo 2.2 pag.50
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
#Crea Pie Chart sobre caracter frecuencia_total
df.plot(kind='pie', y='frecuencia_total', labels=df['situacion'], autopct='%1.1f%%', figsize=(6, 9))
plt.axis('equal')
plt.title('Distribución Frecuencia Total')
plt.show()