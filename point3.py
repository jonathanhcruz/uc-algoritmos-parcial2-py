# Realizar un programa utilizando ciclos  while que permita obtener la siguiente figura: 
# (Nota: El usuario indicará el valor de N por teclado). 

userIter = int(input('Ingrese el numero de iteraciones: '))
iter = 0

while userIter > iter:
    data = []

    if iter != 0:
        for i in range(iter):
            data.append('*')

    data.append('O')
    print(''.join(data))
    iter += 1
