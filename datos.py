
# N es el primer numero de la lista 
N = int(input("ingrese el numero de inicio: "))
# M es el limite de la lista 
M = int(input("ingrese el numero Limite: "))
# I es la progresion aritmetica, cada cuanto ira progresando de nunero en numero 
I = int(input("ingrese el incremento: "))
P = N 

# lista de numeros vacia 
datosX =[]
while P + I <= M : 
    P = P + I
    datosX.append(P)
    
    
# preceder la lista con el numero - la progresion aritmetica
datosX.insert(0 , N - I)
# insertar el numero en la posicion 1 de la lista para que la lista tenga consistencia
datosX.insert(1 , N)
# terminar la lista con el numero final + su progresion aritmetica
datosX.append(M+I)

#impresion de la lista
print(datosX)

