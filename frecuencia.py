from datos import datosX
    
def crear_frecuencia():  
    frecuencia = []
    frecuencia_relativa = []
    n = 0 
    frecuencia.append(n)

    F1 = int(input('INGRESA EL PRIMER DATO A CARGAR (NO INGRESES 0 (CERO)): '))
    print('SELECCIONA 0 (cero) PARA TERMINAR DE CARGAR LOS DATOS')
    while F1 != 0 :
        frecuencia.append(F1)
        F1 = int(input('Ingrese el siguiente dato: '))
        
            
    frecuencia.append(n) 
    print(frecuencia)

    if len(frecuencia) == len(datosX) :
        print('las listas estan completas')
    else:
        print('Las listas estan INCOMPLETAS por favor volve a ingresar los datos')
    
    suma = 0 
    for f in frecuencia :
        suma = suma + f 
    
    for f in frecuencia : 
        frecuencia_relativa.append((f / suma) * 100)    

    freq_relativ =  [round(f , 2 ) for f in frecuencia_relativa]
    return freq_relativ

frecuencia_relativa = crear_frecuencia()








