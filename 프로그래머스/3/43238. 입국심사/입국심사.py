def solution(n, times):
    left, right = min(times), max(times) * n
    
    while left < right: # 이분탐색은 다음과 같이 종료 조건을 두어야함
        sum = 0    
        mid = (left + right) // 2
        
        for time in times:
            sum += mid // time
        
        if sum >= n :
            right = mid
        else:
            left = mid + 1 # mid 보다 + 1이 되게 해야함

    return left #left가 right 보다 크거나 같으면 left return