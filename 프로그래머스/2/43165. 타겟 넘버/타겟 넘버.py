def solution(numbers, target):
    
    def dfs(index, current_sum):
        # 배열의 끝에 도달한 경우
        if index == len(numbers):
            # 현재까지의 합이 타겟 넘버와 같은지 확인
            return 1 if current_sum == target else 0
        
        # 현재 숫자를 더하거나 빼는 두 가지 경우에 대해 재귀적으로 호출
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])
    
    return dfs(0, 0)


    

    