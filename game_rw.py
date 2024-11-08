from gridworld.grid import Grid
import pygame
import random

def draw_car(grid, cell_dimensions):
    grid.screen.blit(myimage, cell_dimensions)

def tick():
    global x, y
    oldx, oldy = x, y
    value = random.random()
    if value < 0.25 and y > 0:
        y = y - 1
    elif value >= 0.25 and value < 0.5 and y < 4:
        y = y + 1
    elif value >= 0.5 and value < 0.75 and x > 0:
        x = x - 1
    elif value >= 0.75 and x < 4:
        x = x + 1
    grid[oldx, oldy] = ''
    grid[x, y] = 'O'

myimage = pygame.image.load("car.png")

maxx = 5
maxy = 5
x = maxx // 2
y = maxy // 2

grid = Grid(maxx, maxy, 90, 90, title='Gridworld', margin=1, framerate=1)
grid.set_drawaction('O', draw_car)

grid.set_timer_action(tick)

grid[2,2] = 'O'
grid.run()



