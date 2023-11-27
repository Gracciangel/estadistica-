from Colores import Colores
# en este sistema la desviacion tipica solo se ingresa manualmente 

def desviacion_tipica() :
    s = input(f'{Colores.AMARILLO}ingrese la desviacion tipica:\n ')
 # en caso que la desviacion tipica sea un numero flotante    
    if '.' in s : 
        try :
            s = float(s)
        except ValueError :
            print(f"{Colores.ROJO}la desviacion tipica no es un numero valido \n ")
            s = input(f'{Colores.AMARILLO}ingrese la desviacion tipica:\n ')
            
# en caso de que la desviacion tipica no sea un numero flotante si no un entero
    else :
        try :
            s = int(s)
        except ValueError :
            print(f'{Colores.ROJO}la desviacion tpica ingresada no es un numero valido \n')
            s = input(f'{Colores.AMARILLO}ingrese la desviacion tipica:\n ')
    
    return s 


desv_tipic = desviacion_tipica()