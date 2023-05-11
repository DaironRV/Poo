#cuerpos celestes

class cuerposCelestes:
    
    tipo_de_cuerpo = "planeta" 
    
    def __init__(self, tamaño, volumen, compocisión, habitado, nombre):
        self.__nombre = nombre
        self.tamaño = tamaño
        self.volumen = volumen
        self.compocisión = compocisión
        self.__habitado = habitado
    
    def get__habitado(self):
        return self.__habitado
    
    def get__nombre(self):
        return self.__nombre
    
    def cuerpo(self):
        print( "el tamaño del cuerpo es:" + self.tamaño)
        print("el volumen es:" + self.volumen)
        print("Essta compuesto por" + self.compocisión)
        print ("tipo de cuerpo celeste:" + self.tipo_de_cuerpo)

class cuerpoCeleste2 (cuerposCelestes):
    
    tipo_de_cuerpo = "Cometa"
    
    def __init__(self, tamaño, volumen, compocisión, habitado, nombre, velocidad, color):
        
        self.velocidad = velocidad
        self.color = color
        
        super().__init__(tamaño, volumen, compocisión, habitado, nombre)
        
    def cuerpo(self):
        
        print("el color es :" + self.color)
        print("su velocidad es: " + self.velocidad)
        
        return super().cuerpo()

class satelite (cuerpoCeleste2):
    
    tipo_de_cuerpo = "meteoritos"


class cuerpoBrilla  (cuerposCelestes): 
    
    tipo_de_cuerpo= "sol/estrella"
    
    def __init__(self, tamaño, volumen, compocisión, habitado, nombre, fuerza):
        
        self.fuerza = fuerza
        
        super().__init__(tamaño, volumen, compocisión, habitado, nombre)
        
    def cuerpo(self):
        
        print("la fuerza de garbedad que este ejerse es: " + self.fuerza)
        
        return super().cuerpo()

class galaxia (cuerposCelestes): 
    
    tipo_de_cuerpo = "galaxia"
    
    def __init__(self, tamaño, volumen, compocisión, habitado, nombre, gusto, porqueG):
        
        self.gusto = gusto 
        self.porqueG = porqueG
        
        super().__init__(tamaño, volumen, compocisión, habitado, nombre)


tierra = cuerposCelestes ("6,371 km", "aproximadamente 1 billón o 1.000.000.000.000 millones de kilómetros cúbicos", "minerales, lava, líquidos y compuestos volátiles","este planeta esta habitado", "tierra" )
tierra.cuerpo()
print(tierra.__nombre())
print(tierra.__habitado())


print("==================================================================================================================")

cometa = cuerpoCeleste2 ("el voluen de un cometa es dependiendo", "10 kl de diametro", "agua, hielo seco, amoníaco, metano, hierro, magnesio, sodio y silicatos", "no esta habitado", "El Cometa Borrelly", "10 y 70 kilómetros por segundo", "azules natralmete")

cometa.cuerpo()
print(cometa.__nombre())
print(cometa.__habitado())

print("==================================================================================================================")

meteorito = satelite ("entre 0.1 mm y 50 m" , "entre 3 y 8 g/cm3", "FERROSOS: se componen de 90 porciento hierro, 9% niquel, y un 1 porciento de otros elementos", "no esta habitado", "Otjozondjupa", " 20-25 km/s", "su color puede ser Morado si es mayor parte de hierro")

meteorito.cuerpo()
print(meteorito.__nombre)
print(meteorito.__habitado)

print("==================================================================================================================")

sol = cuerpoBrilla ("696,340 km", " 1,4123 x 10^18 km³", "71 porciento de Hidrógeno, un 27% Helio, y un 2 porciento de otros elementos más pesados", "274 m/s²", "quien viviria en el sol ._., un costeño talvez")

sol.cuerpo()
print (sol.__habitado)
print (sol.__nombre)

print("==================================================================================================================")

