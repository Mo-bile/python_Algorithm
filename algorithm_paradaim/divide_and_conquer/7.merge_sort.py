
# 모재영 풀이
# def merge(list1, list2):
#     merge_list = []
#     if not list1:
#         merge_list.append(list2[0])
#         return merge_list
#     if not list2:
#         merge_list.append(list1[0])
#         return merge_list
#
#     i = 0
#     j = 0
#     while(i != len(list1) and len(list2) != j):
#         if(list1[i] > list2[j]):
#             merge_list.append(list2[j])
#             j += 1
#         elif(list1[i] < list2[j]):
#             merge_list.append(list1[i])
#             i += 1
#
#     if i != len(list1):
#         for i in range (i, len(list1)):
#             merge_list.append(list1[i])
#
#     if j != len(list2):
#         for j in range (j, len(list2)):
#             merge_list.append(list2[j])
#
#
#     return merge_list


    # 테스트 풀이

    # list1_min = 0
    # list2_min = 0
    # #base case
    # if len(list1) == 1 :
    #     list1_min = (min(list1[:len(list1)]))
    # if len(list2) == 1 :
    #     list2_min = (min(list2[:len(list2)]))
    #
    # merge_list = min(list1_min, list2_min)
    #
    # return merge_list
    #
    # # divide
    # list1_mid = len(list1) // 2
    # list2_mid = len(list2) // 2
    #
    # # conquer     # combine
    # return (merge(list1[:list1_mid], list1[list1_mid + 1:])
    #         + merge(list2[:list2_mid], list2[list2_mid + 1:]))


#  모법답안
def merge(list1, list2):
    i = 0
    j = 0

    merged_list = []

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1


    if i == len(list1):
        merged_list += list2[j:]
    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list

# 재작성 (0926) -> 틀림
#     merge_list = []
#
#     i, j = 0, 0
#     while i < len(list1) and j < len(list2):
#         if list1[i] > list2[j]:
#             merge_list.append(list2[j])
#             j += 1
#         elif list1[i] < list2[j]:
#             merge_list.append(list1[i])
#             i += 1
#
#     if i == len(list1):
#         merge_list += list2[j:]
#     if j == len(list2):
#         merge_list += list1[i:]
#
#     return merge_list



# 테스트 코드
print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))