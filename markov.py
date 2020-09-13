#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
2020 CUMCM B题代码
构建天气变化的马尔科夫链以求得不同天气出现的概率
Coder: 代春洋 胡文哲 刘子奕
"""

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
