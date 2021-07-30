#               Tic Tac Toe
#              by @notalion

# Reglas:
# Dos jugadores
# Cada uno toma un turno y en cada seccion se pone [X | O]
# 
# Se gana cuando se logra un tres en linea
# 

#       Variables

jugador = 'X'

Tablero = { 'Top-I':'1', 'Top-M':'2', 'Top-D':'3', 
            'Mid-I':'4', 'Mid-M':'5', 'Mid-D':'6',
            'Low-I':'7', 'Low-M':'8', 'Low-D':'9'}

#       Funciones

def statusTablero(Tablero):     # Mostrar el tablero
    print('-------')
    print(Tablero['Top-I'] + ' | ' + Tablero['Top-M'] + ' | ' + Tablero['Top-D']  )
    print('-------')
    print(Tablero['Mid-I'] + ' | ' + Tablero['Mid-M'] + ' | ' + Tablero['Mid-D']  )
    print('-------')
    print(Tablero['Low-I'] + ' | ' + Tablero['Low-M'] + ' | ' + Tablero['Low-D']  )
    print('-------')

def statusVictoria(Tablero):    # Revisar la victoria
    if Tablero['Top-I'] == Tablero['Top-M'] and Tablero['Top-M'] == Tablero['Top-D']:   # 1|2|3 Horizontal
        return True
    elif Tablero['Mid-I'] == Tablero['Mid-M'] and Tablero['Mid-M'] == Tablero['Mid-D']: # 4|5|6 Horizontal
        return True
    elif Tablero['Low-I'] == Tablero['Low-M'] and Tablero['Low-M'] == Tablero['Low-D']: # 7|8|9 Horizontal
        return True
    elif Tablero['Top-I'] == Tablero['Mid-M'] and Tablero['Mid-M'] == Tablero['Low-D']: # 1|5|9 Diagonal
        return True
    elif Tablero['Top-D'] == Tablero['Mid-M'] and Tablero['Mid-M'] == Tablero['Low-I']: # 3|5|7 Diagonal
        return True  
    elif Tablero['Top-I'] == Tablero['Mid-I'] and Tablero['Mid-I'] == Tablero['Low-I']: # 1|4|7 Vertical
        return True
    elif Tablero['Top-M'] == Tablero['Mid-M'] and Tablero['Mid-M'] == Tablero['Top-M']: # 2|5|8 Vertical
        return True
    elif Tablero['Top-D'] == Tablero['Mid-D'] and Tablero['Mid-D'] == Tablero['Top-D']: # 3|6|9 Vertical
        return True
    else:
        return False
        
def agregarJugada(Tablero,respuesta,jugador):    # Tomar casilla por jugador
    if respuesta == '1':
        Tablero['Top-I'] = jugador   
    elif respuesta == '2':
        Tablero['Top-M'] = jugador
    elif respuesta == '3':
        Tablero['Top-D'] = jugador
    elif respuesta == '4':
        Tablero['Mid-I'] = jugador    
    elif respuesta == '5':
        Tablero['Mid-M'] = jugador
    elif respuesta == '6':
        Tablero['Mid-D'] = jugador
    elif respuesta == '7':
        Tablero['Low-I'] = jugador  
    elif respuesta == '8':
        Tablero['Low-M'] = jugador
    elif respuesta == '9':
        Tablero['Low-D'] = jugador
    else:
        print("Error, opcion no valida")

def juego(Tablero,jugador):   # Comienza el juego
    for turnos in range (1,10):
        print(statusTablero(Tablero))
        print("Inicia jugador: " + str(jugador))
        respuesta = input()
        print()
        print('Se eligio ' + respuesta)
        agregarJugada(Tablero,respuesta,jugador)        
        print(statusTablero(Tablero))
        if statusVictoria(Tablero) == True:
            print("Victoria")
            print("El ganador es el jugador " + str(jugador))
            print("Turnos tomados: " + str(turnos))
            break
        if jugador == 'X':
            jugador = '0'
        else:
            jugador = 'X'
    print("Empate, todos pierden")


# Codigo Principal
def main():
    global Tablero
    global jugador
    print('''          REGLAS:
        Cada cuadrado esta marcado con un codigo para seleccionar la casilla que quieres a tomar 
        escribe el acronimo mostrado ej. "TM" y se tomara para el jugador que eligio

        Se gana cuando tres casillas juntas tienen el mismo simbolo.

        ¿Estan listos?
    ''')

    juego(Tablero,jugador)

main()