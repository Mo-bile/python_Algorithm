# 0
# None
# 2
# 4
# 1

def binary_search(element, some_list):
    start = 0
    # end = len(some_list)
    end = len(some_list) - 1 # X -1을 안붙여줌

    for data in range(len(some_list)):
        mid = (start + end) // 2
        if some_list[mid] == element:
            return mid
        # element 가 클 때
        elif some_list[mid] < element:
            start = mid + 1
        # element 가 작을 때
        elif some_list[mid] > element:
            end = mid - 1
    return None # V : 이거도 안넣어줌


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))