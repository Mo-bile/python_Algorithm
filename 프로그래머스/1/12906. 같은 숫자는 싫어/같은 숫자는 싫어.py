def solution(arr):
    answer = []
    
    for a in arr:
        if len(answer) == 0:
            answer.append(a)
        else :
            if answer[-1] != a:
                answer.append(a)
            
    return answer
        
# set()은 안됨 -> [1,3,0,1] 중 [0,1,3] 으로 나옴
# hash() 도 안됨 -> 마찬가지
# 즉 두개 다 중복이 없고, 순서가 정렬되어서 출력됨