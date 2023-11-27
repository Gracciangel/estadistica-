from op import media_obtenida
from s import desv_tipic
from datos import datosX 
from frecuencia import frecuencia_relativa
from Colores import Colores

# segido de la formula x - media / s 
# entendiendo a x como cada numero de la lista 
# s es la desviacion tipica 

def obtener_tipificacion_variables(): 
    listaZ= []
# dentro de la listaZ se agregarn los resultados de la expresion (x - media ) / s 
    for x in datosX : 
        z = (x - media_obtenida)/ desv_tipic
        listaZ.append(z)
    
# se alteran los reultados para obtener una lista con numeros cuyos decimales sean 2 
    tipificadas = [round(z , 2 ) for z in listaZ] 
    print(f"{Colores.CYAN} LISTA DE VARIABLES TIPIFICADAS\n")
    print(tipificadas)   

    return listaZ

z = obtener_tipificacion_variables()




