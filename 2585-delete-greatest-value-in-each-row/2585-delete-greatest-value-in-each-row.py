import heapq
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        # 1. row 수에 따라서 list 생성, answer 생성
        answer = []
        max_heaps = [[-y for y in x] for x in grid]

        # 2. grid 에서 각 row list에 대해서 max_heap 정렬
        for i in range(len(max_heaps)):
            heapq.heapify(max_heaps[i])
            

        # 3. 각 list 에서 pop 하고나서 answer에 누적연산
        while any(max_heaps):
            tmp_list = []
            for _ in range(len(max_heaps)):
                tmp_list.append(- heapq.heappop(max_heaps[_]))
            answer.append(max(tmp_list))

        return sum(answer)