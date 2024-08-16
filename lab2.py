#Este es El ejemplo :D este codigo lo Hizo Larin
class Libro():
    tamaño="17x24"
    paginas=0
    precioVenta=0
    peso=0
    precioXPag=0
    pesoXPag=0
    titulo=""
    tapa=""
    URL=""
    ISBN=""
    Estado="No Hay Registros del Libro"
#Este es El constructor
    def __init__(self):
        self.tamaño="17x24"
        self.precioXPag=300
        self.pesoXPag=0.8

    def RegistraLibro(self):
        Estado="Registrado"
        return Estado
    
    def PrecioXPagina(self):
        return  self.precioXPag
    
    def PesoXPagina(self):
        return  self.pesoXPag
    def TamañoLibro(self):
        return  self.tamaño
    #Este Segemnto del codigo me ayuda a hacer los procesos
    def DatosLibro(Libro,NumPag,Nombre,TipoTapa,URLLibro,ISBNLibro):
        Libro.paginas=NumPag
        Libro.precioVenta=Libro.precioXPag*NumPag
        Libro.peso=Libro.pesoXPag*NumPag
        Libro.titulo=Nombre
        Libro.tapa=TipoTapa
        Libro.URL=URLLibro
        Libro.ISBN=ISBNLibro
    #area por donde entran los datos bien inzanos
    def RecibeDatosLibro(self):
        Nombre = input("Hola por favor ingresa el Titulo del libro: ")
        NumPag = int(input("Número de Páginas: "))
        TipoTapa = input("TapaDura (D)/TapaBlanda (B): ")
        URLLibro = input("URL? (S/N): ")
        ISBNLibro = input("ISBN: ")
        print("*****************************************")
        self.DatosLibro(NumPag, Nombre, TipoTapa, URLLibro, ISBNLibro)

    #por aqui Salen los datos it is the output
    def MostrarDatosLibro(self):
        print("*****************************************")
        print("Tamaño= ", self.tamaño)
        print("Paginas= ", self.paginas)
        print("Precio Venta= ", self.precioVenta)
        print("Peso= ", self.peso)
        print("Precio x Pagina= ", self.PrecioXPagina()) 
        print("Peso X Pagina= ", self.PesoXPagina()) 
        print("Titulo= ", self.titulo)
        print("tapa= ", self.tapa)
        print("URL= ", self.URL)
        print("ISBN= ", self.ISBN)
        print("Estado= ", self.Estado)
        print("*****************************************")

Libro1=Libro()
Libro2=Libro()

print("DATOS LIBRO 1")
Libro1.RecibeDatosLibro()

print("DATOS LIBRO 2")
Libro2.RecibeDatosLibro()

Libro1.MostrarDatosLibro()
Libro2.MostrarDatosLibro()