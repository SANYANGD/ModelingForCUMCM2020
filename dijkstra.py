from collections import defaultdict
from heapq import *


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
    return float("D"), []


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


if __name__=='__main__':
    D = float('inf')
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

    # 读取拓扑，并生成给定拓扑中的所有边
    edges = []
    for i in range(len(distanceGraph1)):
        for j in range(len(distanceGraph1[0])):
            if i != j and distanceGraph1[i][j] != D:
                # (i,j) 是一个链接;distanceGraph1[i][j]这里是1，链接的长度(i,j)
                edges.append((i, j, distanceGraph1[i][j]))

    fromPoint, toPoint = 0, 26
    length, Shortest_path = dijkstra(edges, fromPoint, toPoint)
    # print('长度:', length)
    print('从 %s 到 %s的最短路径:' %(fromPoint+1, toPoint+1),  Shortest_path)

