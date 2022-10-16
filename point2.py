# Realizar un programa mediante el uso de ciclos while que permita mostrar la siguiente 
# serie: 0,1,4,9,16,25,36,49 hasta el N dato... (Nota: El usuario indicará el valor de N por 
# teclado). 

userIter = int(input('Ingrese el numero de iteraciones: '))
iter = 0

succession = []

while userIter > iter:
    succession.append(iter * iter)
    iter += 1

print(succession)