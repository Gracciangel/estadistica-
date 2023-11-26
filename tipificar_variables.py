from op import media_obtenida
from s import desv_tipic
from datos import datosX 
from frecuencia import frecuencia_relativa


def obtener_tipificacion_variables(): 
    listaZ= []
    for x in datosX : 
        z = (x - media_obtenida)/ desv_tipic
        listaZ.append(z)
    
    
    tipificadas = [round(z , 2 ) for z in listaZ] 
    print(tipificadas)   

    return listaZ

z = obtener_tipificacion_variables()




