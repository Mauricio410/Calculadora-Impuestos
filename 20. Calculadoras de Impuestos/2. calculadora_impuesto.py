print("----------------------------------------------------------")

precioconIMPUESTO = float(input("Ingrese el total: $."))
impuesto = float(input("Ingrese el porcentaje del impuesto: %."))

print("----------------------------------------------------------")

print("Valor sin impuesto: $.", (precioconIMPUESTO - (precioconIMPUESTO * (impuesto/100))))

print("Valor del Impuesto: $.", (precioconIMPUESTO * (impuesto/100)))

print("----------------------------------------------------------")
