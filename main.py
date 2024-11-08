from enum import Enum
from gridworld.grid import Grid
import pygame
import random

while True:
    print("!!!!!GAAAAMEEEE TIIIMEEEEE!!!!!")
    print("\n GAME N1: \n En este juego hay una probabilidad de 25% de ir a cualquier lado ")
    print("\n GAME N2: \n En este juego solo hay probabilidad especifica del movimiento \n")
    print("\n Para el GAME 1 introduce 1\n")
    print("\n Para el GAME 2 introduce 2\n")
    tipoDeJuego = int(input("INTRODUCE EL NUMERO DE JUEGO QUE QUIERES JUGAR: "))
    
    if (tipoDeJuego == 1 or tipoDeJuego == 2): 
        break

maxX = 4
maxY = 3


x = int(input(f"INGRESA donde quieres posicionar X (entre 0 y {maxX - 1}): "))
y = int(input(f"INGRESA donde quieres posicionar Y (entre 0 y {maxY - 1}): "))

#pero para verificar si el rango introducido es valido 
if x < 0 or x >= maxX or y < 0 or y >= maxY:
    print("COORDENADAS fuera del rango establecido.")
    exit()

grid = Grid(maxX, maxY, 90, 90, title='Tic Tac Toe', margin=1, framerate=2)

class Dir(Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

transitionJuego1 = {
    (0, 1): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (0, 2): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (1, 0): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (1, 1): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (1, 2): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (2, 0): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (2, 1): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (2, 2): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (3, 0): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (3, 2): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
}
transitionJuego2 = {
    (0, 1): {Dir.UP: 1.0, Dir.DOWN: 0.0, Dir.LEFT: 0.0, Dir.RIGHT: 0.0},
    (0, 2): {Dir.UP: 1.0, Dir.DOWN: 0.0, Dir.LEFT: 0.0, Dir.RIGHT: 0.0},
    (1, 0): {Dir.UP: 0, Dir.DOWN: 0.0, Dir.LEFT: 1, Dir.RIGHT: 0},
    (1, 1): {Dir.UP: 0.33, Dir.DOWN: 0.0, Dir.LEFT: 0.34, Dir.RIGHT: 0.33},
    (1, 2): {Dir.UP: 0.33, Dir.DOWN: 0.0, Dir.LEFT: 0.34, Dir.RIGHT: 0.33},
    (2, 0): {Dir.UP: 0, Dir.DOWN: 0.33, Dir.LEFT: 0.34, Dir.RIGHT: 0.33},
    (2, 1): {Dir.UP: 0.0, Dir.DOWN: 0.0, Dir.LEFT: 0.0, Dir.RIGHT: 1.0},
    (2, 2): {Dir.UP: 0.5, Dir.DOWN: 0.0, Dir.LEFT: 0.0, Dir.RIGHT: 0.5},
    (3, 0): {Dir.UP: 0.0, Dir.DOWN: 1.0, Dir.LEFT: 0.0, Dir.RIGHT: 0.0},
    (3, 2): {Dir.UP: 1.0, Dir.DOWN: 0.0, Dir.LEFT: 0.0, Dir.RIGHT: 0.0},
}

trans = {}

if tipoDeJuego == 1:
    trans = transitionJuego1
else:
    trans = transitionJuego2

#posicionando la carita acorde las coordenadas del usuario
grid[x, y] = ':)'

def tick():
    global x, y
    oldx, oldy = x, y

    current_probs = trans[(x, y)]
    value = random.random()

    if value < current_probs[Dir.UP]:
        if y > 0:
            y -= 1
    elif value < current_probs[Dir.UP] + current_probs[Dir.DOWN]:
        if y < maxY - 1:
            y += 1
    elif value < current_probs[Dir.UP] + current_probs[Dir.DOWN] + current_probs[Dir.LEFT]:
        if x > 0:
            x -= 1
    else:
        if x < maxX - 1:
            x += 1

    grid[oldx, oldy] = ''
    grid[x, y] = ':)'

    if (x, y) == (0, 0) or (x, y) == (3, 1):
        print("GAMEEE OVERRRR")
        pygame.quit()
        exit()


grid.set_timer_action(tick)

grid.run()
