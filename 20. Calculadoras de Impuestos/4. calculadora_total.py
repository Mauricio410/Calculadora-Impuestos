print("----------------------------------------------------------")

preciosinIMPUESTO = float(input("Ingrese el valor: $."))
impuesto = float(input("Ingrese el porcentaje del impuesto: %."))

total = preciosinIMPUESTO + (preciosinIMPUESTO * (impuesto/100))

print("----------------------------------------------------------")

print("Valor del Impuesto: $.", (preciosinIMPUESTO * (impuesto/100)))

print("Total a pagar: $.", total)

print("----------------------------------------------------------")
