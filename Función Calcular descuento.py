
 #crearemos una funcion llamada "Calcular_descuentos"

def calcular_descuento(precio, descuento=.10):
   valor_descuento = precio * descuento
   precio_final = precio - valor_descuento
   return precio_final

precio = float(input("Ingrese el precio: "))
descuento = float(input("Ingrese el descuento: "))

precio_final = calcular_descuento(precio, descuento)

print(f"El precio normal es de ${precio}")
print(f"Su valor de descuento es de ${descuento}")
print(f"El precio final a pagar es de ${precio_final}")

precio = float(input("Ingrese el precio: "))
precio_final = calcular_descuento(precio)
print(f"El precio final a pagar es de ${precio_final}")