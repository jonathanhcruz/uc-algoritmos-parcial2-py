# Realice un programa que permita de acuerdo a la compra: aplicar un descuento (20%) 
# a  los  clientes  cuya  compra  supere  los  $ 300,  aplicar  un descuento  (30%) a  los  clientes 
# cuya  compra  supere  los $  400,  aplicar  un  descuento  (40%)  a  los  clientes cuya  compra 
# supere  los  $  600,  aplicar  un  descuento  (50%)  a  los  clientes  cuya  compra  supere  los  $ 
# 1000, El programa debe solicitarle al usuario el valor de la compra y mostrar la pantalla 
# cuanto debe pagar.  
  

purchaseValue = int(input('Ingrese el valor de la compra: '))
paymentValue = 0

if purchaseValue >= 1000:
    paymentValue = purchaseValue * 0.5
    print('Se aplica descuento del 50%')
elif purchaseValue >= 600:
    paymentValue = purchaseValue * 0.6
    print('Se aplica descuento del 40%')
elif purchaseValue >= 400:
    paymentValue = purchaseValue * 0.7
    print('Se aplica descuento del 30%')
elif purchaseValue >= 300:
    paymentValue = purchaseValue * 0.8
    print('Se aplica descuento del 20%')
else:
    print('No se aplica descuento')
    paymentValue = purchaseValue

print('El valor a pagar es: ', str(paymentValue)+'$')

