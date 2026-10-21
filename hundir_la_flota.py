import numpy as np
import random


#aqui creo un tablero con  "_"
def crear_tablero(size=10):
    return np.full((size, size), "_")


# Aqui muestro el tablero
def mostrar_tablero(tablero, titulo):
    print()
    print(titulo)
    print("   ", end="")
    for numero in range(len(tablero)):
        print(numero, end="  ")
    print()
    for numero in range(len(tablero)):
        print(numero, end="  ")
        for casilla in tablero[numero]:
            print(casilla, end="  ")
        print()


# Colocar un barco en el jeugo
def colocar_barco(barco, tablero):
    for casilla in barco:
        fila, col = casilla
        tablero[fila, col] = "O"


# Disparara a un barco
def disparar(casilla, tablero):
    fila, col = casilla
    if tablero[fila, col] == "O":
        tablero[fila, col] = "X"
        print("¡Tocado!")
    elif tablero[fila, col] == "_":
        tablero[fila, col] = "A"
        print("Agua")
    else:
        print("Ya habías disparado ahí")


# Que se cree un barco random que quepa en el board
def crear_barco(eslora, size=10):
    while True:
        fila = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        orientacion = random.choice(["N", "S", "E", "O"])

        barco = []
        for i in range(eslora):
            if orientacion == "N":
                barco.append((fila - i, col))
            elif orientacion == "S":
                barco.append((fila + i, col))
            elif orientacion == "E":
                barco.append((fila, col + i))
            else:
                barco.append((fila, col - i))

        dentro = True
        for f, c in barco:
            if f < 0 or f >= size or c < 0 or c >= size:
                dentro = False

        if dentro:
            return barco


#colocar todos los barcos
def colocar_barcos(tablero):
    esloras = [2, 2, 2, 3, 3, 4]
    for eslora in esloras:
        while True:
            barco = crear_barco(eslora, len(tablero))
            libre = True
            for fila, col in barco:
                if tablero[fila, col] != "_":
                    libre = False
            if libre:
                colocar_barco(barco, tablero)
                break


#juego
size = 10
tablero_jugador = crear_tablero(size)
tablero_maquina = crear_tablero(size)
disparos_jugador = crear_tablero(size)
disparos_maquina = crear_tablero(size)
colocar_barcos(tablero_jugador)
colocar_barcos(tablero_maquina)

while True:
    mostrar_tablero(tablero_jugador, "mi TABLERO")
    mostrar_tablero(disparos_jugador, "mis DISPAROS")

    # mi  turno
    print("mi TURNO")
    while True:
        fila = int(input("Fila: "))
        col = int(input("Columna: "))
        if 0 <= fila < size and 0 <= col < size:
            break
        print("Esa casilla esta fuera del tablero")
    disparar((fila, col), tablero_maquina)
    disparos_jugador[fila, col] = tablero_maquina[fila, col]
    if "O" not in tablero_maquina:
        print("Has hundido toda la flota")
        break

    # ordenador 
    print("TURNO ordenador")
    while True:
        fila = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if disparos_maquina[fila, col] == "_":
            break
    print(f"La máquina dispara a ({fila}, {col})")
    disparar((fila, col), tablero_jugador)
    disparos_maquina[fila, col] = tablero_jugador[fila, col]
    if "O" not in tablero_jugador:
        print("La máquina ha hundido tu flota")
        break
    
        
