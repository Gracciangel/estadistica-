from datos import datosX
from Colores import Colores    
def crear_frecuencia():  
    frecuencia = []
    frecuencia_relativa = []
    n = 0 
    frecuencia.append(n)
    print(f'{Colores.MAGENTA}INGRESA EL PRIMER DATO A CARGAR (NO INGRESES 0 (CERO)): \n')
    print(f'{Colores.CYAN}SELECCIONA 0 (cero) PARA TERMINAR DE CARGAR LOS DATOS\n')
    F1 = int(input())
    indice = len(datosX) -1 
    while  len(frecuencia)< indice :
        frecuencia.append(F1)
        F1 = int(input(f'{Colores.VERDE}Ingrese el siguiente dato: '))
        
            
    frecuencia.append(n) 
    print(frecuencia)
    print("\n")
  
    
    suma = 0 
    for f in frecuencia :
        suma = suma + f 
    
    for f in frecuencia : 
        frecuencia_relativa.append((f / suma) * 100)    

    freq_relativ =  [round(f , 2 ) for f in frecuencia_relativa]
    return freq_relativ

frecuencia_relativa = crear_frecuencia()








