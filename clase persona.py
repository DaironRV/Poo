class persona:
    Genero = "Mujer"
    compras = "Bastantes"
    
    def __init__(self, peso, estatura, edad, empleo):
        self.peso = peso 
        self.estatura = estatura
        self.edad = edad 
        self.empleo = empleo

    def muestra_Datos(self):
        print("el peso de la persona es: " + str(self.peso))
        print("la estatura de la persona es: " + str (self.estatura))
        print("esta persona tien: " + str (self.edad) + " años de edad")
        print("su trabajo es: "+ self.empleo)
        print("su genero es: " + self.Genero)
        print("sus compras echas este año fueron: " + self.compras)

class persona2 (persona):
    compras = "Pocas"
    Genero = "Hombre"

Maria = persona (61, 1.70, 22, "una empresa")
Maria.muestra_Datos()

print("===========================================")

Carlos = persona2 (81, 1.80, 23, "en un call center")
Carlos.muestra_Datos()
