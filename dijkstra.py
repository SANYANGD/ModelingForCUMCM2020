import csv
from collections import defaultdict
from heapq import *
import pandas as pd
import numpy as np

D = float('inf')

def dijkstra_raw(edges, from_node, to_node):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))
    q, seen = [(0, from_node, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == to_node:
                return cost, path
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))
    return 1, []


def dijkstra(edges, from_node, to_node):
    len_shortest_path = -1
    ret_path = []
    length, path_queue = dijkstra_raw(edges, from_node, to_node)
    if len(path_queue) > 0:
        # 1. 先求长度
        len_shortest_path = length
        # 2. 分解path_queue，以获得最短路径中的传递节点
        left = path_queue[0]
        # 2.1 首先记录目标节点
        ret_path.append(left)
        right = path_queue[1]
        while len(right) > 0:
            left = right[0]
            # 2.2 记录其他节点，直到源节点
            ret_path.append(left)
            right = right[1]
        # 3. 最后反转列表，使其成为正常序列
        ret_path.reverse()
    return len_shortest_path, ret_path


def getedge(graph):
    # 读取拓扑，并生成给定拓扑中的所有边
    edges = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if i != j and graph[i][j] != D:
                # (i,j) 是一个链接;graph[i][j]这里是1，链接的长度(i,j)
                edges.append((i, j, graph[i][j]))
    return edges


def findway_1(from_node1, to_node1):
    # distanceGraph1是表示拓扑的二维邻接矩阵
    distanceGraph1 = \
        [[0, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D],
         [1, 0, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, 0, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D],
         [D, D, 1, 0, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D],
         [D, D, D, 1, 0, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D],
         [D, D, D, D, 1, 0, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D],
         [D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, D, D],
         [D, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, D, D],
         [D, D, D, D, D, D, D, 1, 0, 1, D, D, D, D, 1, 1, 1, D, D, D, 1, 1, D, D, D, D, D],
         [D, D, D, D, D, D, D, 1, 1, 0, 1, D, 1, D, 1, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, 1, 0, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, 1, 0, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, 1, 1, 1, 0, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, 1, 1, 0, 1, 1, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, 1, 1, D, D, 1, 1, 0, 1, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, 1, D, D, D, D, 1, 1, 0, 1, 1, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, 1, D, D, D, D, D, D, 1, 0, 1, D, D, 1, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, 0, 1, 1, 1, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, 1, 0, 1, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, 0, 1, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, 1, D, D, D, D, D, D, D, 1, 1, D, 1, 0, 1, 1, D, D, D, 1],
         [D, D, D, D, D, D, 1, 1, 1, D, D, D, D, D, D, D, D, D, D, D, 1, 0, 1, D, D, D, D],
         [D, D, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, 0, 1, D, 1, D],
         [D, D, D, 1, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 0, 1, 1, D],
         [1, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 0, 1, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, 1, 0, 1],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, D, 1, 0]]

    # source_data = pd.read_csv('./distanceGraph.csv', header=None)
    # distanceGraph1 = source_data.values.tolist()
    # print(distanceGraph1)

    edges = getedge(distanceGraph1)
    length, shortest_path = dijkstra(edges, from_node1, to_node1)
    print('关卡 1 中从 %s 到 %s 的最短路径:' % (from_node1 , to_node1 ), shortest_path, ' 最短路长为:', length+1)


def findway_2(from_node2, to_node2):
    distanceGraph2 = \
        [[0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [1, 0, 1, D, D, D, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, 1, 1, D, D, D, D, D, D, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, 1, 1, D, D, D, D, D, 1, 0, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, 1, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, 1, D, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, 0, 1, D, D, D, D, D, D, 1, 1, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, 1, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, 1,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1,
          1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D,
          1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, 1, 0, D, D, D, D, D, D,
          D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D,
          D, 1, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, 1, 0, 1, D, D, D,
          D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, D, D, D, 1, 0, 1, D, D,
          D, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, 1, 0, 1, D,
          D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, 1, 0, 1,
          D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, 1, 0,
          1, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, 1,
          0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, 1, D, D, D, D, D,
          1, 0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, D,
          D, 1, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D,
          D, D, 1, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D,
          D, D, D, D, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D,
          D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1,
          D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1,
          1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, 1, 1, D, D, D, D, D, 1, 0, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, 1, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, 1, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, 1, 1, D, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, 1, D, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, D, 1, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, 1, 1, D, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, 1, 1, D, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, 1, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1, 1],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1, 1],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D, D, 1],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, D, 0, 1, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, 1, 0, 1, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, 1, 0, 1, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, 1, 0, 1, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, D, D, D, D, D, 1, 0, 1],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D,
          D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, 1, 1, D, D, D, D, D, 1, D]]

    edges = getedge(distanceGraph2)
    length, shortest_path = dijkstra(edges, from_node2, to_node2)
    print('关卡 2 中从 %s 到 %s 的最短路径:' % (from_node2, to_node2), shortest_path, ' 最短路长为:', length+1)


