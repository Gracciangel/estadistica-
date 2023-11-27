import matplotlib.pyplot as plt 
import seaborn as sns 
from frecuencia import frecuencia_relativa 
from tipificar_variables import z
from Colores import Colores
#grafico de barras 
def graficar_barras() :
    
    plt.bar(range(len(frecuencia_relativa)), frecuencia_relativa, alpha=0.5, label='Datos 1')
    plt.bar(range(len(z)), z, alpha=0.5, label='Datos 2')

    plt.xlabel(z)
    plt.ylabel(frecuencia_relativa)
    plt.title('Grafico de Barras')
    plt.show()
#grafico de dispersion 

def grafico_dispersion() :
    plt.scatter(z, frecuencia_relativa)
    plt.show()
    

def opciones():
    options = ['Barras', 'Dispersion', 'Salir']
    ln = "\n"
    count = 0
    counter = 1
    print("***** OPCIONES PARA GRAFICAR ****\n")
    print("seleccione una opcion\n")
    
    
    while count < 3 :
        print(f"{counter}: {options[count]+ln}")
        counter = counter + 1 
        count = count +1         
    select = input('_______')
    
    if select == '1' :
        graficar_barras()
    if select == '2' :
        grafico_dispersion()
    if select == '3' :
        False 
        
opciones()


