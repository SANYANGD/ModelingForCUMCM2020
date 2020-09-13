
import numpy as np


def markov():
    init_array = np.array([0.5, 0.2, 0.3])
    transfer_matrix = np.array([[0.222, 0.556, 0.222],
                               [0.357, 0.429, 0.214],
                               [0.333, 0.5, 0.167]])
    restmp = init_array
    for i in range(25):
        res = np.dot(restmp, transfer_matrix)
        print(i, "\t", res)
        restmp = res


if __name__ == '__main__':
    markov()
