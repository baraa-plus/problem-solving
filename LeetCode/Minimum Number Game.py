class Solution:
    def numberGame(self, nums):
        nums.sort()
        n = len(nums)
        result = [0] * n

        i = 0
        while i < n:
            result[i] = nums[i + 1]
            result[i + 1] = nums[i]
            i += 2
        
        return result
