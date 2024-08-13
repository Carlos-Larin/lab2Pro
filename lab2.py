class Libro():
    tamaño=""
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

    def __init__(self):
        self.tamaño="17x24"
        self.precioXPag=300
        self.pesoXPag=0.8

    def RegistraLibro(self):
        Estado="Registrado"
        return Estado
    
    def DatosLibro(Libro,NumPag,Nombre,TipoTapa,URLLibro,ISBNLibro):
        Libro.paginas=NumPag
        Libro.precioVenta=Libro.precioXPag()*NumPag
        Libro.peso=Libro.pesoXPag()*NumPag
        Libro.titulo=Nombre
        Libro.tapa=TipoTapa
        Libro.URL=URLLibro
        Libro.ISBN=ISBNLibro

    def PrecioXPagina(self):
        return  self.precioXPag
    
    def PesoXPagina(self):
        return  self.pesoXPag
    
    def RecibirDatosLibro(Libro):
        Nombre=input("Hola porfavor inrgresa el Titulo del libro: ")
        NumPag=int(input("Numero de Paginas: "))
        TipoTapa=input("TapaDura (D)/TapaBlanda (B): ")
        URLLibro = input("URL? (S/N): ")
        ISBNLibro=input("ISBN: ")
        print("*****************************************")
        DatosLibro(Libro,NumPag,Nombre,TipoTapa,URLLibro,ISBNLibro)




    def MostrarDatosLibro(Libro):
        print("Tamaño= ",Libro.tamaño)
        print("Paginas= ",Libro.paginas)
        print("Precio Venta= ",Libro.precioVenta)
        print("Peso= ",Libro.peso)
        print("Precio x Pagina= ",Libro.PrecioXPagina)
        print("Peso X Pagina= ",Libro.PesoXPagina)
        print("Titulo= ",Libro.titulo)
        print("tapa= ",Libro.tapa)
        print("URL= ",Libro.URL)
        print("ISBN= ",Libro.ISBN)
        print("Estado= ",Libro.Estado)  
