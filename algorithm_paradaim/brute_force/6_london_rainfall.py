# 10
# 6

# def trapping_rain(buildings):
#     building_set = [buildings[0], buildings[1]]
#     index = [0, 1]
#     # 1. 현재 나 보다 큰 값 찾기
#     for i in range(len(buildings) - 1):
#         for j in range(i + 1, len(buildings)):
#             if building_set[0] < buildings[j]:
#                 building_set[0] = buildings[j]
#                 index[0] = j
#
#         if building_set[1] < buildings[i]:
#             building_set[1] = buildings[i]
#             index[1] = i
#
#     index[0] += 1
#     index[1] += 1
#     real_index = abs(index[0] - index[1] - 1)
#     print(real_index)
#     print(index, buildings, "확인용")
#     print(index)
#     print(building_set)
#
#     differ = building_set[0] * building_set[1] * real_index
#     print("differ은",differ)
#     return building_set

    # 2. 0 전후에 가장 큰 값 두가지 받아오기

    # 3. 두가지 값 중 작은 값 기준으로 count 하기

# 모재영 방법
def trapping_rain(buildings):
    rainfall_total = 0
    rainfall = [0] * len(buildings)
    max_left = 0
    max_right = 0
    for i in range(0, len(buildings)):
        # 현재 인덱스 기준 왼쪽 가장 높은 건물 높이
        for j in range(i, -1, -1):
            max_left = max(buildings[j], max_left)
        # 현재 인덱스 기준 오른쪽 가장 높은 건물 높이
        for j in range(i, len(buildings), +1):
            max_right = max(buildings[j], max_right)

        rainfaill_element = min(max_left, max_right) - buildings[i]
        if(rainfaill_element < 0): rainfaill_element = 0

        rainfall[i] = rainfaill_element
        max_left = 0
        max_right = 0

        # max_right 로 다시 i 로 현재위치 재조정

    for rain in rainfall:
        rainfall_total += rain
    print(rainfall)
    return rainfall_total

# code it 방법
def trapping_rain2(buildings):
    total_height = 0

    for i in range(1, len(buildings)-1 ):
        #슬라이싱으로 가볍게 가능함
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        # max_left, max_right 초기화 필요없음 -> 슬라이싱 함
        upper_bound = min(max_left, max_right)
        total_height += max(0, upper_bound - buildings[i])
    return total_height

# 테스트
print(trapping_rain2([3, 0, 0, 2, 0, 4]))
print(trapping_rain2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
