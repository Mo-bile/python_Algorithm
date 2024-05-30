from math import sqrt
# 조합대신 순열로 (순서가 중요)
# from itertools import combinations
from itertools import permutations

def is_prime_number(n):
    if n <= 1:
        return False
    # 2부터 시작해야함
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False;
    return True;

def solution(numbers):
    number_set = set() # set으로 중복 해결함
    
    for length in range(1, len(numbers) + 1):
        for perm in permutations(numbers,length):
            num = int(''.join(perm))
            number_set.add(num)
    
    prime_count = sum(1 for num in number_set
                     if is_prime_number(num))
    
    return prime_count
            
        

# def solution(numbers):
#     count = 0
#     numbers_list = list(numbers)
#     for i in range(1 ,len(numbers_list) + 1):
#         for com in combinations(numbers_list, i):
            
#             new_com = int (list(com))
#             # com_list = list(com)
#             # for v in com_list:
#             if is_prime_number(new_com):
#                 count += 1
    
#     return count
                
    



# 소수 판별에 3가지 방법
# I-1. 나누어 떨어지는것 하나라도 있으면 O(N)
# I-2. 절반만 검사하기
# I-3. 제곱근 -> 대칭된다는 점

# II-1