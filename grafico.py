import matplotlib.pyplot as plt 
import seaborn as sns 
from frecuencia import frecuencia_relativa 
from tipificar_variables import z

plt.bar(range(len(frecuencia_relativa)), frecuencia_relativa, alpha=0.5, label='Datos 1')
plt.bar(range(len(z)), z, alpha=0.5, label='Datos 2')

plt.xlabel(frecuencia_relativa)
plt.ylabel(z)
plt.title('Grafico de Barras')

plt.show()

input('presiona una tecla para terminar')



