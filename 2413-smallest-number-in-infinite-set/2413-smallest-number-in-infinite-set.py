import heapq as hq

class SmallestInfiniteSet:

    def __init__(self):
        # self.current = 1
        self.min_heap = list(range(1,1001))
        self.set = set(self.min_heap) #set 의 필요성 몰랐음
        hq.heapify(self.min_heap)
        

    def popSmallest(self) -> int:
        try:
            pop_data = hq.heappop(self.min_heap)
            # if pop_data in self.set:
            self.set.remove(pop_data)
            return pop_data
            
        except IndexError:
            return None
        except KeyError:
            return None

    def addBack(self, num: int) -> None:
        if num < 1 or num > 1000:
            return None
        else :
            if num in self.set:
               return
            else :
                hq.heappush(self.min_heap, num)
                self.set.add(num)
                return None
        
        
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)