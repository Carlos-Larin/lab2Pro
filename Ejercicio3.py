#Un concesionario de autos vende vehículos nacionales e importados.
#Todos tienen 4 ruedas y capacidad para 5 pasajeros. Esta información
#debe registrarse siempre por razones de ley. Requiere un programa que
#le permita almacenar las 10 principales características de los autos. El
#precio de venta de cada auto es igual al precio de compra multiplicado
#por 1.4 que corresponde a su margen de ganancia.

#aqui lleva el nombre de esa clase porque se trata de un concecionario
class Autos():
    Marca=""
    Modelo=""
    Año=0
    Color=""
    Tipo=""
    Vin=""
    Numero_Motor=""
    PrecioCosto=0
    PrecioVenta=0
    Asientos=0
    Ruedas=0

#he aqui el Bob Constructor
    def __init__(self):
        self.PrecioCosto=0
        self.PrecioVenta=0
        self.Numero_Motor=""
        self.Año=0
        self.Asientos=0
        self.Ruedas=0

#como saldra el area de compra
    def InfoDelVehiCULO(self):
        self.PrecioVenta=self.PrecioCosto*1.4
        print(f"El vehiculo fue adquerido a: ${self.PrecioCosto}")
        print(f"El vehiculo queda a: ${self.PrecioVenta}")
        
 #aqui es donde el usuario ingresa los datos de la Compra  
    def RegistrarVehiculo(self):
        print("Hola bienvenido al Concecionario de Marine Ford")
        self.Marca=input("Marca del vehiculo: ")
        self.Modelo=input("Modelo del vehiculo: ")
        self.Año=int(input("Año del vehiculo: "))
        self.Color=input("Color del Vehiculo: ")
        self.Tipo=input("Tipo de vehiculo: ")
        self.Vin=input("VIN: ")
        self.Numero_Motor=input("Numero de Motor: ")
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
#la salida de los datos       
    def MostrarDatos(self):
        print("Gracias por comprar en nuestro concecionario :D")
        print("Marca del vehiculo: ",self.Marca)
        print("Modelo del vehiculo: ",self.Modelo)
        print("Año del vehiculo: ",self.Año)
        print("Color del Vehiculo: ",self.Color)
        print("Tipo de vehiculo: ",self.Tipo)
        print("VIN: ",self.Vin)
        print("Numero de Motor: ",self.Numero_Motor)
        print("Cantidad de Asientos: ",self.Asientos)
        print("Cantidad de Ruedas: ",self.Ruedas)
        self.InfoDelVehiCULO()

Carro=Autos()
print("***********************Factura****************************")
Carro.RegistrarVehiculo()
print("**********************************************************")
Carro.MostrarDatos()
print("******************Larin Estuvo Aqui***********************")
print("Te Esperamos :D")
        
