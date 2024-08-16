#Ejercicio4
#Un almacén vende dispositivos electrónicos (celulares, tablets y portátiles). 
#Todos PHR que es una nueva marca que está entrando en el mercado. 
#Se requiere almacenar sus 6 principales características. 
#Todos son productos importados y su precio de venta es igual al precio de compra multiplicado por 1.7 que corresponde a su margen de ganancia.

class PHR():
    TipoProducto=""
    Modelo=""
    Almacenamiento=0
    RAM=0
    PrecioCosto=0
    PrecioVenta=0

    def __init__(self):
        self.PrecioCosto=0
        self.PrecioVenta=0
        self.Almacenamiento=0
        self.RAM=0

    def InfoDelProducto(self):
        self.PrecioVenta=self.PrecioCosto*1.7
        print(f"El Articulo fue adquerido a: ${self.PrecioCosto}")
        print(f"El Articulo queda a: ${self.PrecioVenta}")
        

    def RegistrarProducto(self):
        print("Hola bienvenido a PHR")
        self.TipoProducto=input("Tipo de Producto: ")
        self.Modelo=input("Modelo: ")
        self.Almacenamiento=int(input("Almacenamiento: "))
        self.RAM=int(input("RAM: "))
        self.PrecioCosto=int(input("Precio Proveedor: $"))
        

    def DatosPHR(self,PrecioCosto,PrecioVenta,TipoProducto,Modelo,Almacenamiento,RAM):    
        self.TipoProducto=TipoProducto
        self.Modelo=Modelo
        self.Almacenamiento=Almacenamiento
        self.RAM=RAM
        self.PrecioCosto=PrecioCosto
        self.PrecioVenta=PrecioVenta

        
    def MostrarDatos(self):
        print("Gracias por comprar en PHR :D")
        print("Tipo de producto: ",self.TipoProducto)
        print(f"Modelo del {self.TipoProducto}: ",self.Modelo)
        print("Almacenamiento: ",self.Almacenamiento," Gigas")
        print("RAM: ",self.RAM, " Gigas")
        self.InfoDelProducto()

Articulo=PHR()
print("***********************Factura****************************")
Articulo.RegistrarProducto()
print("**********************************************************")
Articulo.MostrarDatos()
print("******************Larin Estuvo Aqui***********************")
print("Te Esperamos :D")
        