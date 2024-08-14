#la Veterinaria se requiere 8 caracteristicas max
class ElPerroj():
    Tipo="Perro"
    NombrePerro=""
    Raza=""
    Edad=""
    ColorPelaje=""
    Dueño=""
    Peso=0
    Estado="No Atendido"
    
    def __init__(self):
        self.Tipo="Perro"
        self.Peso=0
    
    def RegistrarPerro(self):
        return print("ATENDIDO :D")
    
    def PesoPerro(self):
        if(self.Peso>10):
            self.PerroGrande=self.Peso
            print(f"Perro Grande su peso es:{self.PerroGrande}")
        else:
            self.PerroPequeño=self.Peso
            print(f"Perro Pequeño{self.PerroPequeño}")
    
    def DatosPerro(ElPerroj,Tipo,NomPer,RazaBand,Edad,ColorPelaje,Dueño,PesoPerro):
        ElPerroj.Tipo=Tipo
        ElPerroj.NombrePerro=NomPer
        ElPerroj.Raza=RazaBand
        ElPerroj.Edad=Edad
        ElPerroj.ColorPelaje=ColorPelaje
        ElPerroj.Dueño=Dueño
        ElPerroj.Peso=PesoPerro()

    def RecibirDatosDelPerro(NomPer,RazaBand,Edad,ColorPelaje,Dueño,PesoPerro):
        print("**************Doctor Chopper****************")
        NomPer=input("Nombre de la Mascota: ")
        RazaBand=input("Que raza es: ")
        Edad=int(input("Cual es la edad: "))
        ColorPelaje=input("El color del Pelaje: ")
        Dueño= input("Su dueño es: ")
        PesoPerro=int(input("Cuanto Pesa en kg: "))
        print("*********************************************")
        ElPerroj.DatosPerro(NomPer,RazaBand,Edad,ColorPelaje,Dueño,PesoPerro)
    
    def MostrarDatosPerro(self):
        print("**********************************************")
        print("El Nombre del perro es: ",self.NombrePerro)
        print("Raza del canino: ",self.Raza)
        print("Edad del perro es: ",self.Edad)
        print("Color del Pelaje: ",self.ColorPelaje)
        print("El Dueño o encargado es: ",self.Dueño)
        print("Peso del perro es: ",self.PesoPerro())
        print("*****************************************")

perro1=ElPerroj()

print("*****************************************")
print("DatosPerro")
perro1.RecibirDatosDelPerro
print("*****************************************")
perro1.MostrarDatosPerro
print("*****************************************")


