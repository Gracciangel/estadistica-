def desviacion_tipica() :
    s = input('ingrese la desviacion tipica: ')
    
    if '.' in s : 
        try :
            s = float(s)
        except ValueError :
            print("la desviacion tipica no es un numero valido ")
            s = input('ingrese la desviacion tipica: ')
    else :
        try :
            s = int(s)
        except ValueError :
            print('la desviacion tpica ingresada no es un numero valido')
            s = input('ingrese la desviacion tipica: ')
    
    return s 


desv_tipic = desviacion_tipica()