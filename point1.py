# IMC
weight = float(input("Ingrese su peso en kg: "))
height = float(input("Ingrese su estatura en m: "))

imc = weight / height ** 2

print("Su IMC es: ", imc)
print("Su altura es: ", height, "m")
print("Su peso es: ", weight, "kg")

if imc < 16:
    print("Criterio de ingreso en hospital")
elif imc >= 16 and imc < 17:
    print("Infra peso")
elif imc >= 17 and imc < 18:
    print("Bajo peso")
elif imc >= 18 and imc < 25:
    print("Peso normal (saludable)")
elif imc >= 25 and imc < 30:
    print("Sobrepeso (obesidad de grado 1)")
elif imc >= 30 and imc < 35:
    print("Sobrepeso cronico (obesidad de grado 2)")
elif imc >= 35 and imc < 40:
    print("Obesidad premorbida (obesidad de grado 3)")
elif imc >= 40:
    print("Obesidad morbida (obesidad de grado 4)")