
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio * self.radio

# Uso de la abstracción
mi_circulo = Circulo(5)
area = mi_circulo.calcular_area()
print(f"Área del círculo: {area}") 