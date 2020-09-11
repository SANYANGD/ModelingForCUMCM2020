
Inf = float('inf')

def dijstra(distanceMatrix, fromPoint, toPoint, numOfArea):
    dist = [Inf] * numOfArea
    dist[fromPoint] = 0
    book = [0] * numOfArea  # 记录已经确定的顶点
    # 每次找到起点到该点的最短途径
    u = fromPoint
    for _ in range(numOfArea - 1):  # 找n-1次
        book[u] = 1  # 已经确定
        # 更新距离并记录最小距离的结点
        next_u, minVal = None, float('inf')
        for v in range(numOfArea):  # w
            w = distanceMatrix[u][v]
            if w == Inf:  # 结点u和v之间没有边
                continue
            if not book[v] and dist[u] + w < dist[v]:  # 判断结点是否已经确定了，
                dist[v] = dist[u] + w
                if dist[v] < minVal:
                    next_u, minVal = v, dist[v]
        # 开始下一轮遍历
        u = next_u
    print(dist)
    return dist[toPoint]


if __name__=='__main__':
    distanceMatrix1 = [[0,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1, Inf, Inf],
                [1,  0,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf],
                [Inf, Inf,  0,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1, Inf, Inf],
                [Inf, Inf,  1,  0,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  1, Inf, Inf],
                [Inf, Inf, Inf,  1,  0,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf,  1,  0,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  1, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf,  1,  0,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1, Inf, Inf, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf, Inf,  1,  0,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1, Inf, Inf, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  0,  1, Inf, Inf, Inf, Inf,  1,  1,  1, Inf, Inf, Inf,  1,  1, Inf, Inf, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  1,  0,  1, Inf,  1, Inf,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  0,  1,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  0,  1,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  1,  1,  0,  1,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  1,  0,  1,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  1, Inf, Inf,  1,  1,  0,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1, Inf, Inf, Inf, Inf,  1,  1,  0,  1,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1, Inf, Inf, Inf, Inf, Inf, Inf,  1,  0,  1, Inf, Inf,  1, Inf, Inf, Inf, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  1,  0,  1,  1,  1, Inf, Inf, Inf, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1, Inf,  1,  0,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  1,  0,  1, Inf, Inf, Inf, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  1, Inf,  1,  0,  1,  1, Inf, Inf, Inf,  1],
                [Inf, Inf, Inf, Inf, Inf, Inf,  1,  1,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  0,  1, Inf, Inf, Inf, Inf],
                [Inf, Inf, Inf, Inf, Inf,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  1,  0,  1, Inf,  1, Inf],
                [Inf, Inf, Inf,  1,  1,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  0,  1,  1, Inf],
                [1, Inf,  1,  1, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  0,  1, Inf],
                [Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1,  1,  1,  0,  1],
                [Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf,  1, Inf, Inf, Inf, Inf,  1,  0]]
    fromPoint, toPoint, numOfArea = 0, 26, 27
    dijstra(distanceMatrix1, fromPoint, toPoint, numOfArea)
