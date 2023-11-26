from datos  import datosX
from frecuencia import frecuencia_relativa


def media() : 
    media = 0
    media_auto = input('ingresa si para obtener la media automaticamente \n o no para ingresarla manualmente: ')
  
    count = 0 

    if media_auto == 'si' : 
        for x in datosX : 
            count = count + x 
            media = count // len(datosX)
        print(f"la media es: {media}")

    if(media_auto == 'no'): 
        count = int(input('ingrese la media manualmente: '))
        media  = count 
        print(f"la media es: {media}")
        
        return media
media_obtenida = media()
