### variables.py
import random
import time


# Configuración inicial del juego
filas = 10
columnas = 10

barcos = {
    "Barco1": 4,
    "Barco2": 3,
    "Barco3": 3,
    "Barco4": 2,
    "Barco5": 2,
    "Barco6": 2,
    "Barco7": 1,
    "Barco8": 1,
    "Barco9": 1,
    "Barco10": 1
}

vidas_jugador = len(barcos)
vidas_maquina = len(barcos)

# Función para crear un tablero vacío
def crear_tablero(filas, columnas):
    tablero = []
    for _ in range(filas):
        fila = ["~"] * columnas
        tablero.append(fila)
    return tablero


tablero_jugador = crear_tablero(filas, columnas)
tablero_maquina_barcos_oc = crear_tablero(filas, columnas)
tablero_maquina = crear_tablero(filas, columnas)

# Agregar una lista para registrar los disparos realizados
disparos_jugador = crear_tablero(filas, columnas)
disparos_maquina = crear_tablero(filas, columnas)