import matplotlib.pyplot as plt
import numpy as np
import scipy.special


# Measurements
# k = 2
# P  = 0.05  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9
# y  =  0.5  1.3  8.0 14.0 26.0 35.0 50.0 60.0 73.0 84.0

# k = 48
# P  = 0.05  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.0
# y  =  5.0  8.5 22.0 28.0 39.0 48.0 0.59 0.68  0.8  0.91

def plot_k2():
    x = np.array([0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    y = np.array([0.005, 0.013, 0.08, 0.14, 0.26, 0.35, 0.50, 0.60, 0.73, 0.84])
    plt.scatter(x, y, marker='o', label='Messwerte k=2')


def plot_k48():
    pass
    x = np.array([0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    y = np.array([0.05, 0.085, 0.22, 0.28, 0.39, 0.48, 0.59, 0.68, 0.8, 0.91])
    plt.scatter(x, y, marker='o', label='Messwerte k=48')


# wrong frist try
def f(P, k):
    return 1 - ((1 - P) ** (k + 1) + (k + 1) * P * (1 - P) ** k)


def g(P, k):
    n = k + 1
    sum = 0
    for i in range(2, n + 1):
        sum += scipy.special.comb(n, i) * P ** i * (1 - P) ** (n - i) \
               * (i / float(n))
    return sum


def plot():
    plt.ylabel('Restfehler')
    plt.xlabel('Kanalfehler')

    k_list = [2, 3, 5, 10, 20, 48]
    for k in k_list:
        x = np.arange(0.0, 1.0, 0.001)
        y = g(x, k)
        plt.plot(x, y, label='k=' + str(k))

    plot_k2()
    plot_k48()

    plt.legend()
    plt.savefig('plots')
    plt.show()


if __name__ == '__main__':
    plot()
