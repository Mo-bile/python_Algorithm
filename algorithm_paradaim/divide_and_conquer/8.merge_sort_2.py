def merge(list1, list2):
    merge_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merge_list.append(list2[j])
            j += 1
        # elif (list1[i] < list2[j]):
        else:
            merge_list.append(list1[i])
            i += 1

    if i == len(list1):
        merge_list += list2[j:]
    if j == len(list2):
        merge_list += list1[i:]

    return merge_list

# 합병 정렬
def merge_sort(my_list):
    merged_list = []
    if len(my_list) < 2:
        return my_list

    divide_list_left = merge_sort(my_list[:len(my_list)//2])
    divide_list_right = merge_sort(my_list[len(my_list)//2:])

    return merge(divide_list_left, divide_list_right)

    # if len(divide_list_left) < 2:
    #     merged_list.append(merge(divide_list_left, divide_list_right))
    #     return merged_list
    #
    # if len(divide_list_right) < 2:
    #     merged_list.append(merge(divide_list_left, divide_list_right))
    #     return merged_list

    # sorted_list_left = (merge_sort(divide_list_left))
    # sorted_list_right = (merge_sort(divide_list_right))
    # merged_list += sorted_list_left[:len(sorted_list_left)]
    # merged_list += sorted_list_right[:len(sorted_list_right)]

# 테스트 코드
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
