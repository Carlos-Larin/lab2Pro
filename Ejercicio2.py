#Echo por Carlos Larin y con una playlist de rock a media noche
class Papeleria():
    Cuaderno = ""
    Lapices = ""
    CantidadCuadernos = 0
    CantidadLapices = 0
    PrecioVenta = 0
    PrecioLapices = 0
    Ganancia = 0
    LlevasCuadernos = ""
    LlevasLapices = ""

    def __init__(self):
        self.Ganancia = 0
        self.Cuaderno = ""
        self.Lapices = ""
        
    def TipoCuaderno(self):
        if self.Cuaderno == "grande":
            self.PrecioVenta = (self.CantidadCuadernos * 3.50) * 1.30
            print(f"Llevas {self.CantidadCuadernos} cuadernos grandes y su precio es {self.PrecioVenta}")
            print("Marca Hojitas")
        elif self.Cuaderno == "pequeño":
            self.PrecioVenta = (self.CantidadCuadernos * 1.75) * 1.30
            print(f"Llevas {self.CantidadCuadernos} cuadernos pequeños y su precio es {self.PrecioVenta}")
            print("Marca Hojitas")
        else:
            print("No conozco esa opción")

    def TipoLapices(self):
        if self.Lapices == "grafito":
            self.PrecioLapices = (self.CantidadLapices * 0.25) * 1.30
            print(f"Llevas {self.CantidadLapices} lápices de grafito y su precio es {self.PrecioLapices}")
            print("Marca Rayitas")
        elif self.Lapices == "color":
            self.PrecioLapices = round(((self.CantidadLapices * 0.50) * 1.30),2)
            print(f"Llevas {self.CantidadLapices} lápices de color y su precio es {self.PrecioLapices}")
            print("Marca Rayitas")
        else:
            print("No conozco esa opción")

    def DatosCompra(self):
        self.TipoCuaderno()
        self.TipoLapices()
    
    def RegistrarCompra(self):
        print("*****Bienvenido al sistema nakama*****")
        self.LlevasCuadernos = input("¿Llevarás cuadernos? (S/N): ").lower()
        if self.LlevasCuadernos == "s":
            self.Cuaderno = input("Tipo de cuaderno (grande/pequeño): ").lower()
            self.CantidadCuadernos = int(input("¿Cuántos cuadernos llevas?: "))
        else: 
            print("Recuerda, tenemos producto exclusivo en cuadernos.")
        print("**********************************************")   
        self.LlevasLapices = input("¿Llevarás lápices? (S/N): ").lower()
        if self.LlevasLapices == "s":
            self.Lapices = input("Tipo de lápiz (grafito/color): ").lower()
            self.CantidadLapices = int(input("¿Cuántos lápices llevas?: "))
        else: 
            print("Recuerda, tenemos producto exclusivo en lápices.")
        print("**********************************************")   

    def MostrarDatosCompras(self):
        print("*****Bienvenido al sistema nakama*****")
        print("Estado Cuadernos: ", self.LlevasCuadernos)
        if self.LlevasCuadernos == "s":
            self.TipoCuaderno()
        else: 
            print("Recuerda, tenemos producto exclusivo en cuadernos.")
        print("**********************************************")
        print("Estado Lápices: ", self.LlevasLapices)
        if self.LlevasLapices == "s":
           self.TipoLapices()
        else: 
            print("Recuerda, tenemos producto exclusivo en lápices.")
        print("*****************************************")

# Creacion de una instancia de Papeleria
Compra1 = Papeleria()
print("***************Bienvenido al sistema nakama***************")
Compra1.RegistrarCompra()
print("**********************************************************")
Compra1.MostrarDatosCompras()
print("**********************************************************")
print("******Gracias a ti compraremos comida a Chopper***********")
print("**********************************************************")
