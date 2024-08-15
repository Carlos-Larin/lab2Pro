#Un concesionario de autos vende vehículos nacionales e importados.
#Todos tienen 4 ruedas y capacidad para 5 pasajeros. Esta información
#debe registrarse siempre por razones de ley. Requiere un programa que
#le permita almacenar las 10 principales características de los autos. El
#precio de venta de cada auto es igual al precio de compra multiplicado
#por 1.4 que corresponde a su margen de ganancia.


class Autos():
    Marca=""
    Modelo=""
    Año=0
    Color=""
    Tipo=""
    Vin=""
    Numero_Motor=0
    PrecioCosto=0
    PrecioVenta=0
    Asientos=0
    Ruedas=0


    def __init__(self):
        self.PrecioCosto=0
        self.PrecioVenta=0
        self.Numero_Motor=0
        self.Año=0
        self.Asientos=0
        self.Ruedas=0

    def InfoDelVehiCULO(self):
        print("El vehiculo fue adquerido a: $")
        self.PrecioVenta=self.PrecioCosto*1.4
        print(self.PrecioCosto)
        print("El vehiculo queda a: $")
        print(self.PrecioVenta)

    def RegistrarVehiculo(self):
        print("Hola bienvenido al Concecionario de Marine Ford")
        self.Marca=input("Marca del vehiculo: ")
        self.Modelo=input("Modelo del vehiculo: ")
        self.Año=int(input("Año del vehiculo: "))
        self.Color=input("Color del Vehiculo: ")
        self.Tipo=input("Tipo de vehiculo: ")
        self.Vin=input("VIN: ")
        self.Numero_Motor=int(input("Numero de Motor: "))
        self.Asientos=int(input("Cantidad de Asientos: "))
        self.Ruedas=int(input("Cantidad de Ruedas: "))
        self.PrecioCosto=int(input("Precio Costo: $"))

    def DatosRayoMcqueen(self,Marca,Modelo,Año,Color,Tipo,Vin,Numero_Motor,PrecioCosto,PrecioVenta,Asientos,Ruedas):    
        self.Marca=Marca
        self.Modelo=Modelo
        self.Año=Año
        self.Color=Color
        self.Tipo=Tipo
        self.Vin=Vin
        self.Numero_Motor=Numero_Motor
        self.PrecioCosto=PrecioCosto
        self.PrecioVenta=PrecioVenta
        self.Asientos=Asientos    
        self.Ruedas=Ruedas
        
    def MostrarDatos(self):
        print("Gracias por comprar en nuestro concecionario :D")
        print("Marca del vehiculo: ")
        print("Modelo del vehiculo: ")
        print("Año del vehiculo: ")
        print("Color del Vehiculo: ")
        print("Tipo de vehiculo: ")
        print("VIN: ")
        print("Numero de Motor: ")
        print("Cantidad de Asientos: ")
        print("Cantidad de Ruedas: ")
        self.InfoDelVehiCULO()

Carro=Autos()
print("***********************Factura****************************")
print("Hola bienvenido al Concecionario de Marine Ford")
Carro.RegistrarVehiculo
print("Te Esperamos :D")
Carro.MostrarDatos
print("**********************************************************")

        


