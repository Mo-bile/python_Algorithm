# def consecutive_sum(start, end):
#     total = 0
#     # 재귀 구간
#     # 먼저 두개로 분할한다 (divide)
#     divide_number = (start + end) // 2
#     # 분할은 자기 분할할 수 없을 만큼(자기자신) 나눈다. (conquer)
#     # print(divide_number)
#     if start == end:
#         return divide_number
#
#     left_divide = consecutive_sum(start, divide_number)
#     right_divde = consecutive_sum(divide_number+1, end)
#     # 함수탈출 구간
#     # 끝까지 나눈것에서 부터 합을 구한다
#     total += (left_divide + right_divde)
#     # 구한 합에서 옆에 나눈것과 조합한다
#     return total

# 풀이
def consecutive_sum(start, end):
    # base case : 문제가 작아서 바로 풀 수있는 경우
    if end == start:
        return start

    # divide
    mid = (start + end) // 2

    # conquer, combine
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)


# 테스트 코드
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))