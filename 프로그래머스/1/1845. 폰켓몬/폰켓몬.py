from collections import Counter

def solution(nums):
    counter = Counter(nums)  
    answer = min(len(counter), len(nums) // 2)    
    
    
    return answer