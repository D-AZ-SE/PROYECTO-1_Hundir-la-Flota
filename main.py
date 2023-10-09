### main.py
from funciones import *
from variables import *
import random


# Inicio del juego

# Fuera del "while", bienvenida y y preguntar al jugador por el modo de disparo
print("¡Bienvenido al juego de HUNDIR LA FLOTA!")
time.sleep(1)
nombre = input("Por favor, introduce tu nombre: ")
time.sleep(1)
print(f"{nombre}, los barcos han sido aleatoriamente colocados tanto para ti como para la máquina. Comienza el juego...")
time.sleep(1)
modo_disparo = input("¿Cómo quieres elegir tus disparos, de forma 'manual' o 'aleatoria'?: ").lower()

turno_maquina = False

while not fin_del_juego(tablero_jugador, tablero_maquina):
    if turno_maquina:
        # Turno de la máquina
        print("Turno de la Máquina:")
        fila, columna = disparo_maquina(tablero_jugador)

        print(f"La Máquina dispara a la coordenada ({fila}, {columna}):")  # Muestra las coordenadas del disparo
        if tablero_jugador[fila][columna] == "B":
            print("¡La Máquina ha acertado en uno de tus barcos.")
            tablero_jugador[fila][columna] = "X"
            vidas_jugador -= 1
            if vidas_jugador == 0:
                print("La Máquina ganó! Ha hundido todos tus barcos.")
                break
        else:
            print("La Máquina ha fallado.")
            disparos_jugador[fila][columna] = "o"  # Registrar disparo fallado del jugador
    else:
        # Turno del jugador
        print("Turno del Jugador:")
        visualizar_tableros(tablero_jugador, tablero_maquina_barcos_oc, disparos_maquina, disparos_jugador, turno_maquina)
        opcion_disparo = modo_disparo

        if opcion_disparo == "manual":
            print("Turno de disparo manual del Jugador:")
            fila, columna = disparo_jugador(tablero_jugador, modo_disparo, tablero_maquina_barcos_oc)
        else:
            print("Turno de disparo aleatorio del Jugador:")
            fila, columna = disparo_jugador(tablero_jugador, modo_disparo, tablero_maquina_barcos_oc)

        print(f"Has disparado a la coordenada ({fila}, {columna}):")  # Muestra las coordenadas del disparo

        if tablero_maquina[fila][columna] == "B":
            print("¡Has acertado en un barco!")
            tablero_maquina[fila][columna] = "X"
            disparos_maquina[fila][columna] = "X"  # Registrar disparo en el tablero de la máquina
            vidas_maquina -= 1
            if vidas_maquina == 0:
                print("¡GANASTE! Has hundido todos los barcos de la Máquina.")
                break
        else:
            print("Has fallado.")
            tablero_maquina_barcos_oc[fila][columna] = "o"  # Registrar disparo fallado en el tablero de la máquina oculta

    turno_maquina = not turno_maquina

if vidas_jugador == 0:
    print("No te quedan más vidas, victoria para la Máquina. Tendrá que ser otra vez...")
    pass


    