class Persona:
    Conversacion = "Soy tu mayor fan, he escuchado tu obra completa, tengo un póster tuyo en mi cuarto y porto tu camiseta. Pero quiero ver tu rostro, eso es lo único que me inquieta ¿Cuándo vas a dar la cara y quitarte la careta?"
    
    def __init__(self, quien, que_es, hace):
        self.__quien = quien
        self.__que_es = que_es
        self.hace = hace
    
    def get_quien(self):
        return self.__quien
    
    def get_que_es(self):
        return self.__que_es
    
    def texto(self):
        print(self.Conversacion)


class Solitario(Persona):
    Conversacion = "Ni aunque vieras hasta ver morir el universo, comprenderías al fin que mi único anverso es el verso. Entiendo que converso pues con un falso converso, que es estúpido o perverso pues pregunta por lo inverso."


class AlterEgo(Persona):
    def __init__(self, tono, quien, que_es, hace):
        self.tono = tono
        super().__init__(quien, que_es, hace)

    Conversacion = [
        "Aquello que defiendo ¿por qué no te me vas yendo? ¿No ves que no estás entendiendo lo que estás oyendo? Quien me escucha de verdad está leyendo y quienes buscan ver mi rostro nunca me acabarán viendo.",
        "Que lástima me dan que esos borregos prefieran antes un videoclip por mi parte que otra gran obra de arte.",
        "Por enésima vez lamento ser decepcionante: Se equivocaron si lo que buscaban fue un farsante.",
        "Así que esas sugerencias mejor te las ahorras, ni harto de vino comparto reparto con esas zorras, os falta paladar para saborear mis obras.",
        "Porque al cerdo le sabe mejor la comida que las sobras."
    ]

    def texto(self):
        print(self.Conversacion[self.tono])
        
        return super().Conversacion 


persona = Persona("Persona", "es un fan", "Hace una pregunta")
print(persona.get_quien())
print(persona.get_que_es())
print(persona.hace)
persona.texto()

print("===================================================================================================")

solitario = Solitario("persona", "El artista", "responde al fan")
print(solitario.get_quien())
print(solitario.get_que_es())
print(solitario.hace)
solitario.texto()

print("===================================================================================================")

alter_ego = AlterEgo( "agresivo", "Ente sub jetivo imaginario", "El artista", "Dice lo que piensa el artista sin tapujos")
print(alter_ego.get_quien())
print(alter_ego.get_que_es())
print(alter_ego.hace)
alter_ego.texto()

print("la cancion es:Solitario - Entrevista")