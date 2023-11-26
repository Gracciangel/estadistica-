
    
N = int(input("ingrese el numero de inicio: "))
M = int(input("ingrese el numero Limite: "))
I = int(input("ingrese el incremento: "))
P = N 
datosX =[]
while P + I <= M : 
    P = P + I
    datosX.append(P)
    
    

datosX.insert(0 , N - I)
datosX.insert(1 , N)
datosX.append(M+I)
print(datosX)

