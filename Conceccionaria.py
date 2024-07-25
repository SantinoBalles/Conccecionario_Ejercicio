#Hacer una conccecionaria de vehiculos, donde se gestione la compra y venta.
#El usuario va a poder preguntar cuales son los qu eestan disponibles. Su precio y va a poder comprar Uno.

class Automovil:
    def __init__(self,modelo,año,precio,color,km):
        self.modelo = modelo
        self.año = año
        self.precio = precio
        self.color = color
        self.km = km

    def vendido(self,disponible):
        self.disponible = disponible
        if self.disponible == False:
            print(f"el {self.modelo} esta vendido")
        else:
            print(f"el {self.modelo} esta disponible")

    def get_data(self):
            print(f"El auto es un : {self.modelo}")
            print(f"el precio del vehículo es: {self.precio}")
            print(f"el año del auto es: {self.año}")
            print(f"El color del automovil es: {self.color}")
            print(f"la cantidad de km que tiene son: {self.km}")
        
Auto_1 = Automovil("Ford Mondeo",2021,"30000 USD","Blanco","37,000 km")
Auto_2 = Automovil("Toyota Corolla",2024,"25000 USD","Negro","0 km")
Auto_3 = Automovil("Vw Passat CC",2014,"14000 USD","Blanco","189,000 km")
Auto_4 = Automovil("Ford Mustang",2023,"95000 USD","Rojo","12,000 km")
Auto_5 = Automovil("Mercedes Benz A200",2022,"40000 USD","Blanco","67,000 km")

Auto_1.get_data()
Auto_1.vendido(True)
Auto_2.get_data()
Auto_2.vendido(True)
Auto_3.vendido(False)
Auto_3.get_data()
Auto_4.vendido(True)
Auto_4.get_data()
Auto_5.vendido(False)
Auto_5.get_data()

class Cliente:
    def __init__(self,nombre,):
        self.nombre = nombre
        self.colleción = []


    


    

