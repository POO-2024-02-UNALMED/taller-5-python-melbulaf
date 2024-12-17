from zooAnimales.animal import Animal

class Ave(Animal):
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Animal.aves.append(self)

    def getColorPlumas(self):
        return self._colorPlumas

    def movimiento(self):
        return "volar"

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return cls(nombre, edad, "montañas", genero, "café glorioso")

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return cls(nombre, edad, "montañas", genero, "blanco y amarillo")