import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K: # 가장 적은 스코빌 지수가 K보다 작을 때 까지 반복
        
        if len(scoville) < 2 :
            return -1
        
        least_value = heapq.heappop(scoville)
        less_value = heapq.heappop(scoville)
        mixed = least_value + (less_value * 2)
        
        # 문제 잘못이해 "모든 음식이 K이상일 때 임"
        # if mixed >= K :
            # break;
        # else :
        heapq.heappush(scoville, mixed)
        answer += 1
            
    return answer