# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # index1_element = my_list[index1]
    # index2_element = my_list[index2]
    # my_list.remove(index1_element)
    # my_list.remove(index2_element)
    # my_list.insert(index1,index2_element)
    # my_list.insert(index2,index1_element)
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

# 퀵 정렬에서 사용되는 partition 함수
# def partition(my_list, start, end):
    # pivot = my_list[end]
    # small = list()
    # big = list()
    # big_index = 0
    #
    # for i in range(len(my_list) - 2):
    #     # pivot 이 더 클 때
    #
    #     # swap 한다 => b++ =>
    #
    #     # 1) small 에 (리스트 앞부분에) 넣어준다
    #
    #     # 2) small_index 를 받아준다
    #
    #     # 3) small 과 big 의 위치를 바꾼다.
    #
    #     # 3) big_index 를 밀어낸다.
    #     print(i , big_index)
    #     print(my_list[i] <  pivot)
    #     if my_list[i] < pivot:
    #         swap_elements(my_list, i, big_index)
    #         big_index += 1
    #         small.append(my_list[i])
    #     # pivot 이 더 작을 때
    #     else:
    #         print("아무것도")
    #         big.append(my_list[i])
    #     print(i+1,"순회", my_list)
    #
    #
    #     if i == 4:
    #         print("옴")
    #         print(big_index)
    #         swap_elements(my_list, pivot, big_index - 1)
    #         print("최종",my_list)


    # my_list.clear()
    # my_list += small + pivot + big


# 힌트 보고 푼 방법
# def partition(my_list, start, end):
#     pivot = my_list[end]
#     i = start
#     b_index = 0
#
#     for _ in range(len(my_list)):
#
#         if my_list[i] < pivot:
#             swap_elements(my_list, i , b_index)
#             i += 1
#             b_index += 1
#         else:
#             i += 1
#     swap_elements(my_list, b_index, end)
#
#     return my_list.index(pivot)

# 해답을 보고 푼 방법
# def partition(my_list, start, end):
#     # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
#
#     # * start, end 의 용도 생각못함
#     i = start
#     b = start
#     # * pivot 값을 굳이 뺄 필요없음
#     p = end
#
#     # 범위안의 모든 값들을 볼 때까지 반복문을 돌린다
#     while i < p:
#         # i 인덱스의 값이 기준점보다 작으면
#         # i와 b 인덱스에 있는 값들을 교환하고
#         # b를 1 증가 시킨다
#         if my_list[i] <= my_list[p]:
#             swap_elements(my_list, i, b)
#             b += 1
#         # * i는 이렇게 외부로 두면 충분함
#         i += 1
#
#     # b와 기준점인 p 인덱스에 있는 값들을 바꿔준다
#     swap_elements(my_list, b, p)
#     p = b
#
#     # pivot의 최종 인덱스를 리턴해 준다
#     return p


# 한번더 안보고 풀어보기
def partition(my_list, start, end):
    i = start
    b = start
    p = end

    while i < p:
        # 여기서 등호 누락
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    swap_elements(my_list, b, p)
    p = b
    return p



# 테스트 코드 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 코드 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)


