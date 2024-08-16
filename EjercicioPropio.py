#Ejercicio 5 el propio
#Una Farmacia Vende producto controlado (con o sin receta)
#Todos son de la marca SanGithub que es una nueva marca que está entrando en el mercado. 
#Se requiere almacenar sus 5 principales características. 
#Todos son productos importados y su precio de venta es igual al precio de compra multiplicado por 1.3 que corresponde a su margen de ganancia.

class Farmacia:
    TipoMedicamento = ""
    Medicamento = ""
    Cantidad = 0
    PrecioCosto = 0
    PrecioVenta = 0

    def __init__(self):
        self.PrecioCosto = 0
        self.PrecioVenta = 0
        self.Cantidad = 0
#aqui redondeo porque sino van a salir un monton de decimales
    def Cobro(self):
        self.PrecioVenta = round((self.Cantidad * self.PrecioCosto) * 1.3, 2)
        print(f"Precio a Cobrar: ${self.PrecioVenta}")

        
    def DatosCompra(self):
        self.Cobro()
 #aqui es donde el usuario ingresa los datos de la Compra  
    def RegistrarCompra(self):
        print("***** Bienvenido al sistema nakama *****")
        self.TipoMedicamento = input("¿Llevaras Medicamento con Receta? (S/N): ").lower()
        self.Medicamento = input("Nombre del medicamento: ")
        self.Cantidad = int(input(f"¿Cuantos {self.Medicamento} llevas?: "))
        self.PrecioCosto = float(input("Precio del Laboratorio: $"))
        print("*********************************************")   

    def MostrarDatosCompras(self):
        print("***** Detalles de la Compra *****")
        if self.TipoMedicamento == "s":
            print("Es un producto controlado.")
            print("Recuerda consumir de manera controlada, ya que es con receta.")
        else: 
            print("Recuerda, no vendemos productos controlados sin receta.")
        print("**********************************************")
        print(f"Medicamento: {self.Medicamento}")
        print(f"Cantidad: {self.Cantidad}")
        self.DatosCompra()

#Creacion de una instancia de Farmacia
Compra1 = Farmacia()
print("*********** Bienvenido al sistema ***********")
Compra1.RegistrarCompra()
Compra1.MostrarDatosCompras()
print("*********************************************")
print("****** Maria Devuelveme a los niños *********")
print("*********************************************")
