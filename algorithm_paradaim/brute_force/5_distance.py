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

    for coordinate in coordinates:
        for coordinate2 in coordinates:
            if(coordinate == coordinate2):
                continue
            min_product = min(min_product, distance(coordinate, coordinate2))
            if min_product != tmp:
                tuple_list = [coordinate, coordinate2]
                tmp = min_product

    return tuple_list

# 모범답안 케이스 -> 코드 길이가 더 짧음

# 1. len 인덱스 조작 서툼
# 2. 문제에서 요구하는건 최소길이가 없음 그냥 그 좌표 쌍만 찾으면 됨
def closest_pair2(coordinates):
    pair = [coordinates[0], coordinates[1]]

    for i in range(len(coordinates) - 1): # 0 ~ 끝 -1 까지
        for j in range(i + 1, len(coordinates)): # 1 ~ 끝까지
            store1, store2 = coordinates[i], coordinates[j]

            # 굳이 최소길이 구할 필요 없음
            if distance(pair[0], pair[1]) > distance(store1, store2):
                pair = [store1, store2]
    return pair


# 테스트 코드
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
print(closest_pair2(test_coordinates))