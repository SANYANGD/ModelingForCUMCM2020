"""
input:
output: money
"""

MAX_LOAD = 1200
DAY = 10
BASIC_INCOME = 200
WATER_WEIGHT_PERCASE = 2
FOOD_WEIGHT_PERCASE = 3
WATER_PRICE_PERCASE = 5
FOOD_PRICE_PERCASE = 10
BASIC_WATER_CONSUMPTION_0 = 3
BASIC_FOOD_CONSUMPTION_0 = 4
BASIC_WATER_CONSUMPTION_1 = 9
BASIC_FOOD_CONSUMPTION_1 = 9
BASIC_WATER_CONSUMPTION_2 = 10
BASIC_FOOD_CONSUMPTION_2 = 10
END_NOTE = 13


def countPlayersMoney(weather, player, route, routeOther, act, actOther, playerNum):
    for i in range(len(route)):

        # 晴天
        if weather[i] == 0:
            if route[i - 1] == route[i]:
                # 停留
                if act[i] == 0:
                    player['water'] += BASIC_WATER_CONSUMPTION_0
                    player['food'] += BASIC_FOOD_CONSUMPTION_0
                # 停留挖矿
                else:
                    player['water'] += BASIC_WATER_CONSUMPTION_0 * 3
                    player['food'] += BASIC_FOOD_CONSUMPTION_0 * 3
                    # 多人同时挖矿时收益减小
                    if act[i] == actOther[i] and route[i] == routeOther[i]:
                        player['money'] += BASIC_INCOME / playerNum
                    else:
                        player['money'] += BASIC_INCOME
            # 前行
            else:
                # 多人前行时消耗增加
                if route[i] != route[i - 1] and route[i] == routeOther[i] and route[i - 1] == routeOther[i - 1]:
                    player['water'] += BASIC_WATER_CONSUMPTION_0 * 2 * playerNum
                    player['food'] += BASIC_FOOD_CONSUMPTION_0 * 2 * playerNum
                else:
                    player['water'] += BASIC_WATER_CONSUMPTION_0 * 2
                    player['food'] += BASIC_FOOD_CONSUMPTION_0 * 2
        # 高温
        else:
            if route[i - 1] == route[i]:
                # 停留
                if act[i] == 0:
                    player['water'] += BASIC_WATER_CONSUMPTION_1
                    player['food'] += BASIC_FOOD_CONSUMPTION_1
                # 停留挖矿
                else:
                    player['water'] += BASIC_WATER_CONSUMPTION_1 * 3
                    player['food'] += BASIC_FOOD_CONSUMPTION_1 * 3
                    # 多人同时挖矿时收益减小
                    if act[i] == actOther[i] and route[i] == routeOther[i]:
                        player['money'] += BASIC_INCOME / playerNum
                    else:
                        player['money'] += BASIC_INCOME
            # 前行
            else:
                # 多人前行时消耗增加
                if route[i] != route[i - 1] and route[i] == routeOther[i] and route[i - 1] == routeOther[i - 1]:
                    player['water'] += BASIC_WATER_CONSUMPTION_1 * 2 * playerNum
                    player['food'] += BASIC_FOOD_CONSUMPTION_1 * 2 * playerNum
                else:
                    player['water'] += BASIC_WATER_CONSUMPTION_1 * 2
                    player['food'] += BASIC_FOOD_CONSUMPTION_1 * 2

        # 到终点后停止
        if route[i] == END_NOTE:
            break

    player['money'] = player['money'] - player['water'] * WATER_PRICE_PERCASE - player['food'] * FOOD_PRICE_PERCASE
    # print(player['water'], player['food'], player['money'])
    return player


def main():
    weather = [0, 1, 0, 0, 0, 0, 1, 1, 1, 1]
    playerNum = 2

    routeA = [[2, 3, 9, 10, 13, 0, 0, 0, 0, 0],
              [2, 2, 3, 9, 10, 13, 0, 0, 0, 0],
              [2, 3, 9, 9, 10, 13, 0, 0, 0, 0],
              [2, 2, 3, 9, 9, 10, 13, 0, 0, 0],
              [2, 3, 9, 9, 9, 10, 13, 0, 0, 0],
              [2, 2, 3, 9, 9, 9, 10, 13, 0, 0],
              [2, 3, 9, 9, 9, 9, 10, 13, 0, 0],
              [5, 6, 13, 0, 0, 0, 0, 0, 0, 0],
              [4, 7, 12, 13, 0, 0, 0, 0, 0, 0]]
    actA = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    routeB = [[4, 3, 9, 11, 13, 0, 0, 0, 0, 0],
              [4, 4, 3, 9, 11, 13, 0, 0, 0, 0],
              [4, 3, 9, 9, 11, 13, 0, 0, 0, 0],
              [4, 4, 3, 9, 9, 11, 13, 0, 0, 0],
              [4, 3, 9, 9, 9, 11, 13, 0, 0, 0],
              [4, 4, 3, 9, 9, 9, 11, 13, 0, 0],
              [4, 3, 9, 9, 9, 9, 11, 13, 0, 0],
              [5, 6, 13, 0, 0, 0, 0, 0, 0, 0],
              [4, 7, 12, 13, 0, 0, 0, 0, 0, 0]]
    actB = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for i in range(len(routeA)):
        for j in range(len(routeB)):
            playerA = countPlayersMoney(weather, {'water': 0, 'food': 0, 'money': 10000}, routeA[i], routeB[j],
                                        actA[i], actB[j], playerNum)
            playerB = countPlayersMoney(weather, {'water': 0, 'food': 0, 'money': 10000}, routeB[j], routeA[i],
                                        actB[j], actA[i], playerNum)
            print('A为方案 %d ，B为方案 %d 时，两者结果。' % (i+1, j+1), 'playerA：', playerA, 'playerB：', playerB)


if __name__ == '__main__':
    main()

