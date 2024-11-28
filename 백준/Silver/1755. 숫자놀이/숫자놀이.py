import sys
# 1. 값 두개 입력받음 (정수)
M, N = sys.stdin.readline().strip().split()

# 1-1 입력 받은 값 (정수로 나열)
numbers = [str(i) for i in range(int(M), int(N) + 1)]

# 2. 정렬 기준 만듬
number_standard = {0 : 'zero', 1: 'one', 2: 'two', 3: 'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
number_standard_sort = dict(sorted(number_standard.items(), key=lambda x: x[1]))

# 원래 숫자와 우선순위 정렬
number_dict = {str(n) : i for i, n in enumerate(number_standard_sort)}

# 2. 값들 정렬
# for _ in range(len(numbers)):
# # 1순위 : 자리 갯수 (한자리, 두자리)
#     if len(numbers[i]) == 1:

# numbers.sort(key = lambda x : (len(x), number_dict[x]))
numbers.sort(key=lambda x: [number_dict[digit] for digit in x])
i = 1
for num in numbers:
    sys.stdout.write(str(num) + " ")
    if i % 10 == 0:
        sys.stdout.write("\n")
    i += 1

# 비람다 방식
# def sort_key(x):
#     # 각 자릿수를 number_dict의 순서로 매핑
#     mapped_digits = [number_dict[digit] for digit in x]
#     return mapped_digits
# # 두 자릿수 이상의 숫자도 처리
# numbers.sort(key=sort_key)