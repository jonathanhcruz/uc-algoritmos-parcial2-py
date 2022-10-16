userIter = int(input('Ingrese el numero de iteraciones: '))
iter = 0

succession = []

while userIter > iter:
    succession.append(iter * iter)
    iter += 1

print(succession)