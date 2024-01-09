def max_profit(price_list, count):
    # profit_table = [price_list[0], price_list[1]] # 그냥 0만 너을 때와 어떤차이?
    profit_table = [price_list[0]] #같은 값이 두번 들어가버림
    # profit_table = [0]

    for i in range(1, count + 1):
        if i < len(price_list): # count -> i 로 변경
            profit = price_list[i]
        else:
            profit = 0

        for j in range(1, i // 2 + 1): # i // 2 + 1 로 변경
            tmp = profit_table[j] + profit_table[i - j]
            profit = max(profit, tmp)
        profit_table.append(profit)

    return profit_table[count]



# 테스트 코드
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))