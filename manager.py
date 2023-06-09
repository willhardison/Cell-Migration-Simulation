import pygame
from grid import generate_gradient
from cell import Cell, SplitCell
import numpy as np

# define constants
m = 100
n = 100
variance = 1
cell_size = 10
tick_rate = 20  # milliseconds
vision_radius = 1

# initialize grid and cell
grid = generate_gradient(m, n, variance)
split_cell = SplitCell(50, 15, grid)
compass_cell = Cell(50, 15, grid, 1)

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((n*cell_size, m*cell_size))
clock = pygame.time.Clock()

# draw the grid and cell


def draw_grid():
    for i in range(m):
        for j in range(n):
            # map the value to 0-255 for grayscale
            val = abs(int(grid[i, j]*255/np.max(grid)))
            color = (val, val, val)
            pygame.draw.rect(screen, color, (j*cell_size, i *
                             cell_size, cell_size, cell_size))
    for cell in split_cell.visited:
        if cell in compass_cell.visited:
            pygame.draw.rect(screen, (100, 100, 0), (cell[1]*cell_size,
                             cell[0]*cell_size, cell_size, cell_size))
        else:
            pygame.draw.rect(screen, (100, 0, 0), (cell[1]*cell_size,
                                                   cell[0]*cell_size, cell_size, cell_size))
    for cell in compass_cell.visited:
        if cell in split_cell.visited:
            pygame.draw.rect(screen, (100, 100, 0), (cell[1]*cell_size,
                             cell[0]*cell_size, cell_size, cell_size))
        else:
            pygame.draw.rect(screen, (0, 100, 0), (cell[1]*cell_size,
                                                   cell[0]*cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, (200, 0, 0), (split_cell.y*cell_size,
                     split_cell.x*cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, (0, 255, 0,), (compass_cell.y*cell_size,
                     compass_cell.x*cell_size, cell_size, cell_size))


def run(m, n, variance, cell_size, tick_rate):
    running = True
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update the cell's position
        split_cell.move()
        compass_cell.move()

        # draw the grid and cell
        draw_grid()

        # update the screen
        pygame.display.flip()

        # wait for the next tick
        clock.tick(tick_rate)

    # quit pygame
    pygame.quit()


# run the simulation
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update the cell's position
    split_cell.move()
    compass_cell.move()

    # draw the grid and cell
    draw_grid()

    # update the screen
    pygame.display.flip()

    # wait for the next tick
    clock.tick(tick_rate)

# quit pygame
pygame.quit()
