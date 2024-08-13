class Libro():
    tamaño=""
    paginas=0
    precioVenta=0
    precioXPag=0
    pesoXPag=0
    titulo=""
    tapa=""
    URL=""
    ISBN=""
    Estado="No Hay Registros del Libro"
    #holaZapata estuvo aqui
    def __init__(self):
        self.tamaño="17x24"
        self.precioXPag=300
        self.pesoXPag=0.8

    def RegistraLibro(self):
        Estado="Registrado"
        return Estado