def findway_3(from_node3, to_node3):
    distanceGraph3 = \
       [[0, 1, D, 1, 1, D, D, D, D, D, D, D, D],
        [1, 0, 1, 1, D, D, D, D, D, D, D, D, D],
        [D, 1, 0, 1, D, D, D, 1, 1, D, D, D, D],
        [1, 1, 1, 0, 1, 1, 1, D, D, D, D, D, D],
        [1, D, D, 1, 0, 1, D, D, D, D, D, D, D],
        [D, D, D, 1, 1, 0, 1, D, D, D, D, 1, 1],
        [D, D, D, 1, D, 1, 0, D, D, D, 1, 1, D],
        [D, D, 1, D, D, D, D, 0, 1, D, D, D, D],
        [D, D, 1, D, D, D, D, 1, 0, 1, 1, D, D],
        [D, D, D, D, D, D, D, D, 1, 0, 1, D, 1],
        [D, D, D, D, D, D, 1, D, 1, 1, 0, 1, 1],
        [D, D, D, D, D, 1, 1, D, D, D, 1, 0, 1],
        [D, D, D, D, D, 1, D, D, D, 1, 1, 1, 0]]

    edges = getedge(distanceGraph3)
    length, shortest_path = dijkstra(edges, from_node3, to_node3)
    print('关卡 3 中从 %s 到 %s 的最短路径:' % (from_node3, to_node3), shortest_path, ' 最短路长为:', length+1)


def findway_4(from_node4, to_node4):
    distanceGraph4 = \
        [[0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [1, 0, D, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [1, D, D, D, D, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, 1, D, D, D, 1, 0, D, D, D, D, 1, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, 1, D, D, D, D, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, D, D, D, D, 1, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, 1, D, D, D, D, 0, 1, D, D, D, 1, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, D, D, D, D, 1],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, D, 0, 1, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0]]

    edges = getedge(distanceGraph4)
    length, shortest_path = dijkstra(edges, from_node4, to_node4)
    print('关卡 4 中从 %s 到 %s 的最短路径:' % (from_node4, to_node4), shortest_path, ' 最短路长为:', length+1)


def findway_5(from_node5, to_node5):
    distanceGraph5 = \
        [[0, 1, D, 1, 1, D, D, D, D, D, D, D, D],
         [1, 0, 1, 1, D, D, D, D, D, D, D, D, D],
         [D, 1, 0, 1, D, D, D, 1, 1, D, D, D, D],
         [1, 1, 1, 0, 1, 1, 1, D, D, D, D, D, D],
         [1, D, D, 1, 0, 1, D, D, D, D, D, D, D],
         [D, D, D, 1, 1, 0, 1, D, D, D, D, 1, 1],
         [D, D, D, 1, D, 1, 0, D, D, D, 1, 1, D],
         [D, D, 1, D, D, D, D, 0, 1, D, D, D, D],
         [D, D, 1, D, D, D, D, 1, 0, 1, 1, D, D],
         [D, D, D, D, D, D, D, D, 1, 0, 1, D, 1],
         [D, D, D, D, D, D, 1, D, 1, 1, 0, 1, 1],
         [D, D, D, D, D, 1, 1, D, D, D, 1, 0, 1],
         [D, D, D, D, D, 1, D, D, D, 1, 1, 1, 0]]

    edges = getedge(distanceGraph5)
    length, shortest_path = dijkstra(edges, from_node5, to_node5)
    print('关卡 5 中从 %s 到 %s 的最短路径:' % (from_node5, to_node5), shortest_path, ' 最短路长为:', length+1)


def findway_6(from_node6, to_node6):
    distanceGraph6 = \
        [[0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [1, 0, D, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [1, D, D, D, D, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, 1, D, D, D, 1, 0, D, D, D, D, 1, D, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, 1, D, D, D, D, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, D, D, D, D, 1, D, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, 1, D, D, D, D, 0, 1, D, D, D, 1, D, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D, D, D, 1, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, D, D, D, D, 1],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, D, 0, 1, D, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1, D],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0, 1],
         [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, 1, D, D, D, 1, 0]]

    edges = getedge(distanceGraph6)
    length, shortest_path = dijkstra(edges, from_node6, to_node6)
    print('关卡 6 中从 %s 到 %s 的最短路径:' % (from_node6, to_node6), shortest_path, ' 最短路长为:', length+1)


if __name__=='__main__':
    findway_1(0, 26)
    findway_2(0, 63)
    findway_3(0, 12)
    findway_4(0, 24)
    findway_5(0, 12)
    findway_6(0, 24)

