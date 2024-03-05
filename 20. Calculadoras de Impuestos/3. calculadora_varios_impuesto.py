print("----------------------------------------------------------")

precioconIMPUESTO = float(input("Ingrese el total: $."))
impuesto1 = float(input("Ingrese el porcentaje del impuesto: %."))
impuesto2 = float(input("Ingrese el porcentaje del impuesto: %."))
impuesto3 = float(input("Ingrese el porcentaje del impuesto: %."))
impuesto4 = float(input("Ingrese el porcentaje del impuesto: %."))

print("----------------------------------------------------------")

print("Valor sin impuesto: $.", ( (precioconIMPUESTO - (precioconIMPUESTO * (impuesto1/100))) + ( - (precioconIMPUESTO * (impuesto2/100))) + ( - (precioconIMPUESTO * (impuesto3/100))) + ( - (precioconIMPUESTO * (impuesto4/100))) ))

print("Valor del Primer Impuesto: $.", (precioconIMPUESTO * (impuesto1/100)))
print("Valor del Segundo Impuesto: $.", (precioconIMPUESTO * (impuesto2/100)))
print("Valor del Tercer Impuesto: $.", (precioconIMPUESTO * (impuesto3/100)))
print("Valor del Cuarto Impuesto: $.", (precioconIMPUESTO * (impuesto4/100)))

print("----------------------------------------------------------")
