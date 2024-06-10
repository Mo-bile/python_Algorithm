def solution(n, times):
    left, right = min(times), max(times) * n
    
    
    while left < right:
        total = 0    
        mid = (left + right) // 2
        
        for time in times:
            total += mid // time
        
        if total >= n :
            right = mid
        else:
            left = mid + 1

    return left