def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    i = start
    b = start
    p = end

    while i < p :
        if my_list[i] <= my_list[p]:
            swap_elements(my_list,i,b)
            b += 1
        i += 1

    swap_elements(my_list, p, b)
    p = b
    return p

# 퀵 정렬
# 내가 직접 풀어본 경우
# def quicksort(my_list, start, end):
#     #base_case
#     if start == end:
#         return my_list
#
#     #recursive case
#     pivot = partition(my_list, start, end)
#     return quicksort(my_list, start, pivot - 1) + quicksort(my_list, pivot, end)

def quicksort(my_list, start, end):
    # base case
    # * 연산으로 return 하는 것이 바람직함
    # * 추가로 list 를 반환하는 것이 아니라는 점
    if end - start < 1:
        return

    # my_list를 두 부분으로 나누어주고,
    # partition 이후 pivot의 인덱스를 리턴받는다
    pivot = partition(my_list, start, end)

    # * 두부분 다 pivot -1 혹은 +1을 해야함
    # pivot의 왼쪽 부분 정렬
    quicksort(my_list, start, pivot - 1)

    # pivot의 오른쪽 부분 정렬
    quicksort(my_list, pivot + 1, end)

# 테스트 코드 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 코드 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 코드 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)