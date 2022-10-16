purchaseValue = int(input('Ingrese el valor de la compra: '))
paymentValue = 0

if purchaseValue >= 1000:
    purchaseValue = purchaseValue * 0.5
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

