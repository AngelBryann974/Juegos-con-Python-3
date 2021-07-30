#        Ahorcado
#       by @notalion

#        Reglas:
#  Se muestra un tanto 
# Si dentro de la frase a adivinar hay números hay que comunicarlo con anterioridad. 
# Si finalmente el jugador que ha de adivinar la palabra pierde y descubre que la frase 
# contenía número y no se le advirtió gana automáticamente.
# se suele prohibir el uso de nombres y apellidos como palabras a adivinar, al igual que las palabras en otros idiomas
# 
# Si el jugador ha preguntado por una letra (por ejemplo la M) y el otro jugador no se da cuenta que la palabra contiene la M 
# y lo marca como error al finalizar y descubrirse que si la contenía perderá el juego.
# 
# Si el jugador del ahorcado que tiene que adivinar la palabra repite dos veces una letra no se le marcaran dos fallos, 
# sino que simplemente se le indicara que ya estaba dicha esta letra.
#

# Modulos

import random

# Variables

palabras = ['Gato', 'Perro', 'Oso', 'Gallina','Ornitorinco', 'Toro', 'Paloma', 'Tortuga', 'Perico']                  # Diccionario con todas las posibles respuestas
Respuesta = str.lower(palabras[random.randint(0,len(palabras))])            # Seleccionar la palabra
Secreto = []                                             
limite = int(len(Respuesta) + 3)                                # Limite de intentos es el num de letras de la palabra + 3

# Metodos

def asignarRespuesta(Respuesta,Secreto):                        # Agregar la respuesta al tablero para mostrar
    for i in range (0, len(Respuesta)):
        Secreto.append('X')

    print('La palabra secreta es: ')
    print(list(Secreto))

def juegoInicia(Respuesta,Secreto,limite):
    for intentos in range (1, limite):
        print('Cual es la letra que quieres usar?')             # Aqui recoge la letra del usuario
        letra = str.lower(input())
        for i in range (0, len(Respuesta)) :
            if letra == Respuesta[i]:
                Secreto[i] = letra
                if list(Secreto) == list(Respuesta):
                    print('''
                           _.+._
                         (^\/^\/^)
                          \@*@*@/
                          {_____}
                    ''')
                    print("                         Victoria")
                    print("                  La palabra era " + str(Respuesta))
                    print("                  Intentos restantes: " + str(limite - intentos - 1))
                    quit()
            else:
                pass
        print(list(Secreto))
        print("Quedan : " + str(limite - intentos - 1) + " intentos !" )
    
    print('''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      | |
     |
    _|___
    ''')
    print("                  Buuuu")
    print("                  La palabra era " + str(Respuesta))


# Programa principal
def main():
    global Respuesta
    global Secreto
    global limite
    asignarRespuesta(Respuesta,Secreto)
    juegoInicia(Respuesta,Secreto,limite)

main()
