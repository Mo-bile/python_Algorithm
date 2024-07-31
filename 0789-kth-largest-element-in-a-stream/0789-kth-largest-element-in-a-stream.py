import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)


    def add(self, val: int) -> int:
        if self.heap:
            heapq.heappush(self.heap, val)
            while self.k < len(self.heap):
                heapq.heappop(self.heap)
        else :
            self.heap.append(val)
            heapq.heapify(self.heap)
        heap_ = self.heap[0]

        return heap_


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# 실수1
# pop 은 없음