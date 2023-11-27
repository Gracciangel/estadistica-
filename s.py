
# en este sistema la desviacion tipica solo se ingresa manualmente 

def desviacion_tipica() :
    s = input('ingrese la desviacion tipica: ')
 # en caso que la desviacion tipica sea un numero flotante    
    if '.' in s : 
        try :
            s = float(s)
        except ValueError :
            print("la desviacion tipica no es un numero valido ")
            s = input('ingrese la desviacion tipica: ')
            
# en caso de que la desviacion tipica no sea un numero flotante si no un entero
    else :
        try :
            s = int(s)
        except ValueError :
            print('la desviacion tpica ingresada no es un numero valido')
            s = input('ingrese la desviacion tipica: ')
    
    return s 


desv_tipic = desviacion_tipica()