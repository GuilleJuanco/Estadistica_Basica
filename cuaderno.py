# Importa librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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