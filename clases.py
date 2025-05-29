



class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        print(f"Hola, soy {self.nombre} {self.apellido}")


hanz = Persona("Hanz", "Saenz")
hanz.saludar()

daniel = Persona("Daniel", "Saenz")
daniel.saludar()


class Perros:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def ladrar(self):
        print(f"{self.nombre} esta ladrando")

    def descripcion(self):
        print(f"{self.nombre} tiene {self.edad} años") 


lennon = Perros('Lennon', 2, 'Macho')
lennon.descripcion()
lennon.ladrar()

oz = Perros('Oz', 1, 'Macho')
oz.descripcion()
oz.ladrar()


class Rectangulo:
    def __init__(self, ancho, altura):
        self.base = ancho
        self.altura = altura

    def area(self):
        area = self.base * self.altura
        self.area = area
        return self.area
    
    def resultado(self):
        print(f"El area del rectangulo es {self.area}")

area = Rectangulo(10, 5)
area.area()
area.resultado()

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        print(f"{self.nombre} esta hablando")

class Perro(Animal, Perros):
    def __init__(self, nombre, edad, raza, genero):
        # super().__init__(nombre, edad)
        Animal.__init__(self, nombre, edad)
        Perros.__init__(self, nombre, edad, genero)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} esta ladrando")

    def mi_raza(self):
        print(f"{self.nombre} es de la raza {self.raza}")

    def mi_edad(self):
        print(f"{self.nombre} tiene {self.edad} años")

    def describeme(self):
        print(f"{self.nombre} tiene {self.edad} años y es del genero {self.genero}")

animal = Animal("Hormiga", 2)
animal.hablar()

perra=Perro('Bella', 8,'Criolla', "Femenino")
perra.ladrar()
perra.mi_raza()
perra.mi_edad()
perra.describeme()