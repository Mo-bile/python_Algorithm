# [(2, 3), (3, 4)]

# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    tuple_list = [coordinates[0], coordinates[1]]
    min_product = distance(coordinates[0], coordinates[1])
    tmp = min_product
    # print(min_product)
    # 여기에 코드를 작성하세요
    # i = 0
    for coordinate in coordinates:
        for coordinate2 in coordinates:
            if(coordinate == coordinate2):
                # print(coordinate , coordinate2)
                continue
            # print(coordinate, coordinate2)
            min_product = min(min_product, distance(coordinate, coordinate2))
            if min_product != tmp:
                tuple_list = [coordinate, coordinate2]
                tmp = min_product
            # i += 1
            # print( i,"은" , result)

    return tuple_list

# 테스트 코드
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))