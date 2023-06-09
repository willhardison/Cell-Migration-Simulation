import numpy as np
import random


def generate_gradient(m, n, variance):
    grid = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            choice = random.randint(j-variance, j+variance)
            if choice < 1:
                choice = 1
            grid[i, j] = choice
    return grid
