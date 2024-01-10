def min_fee(pages_to_print):
    late_min = 0
    late_list = list()

    for page in sorted(pages_to_print):
        late_min += page
        late_list.append(late_min)

    return sum(late_list)

def min_fee2(pages_to_print):
    sorted_page = sorted(pages_to_print)
    amount = 0
    for i in range(len(sorted_page)):
        amount += sorted_page[i] * (len(sorted_page) - i)
    return amount

# 테스트 코드
print(min_fee2([6, 11, 4, 1]))
print(min_fee2([3, 2, 1]))
print(min_fee2([3, 1, 4, 3, 2]))
print(min_fee2([8, 4, 2, 3, 9, 23, 6, 8]))