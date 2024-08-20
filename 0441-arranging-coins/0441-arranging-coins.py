class Solution:
    def arrangeCoins(self, n: int) -> int:
        def ap(k):
            return k * (k+1) // 2
        if n == 1 :
            return 1
        
        low, high = 1, n
        mid = 0
        while low <= high :
            mid = (low + high) // 2 # 1
            print(mid)
            
            ap_result = ap(mid)
            print(ap_result)
            if ap_result == n:
                return mid
            elif ap_result > n:
                high = mid - 1
            elif ap_result < n:
                low = mid + 1
            
        return high