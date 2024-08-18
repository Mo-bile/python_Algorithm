from collections import deque

def solution(priorities, location):
    answer = 0    
    queue = deque()
    
    p = 0
    for prioritie in priorities:
        queue.append((p,prioritie))    
        p += 1
    
    while queue :
        ps = queue.popleft()
        
        # 우선순위가 더 높은 프로세스가 있는지 확인
        if any(ps[1] < q[1] for q in queue):
            queue.append(ps)
        else :
            answer += 1
            if ps[0] == location:
                return answer
    
    # while queue :
    #     ps = queue.popleft()
    #     for i in range(len(queue)):
    #         # if ps[1] >= queue[i][1]: # 내가 가장 크면
    #         if ps[1] >= queue[i][1]: # 내가 가장 크면
    #             print(i)
    #             print(ps[1], queue[i][1])
    #             answer += 1
    #             if ps[0] == location:
    #                 return answer
    #             continue # 프로세스 실행
    #         # 다른게 더 크면
    #         queue.append(ps) # 큐에 다시 넣기    
    
    return answer