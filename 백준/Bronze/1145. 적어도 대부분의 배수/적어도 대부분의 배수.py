from itertools import combinations
from math import gcd

if __name__ == "__main__":
    input_list = list(map(int, input().split()))

    # 최대공약수 구하기인것을 몰랐을 때
    # set 으로 해서 공집합 방식으로 하려고 함

    # set_list = []
    # for _ in range(len(input_list)):
    #     value = input_list.pop()
    #
    #     multi = 1
    #     set_value = set()
    #     multiple_value = 0
    #     while multiple_value < 101:
    #         multiple_value = multi * value
    #         multi += 1
    #         set_value.add(multiple_value)
    #     set_list.append(set_value)
    # print(set_list)


    def lcm(a,b):
        # 최소공배수로 최대공약수 구하기
        return a * b // gcd(a,b)

    min_lcm = float('inf')
    for combo in combinations(input_list, 3):
        lcm_value = lcm(lcm(combo[0], combo[1]), combo[2])
        min_lcm = min(min_lcm, lcm_value)

    print(min_lcm)
