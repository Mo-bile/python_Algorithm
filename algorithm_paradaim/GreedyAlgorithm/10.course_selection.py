def course_selection(course_list):
    selected_list = list()

    for i in range(len(course_list)):
        earliest_end_course = 100
        earliest_end_index = -1
        for j, val in enumerate(course_list):
            end_time = val[1]
            if end_time < earliest_end_course:
                earliest_end_course = end_time
                earliest_end_index = j

        if earliest_end_index != -1:
            selected_list.append(course_list[earliest_end_index])
            course_list.remove(course_list[earliest_end_index])

            for k, val2 in enumerate(course_list):
                start_time = val2[0]
                end_time = val2[1]
                if earliest_end_course >= start_time or earliest_end_course >= end_time:
                    course_list.remove(course_list[k])

    return selected_list

def course_selection2(course_list):
    sorted_list = sorted(course_list, key=lambda x : x[1]) #key를 기준으로 정렬가능함
    my_selection = [sorted_list[0]]

    for course in sorted_list:
        if course[0] > my_selection[-1][1]: #이렇게 리스트안, 리스트는 이렇게 접근가능 함
            my_selection.append(course)

    return my_selection

# 테스트 코드
print(course_selection2([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection2([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection2([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
