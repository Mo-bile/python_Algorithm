class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        for index, num in enumerate(nums):
            if index != num:
                return index

        return n