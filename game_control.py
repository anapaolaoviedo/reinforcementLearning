from gridworld.grid import Grid
import pygame

def key_action(key):
    global x, y
    oldx, oldy = x, y
    if key == pygame.K_LEFT and x > 0:
        x = x - 1
    elif key == pygame.K_RIGHT and x < 4:
        x = x + 1
    elif key == pygame.K_UP and y > 0:
        y = y - 1
    elif key == pygame.K_DOWN and y < 4:
        y = y + 1
    grid[oldx, oldy] = ''
    grid[x, y] = 'O'

myimage = pygame.image.load("car.png")

def draw_car(grid, cell_dimensions):
    grid.screen.blit(myimage, cell_dimensions)

maxx = 5
maxy = 5
x = maxx // 2
y = maxy // 2

grid = Grid(maxx, maxy, 90, 90, title='Gridworld', margin=1)
grid.set_drawaction('O', draw_car)

grid.set_key_action(key_action)

grid[2,2] = 'O'
grid.run()