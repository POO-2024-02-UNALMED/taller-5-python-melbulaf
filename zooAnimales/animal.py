class Animal:
    totalAnimales = 0
    mamiferos = []
    aves = []
    reptiles = []
    peces = []
    anfibios = []

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal.totalAnimales += 1

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        return f"Mamiferos : {len(Animal.mamiferos)}\nAves : {len(Animal.aves)}\nReptiles : {len(Animal.reptiles)}\nPeces : {len(Animal.peces)}\nAnfibios : {len(Animal.anfibios)}"

    def toString(self):
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"