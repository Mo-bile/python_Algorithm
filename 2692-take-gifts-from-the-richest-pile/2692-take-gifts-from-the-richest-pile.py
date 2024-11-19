import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        answer = 0

        # 1. gits 를 maxheap 으로 변환
        max_heap = [-x for x in gifts]
        heapq.heapify(max_heap)

        # 2. K 번 반복하기
        for _ in range(k):
            # (1) heapop 후 제곱근 (내림)
            if not max_heap:
                break
            piles = - heapq.heappop(max_heap)
            print(piles)

            # 1) 만약 1이라면 제곱근 안하기
            if piles == 1:
                answer += 1
                continue
            # 2) 제곱근
            squ_pile = int(math.sqrt(piles))
            # (2) heappush
            heapq.heappush(max_heap, -squ_pile)

        # 3. list 의 값 더하기
        answer += (-sum(max_heap))

        return answer