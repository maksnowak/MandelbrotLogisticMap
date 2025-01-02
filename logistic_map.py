import numpy as np

def logistic_map(r, x):
    return r * x * (1 - x)

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    r = [0.5, 1, 2, 3.2, 3.5, 3.8, 3.9]
    x = np.linspace(0, 1, 1000)
    for r_i in range(len(r)):
        y = logistic_map(r_i, x)
        plt.plot(x, y)
    plt.xlabel('$x_n$')
    plt.ylabel('$f(x) = x_{n+1}$')
    plt.title('Logistic map')
    plt.legend(['r = 0.5', 'r = 1', 'r = 2', 'r = 3.2', 'r = 3.5', 'r = 3.8', 'r = 3.9'])
    plt.show()