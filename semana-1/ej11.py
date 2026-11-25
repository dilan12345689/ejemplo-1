monto = float(input("Ingrese el monto de la compra: "))

if monto > 1000:
    descuento = monto * 0.10
    precio_final = monto - descuento
else:
    descuento = 0
    precio_final = monto

print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Precio final: ${precio_final:.2f}")   