print("----------------------------------------------------------")

preciosinIMPUESTO = float(input("Ingrese el valor: $."))
impuesto1 = float(input("Ingrese el porcentaje del impuesto: %."))
impuesto2 = float(input("Ingrese el porcentaje del impuesto: %."))
impuesto3 = float(input("Ingrese el porcentaje del impuesto: %."))
impuesto4 = float(input("Ingrese el porcentaje del impuesto: %."))


total = preciosinIMPUESTO + (preciosinIMPUESTO * (impuesto1/100)) + (preciosinIMPUESTO * (impuesto2/100)) + (preciosinIMPUESTO * (impuesto3/100)) + (preciosinIMPUESTO * (impuesto4/100))

print("----------------------------------------------------------")

print("Valor del Impuesto: $.", (preciosinIMPUESTO * (impuesto1/100)))
print("Valor del Impuesto: $.", (preciosinIMPUESTO * (impuesto2/100)))
print("Valor del Impuesto: $.", (preciosinIMPUESTO * (impuesto3/100)))
print("Valor del Impuesto: $.", (preciosinIMPUESTO * (impuesto4/100)))

print("Total a pagar: $.", total)

print("----------------------------------------------------------")
