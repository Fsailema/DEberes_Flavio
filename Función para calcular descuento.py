
def calcular_descuento(precio, bono_descuento, descuento=.10):
    valor_descuento = precio * descuento
    precio_final = precio - valor_descuento - bono_descuento
    return precio_final

total = calcular_descuento(100, 10)
print(f"El precio final es de ${total:.2f}")


total = calcular_descuento(97, 40, 0.12)
print(f"El precio final es de ${total:.2f}")



