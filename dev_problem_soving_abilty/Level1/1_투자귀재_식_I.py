# 의문 1. 어떻게 해결하지?

def sublist_max(profits):
    max_value = -100
    # pre_value = 0
    sum_list = list()

    for i in range(len(profits)):
        sum_list = profits[i:]
        # j = 0
        for j in range(len(sum_list)):
            # pre_value = max_value # 아래 break 필요가 없어짐
            new_list = sum_list[:j + 1] # 수월한 디버깅 위해서 변수를 따로 둠
            max_value = max(max_value, sum(new_list))
            # if pre_value == max_value: # *중간끼인 + 값 생략되는 우려 존재
            #     break
    return max_value

# 테스트 코드
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8])) # 6, 8, -5, -4, 10, -1, 8 => 22