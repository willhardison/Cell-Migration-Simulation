from grid import generate_gradient
from cell import Cell, SplitCell
import numpy as np
import matplotlib.pyplot as plt


def sim(m, n, variance, x, y):
    grid = generate_gradient(m, n, variance)
    split_cell = SplitCell(x, y, grid)
    compass_cell = Cell(x, y, grid, 1)
    c_final = 1
    s_final = 1
    compass_speed = 0
    split_speed = 0

    compass_end = False
    split_end = False

    running = True
    while running:
        # update the cell's position
        if not compass_end:
            compass_cell.move()
            compass_speed += 1
        if not split_end:
            split_cell.move()
            split_speed += 1

        if int(compass_cell.y) == int(n)-1:
            compass_end = True
            c_final = compass_speed
        if int(split_cell.y) == int(n)-1:
            split_end = True
            s_final = split_speed

        if compass_end and split_end:
            running = False
    return c_final, s_final


def average_sim(m, n, varience, iterations, x, y):
    c_final = 0
    s_final = 0
    for i in range(iterations):
        c, s = sim(m, n, varience, x, y)
        c_final += c
        s_final += s
    c_final /= iterations
    s_final /= iterations
    return c_final, s_final


def variance_sim(m, n, variance, iterations, x, y):
    d = {}
    for i in range(variance):
        c, s = average_sim(m, n, i, iterations, x, y)
        d[i] = [c, s]
    return d


def grid_size_sim(m, variance, iterations):
    d = {}
    for i in range(variance//2, m):
        x = i//5
        y = i//5
        c, s = average_sim(i, i, variance, iterations, x, y)
        d[i] = [c, s]
    return d


def plot_variance(d, size):
    x = []
    y1 = []
    y2 = []
    for i in d:
        x.append(i)
        y1.append(int(d[i][0]))
        y2.append(int(d[i][1]))
    c_y = np.array(y1)
    s_y = np.array(y2)
    x1 = np.array(x)
    a, b, c = np.polyfit(x1, c_y, 2)  # Update to fit a second-order polynomial
    e, f, g = np.polyfit(x1, s_y, 2)

    # Generate points for the curve
    x_curve = np.linspace(min(x), max(x), 100)
    y1_curve = a*x_curve**2 + b*x_curve + c
    y2_curve = e*x_curve**2 + f*x_curve + g

    # Update this line
    plt.plot(x_curve, y1_curve, label='Line of Best Fit (2nd Order) Compass')
    plt.plot(x_curve, y2_curve, label='Line of Best Fit (2nd Order) Split')
    plt.scatter(x, y1, label='Compass Speed')
    plt.scatter(x, y2, label='Split Speed')
    plt.legend()
    plt.xlabel('Variance')
    plt.ylabel('Speed')
    plt.title('Compass and Split Cell Completion Time vs. Variance at size ' + size)
    plt.show()


def plot_grid_size(d, variance):
    x = []
    y1 = []
    y2 = []
    for i in d:
        x.append(i)
        y1.append(int(d[i][0]))
        y2.append(int(d[i][1]))
    c_y = np.array(y1)
    s_y = np.array(y2)
    x1 = np.array(x)
    a, b, c = np.polyfit(x1, c_y, 2)  # Update to fit a second-order polynomial
    e, f, g = np.polyfit(x1, s_y, 2)

    # Generate points for the curve
    x_curve = np.linspace(min(x), max(x), 100)
    y1_curve = a*x_curve**2 + b*x_curve + c
    y2_curve = e*x_curve**2 + f*x_curve + g

    # Update this line
    plt.plot(x_curve, y1_curve, label='Line of Best Fit (2nd Order) Compass')
    plt.plot(x_curve, y2_curve, label='Line of Best Fit (2nd Order) Split')
    plt.scatter(x, y1, label='Compass Time')
    plt.scatter(x, y2, label='Split Time')
    plt.legend()
    plt.xlabel('Grid size')
    plt.ylabel('Time to Completion')
    plt.title('Compass and Split Completion vs. Variance at size ' + variance)
    plt.show()


if __name__ == "__main__":
    d = variance_sim(100, 100, 40, 300, 50, 10)
    # f = grid_size_sim(200, 20, 100)
    # for i in f:
    #     print("size: " + str(i), "compass length: " +
    #           str(f[i][0]), "split length: " + str(f[i][1]))
    for i in d:
        print("variance: " + str(i), "compass speed: " +
              str(d[i][0]), "split speed: " + str(d[i][1]))
    plot_variance(d, "100")
    # print(average_sim(30, 30, 10, 500))
