def select_stops(water_stops, capacity):
    sorted_list = []
    current_stop = 0
    for i in range(len(water_stops)):
        stop_capacity = water_stops[i] - capacity
        if stop_capacity > current_stop:
            sorted_list.append(water_stops[i - 1])
            current_stop = water_stops[i - 1]

    sorted_list.append(water_stops[-1])

    return sorted_list

    # select_list = list()
    # select_list.append(water_stops[-1]) # 26
    # # limit_stop = capacity
    #
    # for i in range(len(water_stops)):
    #     now_stop = select_list[i] # 26
    #     compare_list = list()
    #     for j in range(len(water_stops) - 1):
    #         next_stop_range = now_stop - capacity
    #         # 26 - 4 = 22
    #
    #         stop_candidate = water_stops[-(j + 2)]
    #         if stop_candidate >= next_stop_range:
    #             compare_list.append(stop_candidate)
    #
    #     compare_list.sort()
    #     if compare_list[0] == select_list[-1]:
    #         break
    #     if select_list[-1] - capacity <= 0:
    #         break
    #
    #     select_list.append(compare_list[0])
    #
    # return sorted(select_list)



# 테스트 코드
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))