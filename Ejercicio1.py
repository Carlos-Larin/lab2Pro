#aqui inicie la clase 
class ElPerroj():
    Tipo = "Perro"
    NombrePerro = ""
    Raza = ""
    Edad = 0
    ColorPelaje = ""
    Dueño = ""
    Peso = 0
    Estado = "No Atendido"
    
    def __init__(self):
        self.Tipo = "Perro"
        self.Peso = 0
    
    def RegistrarPerro(self):
        self.Estado = "Atendido"
        print("ATENDIDO :D")
#usare esta parte para ver cuando sea grande o pequeño   
    def PesoPerro(self):
        if self.Peso > 10:
            print(f"Perro Grande su peso es: {self.Peso} kg")
        else:
            print(f"Perro Pequeño su peso es: {self.Peso} kg")
    
    def DatosPerro(self, Tipo, NomPer, RazaBand, Edad, ColorPelaje, Dueño, PesoPerro,Estado):
        self.Tipo = Tipo
        self.NombrePerro = NomPer
        self.Raza = RazaBand
        self.Edad = Edad
        self.ColorPelaje = ColorPelaje
        self.Dueño = Dueño
        self.Peso = PesoPerro
        self.Estado=Estado
#aqui es donde el usuario ingresa los datos de la mascota
    def RecibirDatosDelPerro(self):
        print("**************Doctor Chopper****************")
        NomPer = input("Nombre de la Mascota: ")
        RazaBand = input("¿Qué raza es?: ")
        Edad = int(input("¿Cuál es la edad?: "))
        ColorPelaje = input("¿Cuál es el color del pelaje?: ")
        Dueño = input("¿Quién es su dueño?: ")
        PesoPerro = int(input("¿Cuánto pesa en kg?: "))
        Estado=input("El perro ya Fue atendido? (S/N): ").lower()
        print("*********************************************")
        self.DatosPerro("Perro", NomPer, RazaBand, Edad, ColorPelaje, Dueño, PesoPerro,Estado)
#aqui el usuario se le mostraran los datos en consola   
    def MostrarDatosPerro(self):
        print("**************Doctor Chopper****************")
        print("El Nombre del perro es: ", self.NombrePerro)
        print("Raza del canino: ", self.Raza)
        print("Edad del perro es: ", self.Edad)
        print("Color del Pelaje: ", self.ColorPelaje)
        print("El Dueño o encargado es: ", self.Dueño)
        print("Peso del perro es: ", self.Peso, "kg")
        if self.Peso > 10:
            print("Este es un perro grande.")
        else:
            print("Este es un perro pequeño.")
        print("Estado: ", self.Estado)
        if self.Estado=="s":
            print("Su estado es Atendido.")
        else:
            print("Aun no fue atendido D:")

# Creación de una instancia de ElPerroj
perro1 = ElPerroj()
print("**************Doctor Chopper****************")
print("Datos del Perro")
print("*****************************************")
perro1.RecibirDatosDelPerro() 
perro1.MostrarDatosPerro() 
print("*****************************************")

