#Animales
class mamiferos: 
    dieta = "Los gatos salvajes son depredadores naturales, su dieta se vaza en, aves, roedores pequeños, peces y reptiles pequeños"
    no_recuedo_como_se_llama_esto = "felinos"
    
    def __init__(self,peso, altura, alias): 
        self.peso =  peso
        self.altura = altura
        self.__alias = alias
    
    def get_alias(self):
        return self.__alias 
    
    def Muestra_datos (self): 
        print ("el peso promedio es:" + str (self.peso) + "kg")
        print ("su altura promedio es: " + str (self.altura) + "cm" )
        print (self.dieta)
        print (self.no_recuedo_como_se_llama_esto)


class mamiferos2(mamiferos):
    dieta = "Los perros salvajes como tal no existen, solo serian perro comun menteconosidos como callegeros, su alimentanción es solo lo que encunentren"
    no_recuedo_como_se_llama_esto = "caninos/Canidae"

Gato = mamiferos ( "4 a 5", 25, "MuchiFus Devorador de almas y de WHISKAS")
Gato.Muestra_datos()
print(Gato.get_alias())

print("====================================================================================================================================================")

Perro = mamiferos2  ( 110, 110, "Doom cazador de demonios maestro de las mordidas")
Perro.Muestra_datos()
print(Perro.get_alias())