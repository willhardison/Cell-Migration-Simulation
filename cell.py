import numpy as np
import random


class Cell:
    def __init__(self, x, y, grid, vision_radius):
        self.x = x
        self.y = y
        self.grid = grid
        self.visited = set()
        self.vision_radius = vision_radius

    def get_adjacent_cells(self):
        adjacent_cells = []
        for i in range(self.x-1, self.x+2):
            for j in range(self.y-1, self.y+2):
                if i == self.x and j == self.y:
                    continue
                if 0 <= i < self.grid.shape[0] and 0 <= j < self.grid.shape[1]:
                    adjacent_cells.append((i, j))
        return adjacent_cells

    def move(self):
        adjacent_cells = self.get_adjacent_cells()
        max_val = -np.inf
        max_cell = None
        for cell in adjacent_cells:
            x, y = cell
            if (x, y) in self.visited:
                continue
            val = float(self.grid[x, y])*float(random.randint(99, 100))/100.0
            if val > float(max_val):
                max_val = val
                max_cell = cell
        if max_cell:
            self.visited.add(max_cell)
            self.x, self.y = max_cell
        else:
            self.x, self.y = random.choice(adjacent_cells)


class SplitCell:
    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
        self.grid = grid
        self.last_direction = (0, 0)
        self.front = 2
        self.side_front = 3
        self.side = 1.0
        self.back = 0.0
        self.side_back = 0.5
        self.visited = set()
        # [-1-1, -10, -11],
        # [0-1, 00, 01],
        # [1-1, 10, 11]
        self.direction_weights = {
            '00': {"11": 1,
                   "01": 1,
                   "-11": 1,
                   "-1-1": 1,
                   "10": 1,
                   "1-1": 1,
                   "-10": 1,
                   "0-1": 1
                   },
            "01": {"01": self.front,
                   "11": self.side_front,
                   "10": self.side,
                   "1-1": self.side_back,
                   "0-1": self.back,
                   "-1-1": self.side_back,
                   "-10": self.side,
                   "-11": self.side_front
                   },
            "11": {"11": self.front,
                   "10": self.side_front,
                   "1-1": self.side,
                   "0-1": self.side_back,
                   "-1-1": self.back,
                   "-10": self.side_back,
                   "-11": self.side,
                   "01": self.side_front,
                   },
            "10": {"10": self.front,
                   "1-1": self.side_front,
                   "0-1": self.side,
                   "-1-1": self.side_back,
                   "-10": self.back,
                   "-11": self.side_back,
                   "01": self.side,
                   "11": self.side_front
                   },
            "1-1": {"1-1": self.front,
                    "0-1": self.side_front,
                    "-1-1": self.side,
                    "-10": self.side_back,
                    "-11": self.back,
                    "01": self.side_back,
                    "11": self.side,
                    "10": self.side_front
                    },
            "0-1": {"0-1": self.front,
                    "-1-1": self.side_front,
                    "-10": self.side,
                    "-11": self.side_back,
                    "01": self.back,
                    "11": self.side_back,
                    "10": self.side,
                    "1-1": self.side_front
                    },
            "-1-1": {"-1-1": self.front,
                     "-10": self.side_front,
                     "-11": self.side,
                     "01": self.side_back,
                     "11": self.back,
                     "10": self.side_back,
                     "1-1": self.side,
                     "0-1": self.side_front
                     },
            "-10": {"-10": self.front,
                    "-11": self.side_front,
                    "01": self.side,
                    "11": self.side_back,
                    "10": self.back,
                    "1-1": self.side_back,
                    "0-1": self.side,
                    "-1-1": self.side_front
                    },
            "-11": {"-11": self.front,
                    "01": self.side_front,
                    "11": self.side,
                    "10": self.side_back,
                    "1-1": self.back,
                    "0-1": self.side_back,
                    "-1-1": self.side,
                    "-10": self.side_front
                    }
        }

    def get_adjacent_cells(self):
        adjacent_cells = []
        for i in range(self.x-1, self.x+2):
            for j in range(self.y-1, self.y+2):
                if i == self.x and j == self.y:
                    continue
                if 0 <= i < self.grid.shape[0] and 0 <= j < self.grid.shape[1]:
                    adjacent_cells.append((i, j))
        return adjacent_cells

    def move(self):
        adjacent_cells = self.get_adjacent_cells()
        max_val = -np.inf
        max_cell = None
        for cell in adjacent_cells:
            x, y = cell
            if (x, y) in self.visited:
                continue
            else:
                last = str(self.last_direction[0]) + \
                    str(self.last_direction[1])
                curr = str(x-self.x) + str(y-self.y)
                weight = self.direction_weights[last][curr]
                val = self.grid[x, y]
                if curr == "00":
                    continue
                random_val = float(random.randint(99, 100)) / \
                    100.0 * float(weight) * float(val)
                if random_val > max_val:
                    max_val = random_val
                    max_cell = cell
        if max_cell:
            self.last_direction = (max_cell[0]-self.x, max_cell[1]-self.y)
            self.visited.add(max_cell)
            self.x, self.y = max_cell
        else:
            self.x, self.y = random.choice(adjacent_cells)
