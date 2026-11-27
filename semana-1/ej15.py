weight = float(input("Peso en Kg: "))
height = float(input("Altura en metros: "))

imc = weight / height ** 2
print("Tu IMC es: ", round(imc, 2))

if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")