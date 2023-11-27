import matplotlib.pyplot as plt 
import seaborn as sns 
from frecuencia import frecuencia_relativa 
from tipificar_variables import z

#grafico de barras 

plt.bar(range(len(frecuencia_relativa)), frecuencia_relativa, alpha=0.5, label='Datos 1')
plt.bar(range(len(z)), z, alpha=0.5, label='Datos 2')

plt.xlabel(z)
plt.ylabel(frecuencia_relativa)
plt.title('Grafico de Barras')

#grafico de dispersion 

# plt.scatter(z, frecuencia_relativa)


plt.show()

input('presiona una tecla para terminar')



