### funciones.py
from variables import *
import random

# Función para verificar si se puede colocar un barco en una posición dada
def verificar_colocacion(tablero, longitud, fila, columna, orientacion):
    if orientacion == "N":
        if fila - longitud < 0:
            return False
        for i in range(longitud):
            if tablero[fila - i][columna] != "~":
                return False
    elif orientacion == "S":
        if fila + longitud > len(tablero) - 1:
            return False
        for i in range(longitud):
            if tablero[fila + i][columna] != "~":
                return False
    elif orientacion == "E":
        if columna + longitud > len(tablero[0]) - 1:
            return False
        for i in range(longitud):
            if tablero[fila][columna + i] != "~":
                return False
    elif orientacion == "O":
        if columna - longitud < 0:
            return False
        for i in range(longitud):
            if tablero[fila][columna - i] != "~":
                return False
    return True

# Función para colocar un barco en el tablero
def colocar_barco(tablero, longitud, fila, columna, orientacion):
    if orientacion == "N":
        for i in range(longitud):
            tablero[fila - i][columna] = "B"
    elif orientacion == "S":
        for i in range(longitud):
            tablero[fila + i][columna] = "B"
    elif orientacion == "E":
        for i in range(longitud):
            tablero[fila][columna + i] = "B"
    elif orientacion == "O":
        for i in range(longitud):
            tablero[fila][columna - i] = "B"

# Función para colocar barcos aleatoriamente en el tablero
def colocar_barcos_aleatorios(tablero, barcos):
    for barco, longitud in barcos.items():
        while True:
            fila = random.randint(0, len(tablero) - 1)
            columna = random.randint(0, len(tablero[0]) - 1)
            orientacion = random.choice(["N", "S", "E", "O"])
            if verificar_colocacion(tablero, longitud, fila, columna, orientacion):
                colocar_barco(tablero, longitud, fila, columna, orientacion)
                break

colocar_barcos_aleatorios(tablero_jugador, barcos)
colocar_barcos_aleatorios(tablero_maquina, barcos)

# Función para realizar un disparo aleatorio por la máquina
def disparo_maquina(tablero):
    fila = random.randint(0, len(tablero) - 1)
    columna = random.randint(0, len(tablero[0]) - 1)
    return fila, columna

def disparo_jugador(tablero, modo_disparo, tablero_maquina_barcos_oc):
    if modo_disparo == "manual":
        while True:
            try:
                fila = int(input("Ingresa la fila: "))
                columna = int(input("Ingresa la columna: "))
                if 0 <= fila < len(tablero) and 0 <= columna < len(tablero[0]) and tablero[fila][columna] == "~":
                    return fila, columna
                else:
                    print("Posición inválida o ya disparada. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada inválida. Debes ingresar números enteros.")
    elif modo_disparo == "aleatorio":
        fila = random.randint(0, len(tablero) - 1)
        columna = random.randint(0, len(tablero[0]) - 1)
        return fila, columna
    else:
        print("Opción no válida. Se realizará un disparo aleatorio.")
        fila = random.randint(0, len(tablero) - 1)
        columna = random.randint(0, len(tablero[0]) - 1)
        return fila, columna

# Función para visualizar los tableros del jugador y la máquina oculta
def visualizar_tableros(tablero_jugador, tablero_maquina_barcos_oc, disparos_maquina, disparos_jugador, turno_maquina=False):
    print("Tablero del Jugador:")
    for i in range(len(tablero_jugador)):
        fila_mostrada = ["X" if c == "B" else c for c in tablero_jugador[i]]
        for j in range(len(fila_mostrada)):
            if disparos_jugador[i][j] == "o":
                fila_mostrada[j] = "o"
        print(" ".join(fila_mostrada))

    if not turno_maquina:
        print("\nTablero de la Máquina (Oculto):")
        for i in range(len(tablero_maquina_barcos_oc)):
            fila_mostrada = ["~" if c == "B" else c for c in tablero_maquina_barcos_oc[i]]
            for j in range(len(fila_mostrada)):
                if disparos_maquina[i][j] == "X":
                    fila_mostrada[j] = "X"
                elif disparos_maquina[i][j] == "o":
                    fila_mostrada[j] = "o"
            print(" ".join(fila_mostrada))

# Función para verificar el fin del juego
def fin_del_juego(jugador, maquina):
    return all(c == "~" for fila in jugador for c in fila) or all(c == "~" for fila in maquina for c in fila)