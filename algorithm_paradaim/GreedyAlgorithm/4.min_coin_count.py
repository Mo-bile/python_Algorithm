# 모's way
def min_coin_count(value, coin_list):
    coin_list.sort(reverse=True)
    count_coin = 0

    for coin in coin_list:
        count_coin += value // coin
        value %= coin
        if value <= 0:
            break
    return count_coin

# 모범답안
def min_coin_count2(value, coin_list):
    # 누적 동전 개수
    count = 0

    # coin_list의 값들을 큰 순서대로 본다
    for coin in sorted(coin_list, reverse=True):
        # 현재 동전으로 몇 개 거슬러 줄 수 있는지 확인한다
        count += (value // coin)

        # 잔액을 계산한다
        value %= coin

    return count

# 테스트 코드
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))