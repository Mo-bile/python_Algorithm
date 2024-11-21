import heapq
def solution(scoville, K):    
    count = 0
    # 1. scoville 을 heapify
    heapq.heapify(scoville)
    
    # 2. while 반복문 "scoville최솟값[0]" <= "K" 일때 True
    while scoville[0] < K:
        if len(scoville) <= 1:
            count = -1
            break    
        # 2-1. heappop 두번
        least = heapq.heappop(scoville)
        pre_least = heapq.heappop(scoville)
        # 2-2. 두개 값 연산 (최저 + (두번째 최저 * 2))
        new_scoville = least + (pre_least * 2)
        # 2-3. heappush
        heapq.heappush(scoville, new_scoville) # 늘 무조건 push 되어야함
        count += 1
            
    return count