
class BasoPromedio: 
    Agua_Leche = "Agua"
    Azucar = "Tiene azucar"
    
    def __init__(self, Vaso , Tamaño_bebida, Gusto, Quien):
        self.Vaso = Vaso
        self.Tamaño_bebida = Tamaño_bebida
        self.Gusto = Gusto
        self.__Quien = Quien
    
    def get__Quien(self):
        return self.__Quien
    
    def MuestraDatos(self): 
        print("El tamaño del vaso es: " + str(self.Vaso) + "c2" )
        print("El tamaño de la bebida: " + self.Tamaño_bebida )
        print("A la persona que lo bebbio le: "+ self.Gusto )
        print(self.Agua_Leche)
        print(self.Azucar)


class BasoPromedio2(BasoPromedio):
    Agua_Leche = "Leche"
    Azucar = "No Tiene Azucar"

class Jarra(BasoPromedio2): 
    Agua_Leche = "Agua"
    Azucar = "no"
    
    def __init__(self, Vaso , Tamaño_bebida, Gusto, Quien, color, Agarradera):
        self.color = color
        self.Agarradera = Agarradera
        super().__init__(Vaso , Tamaño_bebida, Gusto, Quien)
    
    def MuestraDatos(self):
        print("El color de la jarra es: " + self.color)
        print("Esta jarra tieno o no Agarradera: " + self.Agarradera)
        
        return super().MuestraDatos()


Maria = BasoPromedio(200, "mediano", "le gusto la bebida", "Maria")
Maria.MuestraDatos()
print(Maria.get__Quien())

print("=====================================================================")

Jose = BasoPromedio2(400, "grande", "No le gusto tanto", "Jose")
Jose.MuestraDatos()
print(Jose.get__Quien())

print("=====================================================================")

Alejo = Jarra(1005.31, "Enorme", "le encato, pero no se la termino de tomar", "Alejo", "blanca", "si")
Alejo.MuestraDatos()
print(Alejo.get__Quien())

print("=====================================================================")

print("Fin del programa")