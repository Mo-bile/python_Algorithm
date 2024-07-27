def solution(nums):
    dic = {}
    
    for n in nums:
        if n in dic:
            dic[n] += 1
        else :
            dic[n] = 1

    if len(dic) > len(nums) / 2:
        return len(nums) / 2
    else : 
        return len(dic)