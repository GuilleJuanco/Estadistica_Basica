# Importa librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
