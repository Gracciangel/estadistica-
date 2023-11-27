from datos  import datosX
from frecuencia import frecuencia_relativa

# funcion para definir la media de la lista 
def media() : 
    media = 0
    media_auto = input('ingresa si para obtener la media automaticamente \n o no para ingresarla manualmente: ')
  
    count = 0 
# en caso de querer la media automatica se procede a ingresar "si"
    if media_auto == 'si' : 
        for x in datosX : 
            count = count + x 
            media = count // len(datosX)
        print(f"la media es: {media}")
# en caso de ingresar una media manualmente se procede a ingresar "no"
    if(media_auto == 'no'): 
        count = int(input('ingrese la media manualmente: '))
        media  = count 
        print(f"la media es: {media}")
        
        return media
media_obtenida = media()
