class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        total = 0
        nums.sort()

        for i in range(0, len(nums) , 2):
            # total += min(nums[i : i + 2])
            total += nums[i]
            
        return total