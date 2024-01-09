def max_profit_memo(price_list, count, cache):
    #base case
    # count 1개는 그 가격 그대로 원으로 return
    if count < 2:
        cache[count] = price_list[count]
        return cache[count]

    # cache 내에 존재하는 경우
    if count in cache:
        # count 개를 팔때 저장된 최대 값
        return cache[count]

    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    # cache 내에 존재하지 않는 경우
    # 반복문 목적 : 나누는 경우의 수 각 만들어서 더하기
    for i in range(1, count // 2 + 1):
        profit = max(profit,
                     max_profit_memo(price_list, i, cache) +
                     max_profit_memo(price_list, count - i, cache)
                     )
    cache[count] = profit
    return profit


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트 코드
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
