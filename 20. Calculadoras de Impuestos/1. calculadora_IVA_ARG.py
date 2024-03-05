def calculariva(n):
    IVA = n * 0.21
    return IVA

print("----------------------------------------------------------")

preciosinIVA = float(input("Ingrese el valor de la compra: $.",))

IVA = calculariva(preciosinIVA)

print("----------------------------------------------------------")

print("El valor de la compra sin el impuesto IVA es de: $.", preciosinIVA)

print("El valor total de la compra con IVA es de: $.", (preciosinIVA + IVA))

print("----------------------------------------------------------")
