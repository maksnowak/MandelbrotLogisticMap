import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch


def generate_x_values(xmin=-2, xmax=1, xres=20000):
    return np.linspace(xmin, xmax, xres)


def generate_population(xmin=-2, xmax=1, ymin=-1.5, ymax=1.5, xres=3000, yres=3000):
    re = np.linspace(xmin, xmax, xres)
    im = np.linspace(ymin, ymax, yres)
    return re[np.newaxis, :] + 1j * im[:, np.newaxis]


def mandelbrot(c, max_iter=100):
    z = 0
    for _ in range(max_iter):
        z = z ** 2 + c
    return abs(z) < 2


def stabilized_values(c, max_iter=5000, tolerance=1e-6):
    z = 0
    unique = []
    for _ in range(max_iter):
        z = z ** 2 + c
        if abs(z) > 2:
            return []

    for _ in range(10):
        z = z ** 2 + c
        if all(abs(z - u) > tolerance for u in unique):
            unique.append(z)

    return unique


def plot_mandelbrot_set():
    population = generate_population(xres=10000, yres=10000)
    mandelbrot_set = np.zeros(population.shape, dtype=bool)
    for i in range(population.shape[0]):
        for j in range(population.shape[1]):
            mandelbrot_set[i, j] = mandelbrot(population[i, j])

    plt.imshow(mandelbrot_set, extent=[-2, 2, -2, 2])
    plt.xlabel('Re c')
    plt.ylabel('Im c')
    plt.title('Mandelbrot set')
    plt.savefig('mandelbrot_set.png', dpi=300)
    plt.show()


def plot_stabilized_values():
    cmap = ListedColormap([
        'black',
        '#482878',
        '#3E4989',
        '#31688E',
        '#26828E',
        '#1F9E89',
        '#35B779',
        '#6DCD59',
        '#B4DE2C',
        '#FDE725'
    ])
    norm = plt.Normalize(vmin=-1, vmax=10)

    population = generate_population(xres=2000, yres=500)
    num_stabilized = np.zeros(population.shape, dtype=int)

    for i in range(population.shape[0]):
        for j in range(population.shape[1]):
            num_stabilized[i, j] = len(stabilized_values(population[i, j]))

    plt.figure(figsize=(8, 8))
    plt.imshow(np.clip(num_stabilized, -1, 10), extent=[-2, 1, -1.5, 1.5], cmap=cmap, norm=norm)
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.title('Number of Stabilized Values for Each Point')

    legend_elements = [
        Patch(facecolor='black', label='Diverged'),
        Patch(facecolor='#482878', label='1'),
        Patch(facecolor='#3E4989', label='2'),
        Patch(facecolor='#31688E', label='3'),
        Patch(facecolor='#26828E', label='4'),
        Patch(facecolor='#1F9E89', label='5'),
        Patch(facecolor='#35B779', label='6'),
        Patch(facecolor='#6DCD59', label='7'),
        Patch(facecolor='#B4DE2C', label='8'),
        Patch(facecolor='#FDE725', label='9-10'),
    ]
    plt.legend(handles=legend_elements, loc='upper right', title='Stabilized Values')

    plt.savefig('stabilized_values.png', dpi=300)
    plt.show()


def plot_x_length_stabilized_values():
    x = generate_x_values()
    stabilized = [stabilized_values(c) for c in x]

    x_values = []
    y_values = []
    for c, stabilized_set in zip(x, stabilized):
        x_values.append(c.real)
        y_values.append(len(stabilized_set))

    plt.plot(x_values, y_values)
    plt.xlabel('Re')
    plt.ylabel('Number of stabilized values')
    plt.title('Number of stabilized values in Mandelbrot set for z = x + 0j')
    plt.savefig('x_length_stabilized_values.png', dpi=300)
    plt.show()


def plot_x_stabilized_values():
    x = generate_x_values()
    stabilized = [stabilized_values(c) for c in x]

    x_values = []
    y_values = []
    for c, stabilized_set in zip(x, stabilized):
        for value in stabilized_set:
            x_values.append(c.real)
            y_values.append(value.real)
    plt.scatter(x_values, y_values, s=0.5, alpha=0.7, color='blue')
    plt.xlabel('Re')
    plt.ylabel('Stabilized values')
    plt.title('Stabilized values in Mandelbrot set for z = x + 0j')
    plt.savefig('x_stabilized_values.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    plot_mandelbrot_set()
    # plot_stabilized_values()
    # plot_x_length_stabilized_values()
    # plot_x_stabilized_values()
