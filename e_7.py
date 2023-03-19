from abc import ABC

class Persona(ABC):
    def __init__(self, nombre, apellido, dni, edad, email):
        self.nombre = nombre
        self.apellido = apellido    
        self.dni = dni
        self.edad = edad
        self.email = email

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} {self.edad} {self.cantidad}'

class Cuenta(Persona):
    def __init__(self, nombre, apellido, dni, edad, email, cantidad):
        super().__init__(nombre, apellido, dni, edad, email)
        self.cantidad = cantidad

    #GETTER
    @property
    def cantidad(self):
        return self.__cantidad

    #SETTER
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad
    
    def mostrar(self):
        print(f"Titular: {self.nombre} {self.apellido}")
        print(f"Cantidad: {self.cantidad}")

    def ingresar(self):
        nueva_cantidad = int(input('Ingrese la cantidad a depositar: '))
        if nueva_cantidad > 0:
            self.cantidad += nueva_cantidad
            print(f'Saldo actual: {self.cantidad}')

    def retirar(self):
        nueva_cantidad = int(input('Ingrese la cantidad a retirar: '))
        self.cantidad -= nueva_cantidad
        print(f'Saldo actual: {self.cantidad}')

cuenta_1 = Cuenta("María", "Gómez", 23456765, 43, "mariagomez@gmail.com", 80000)
cuenta_1.mostrar()
cuenta_1.ingresar()
cuenta_1.retirar()
print(cuenta_1)
cuenta_1.cantidad = 40000
print(cuenta_1)

