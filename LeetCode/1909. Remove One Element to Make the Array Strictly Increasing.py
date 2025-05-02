class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                count += 1
                if i > 1 and nums[i] <= nums[i - 2] and i + 1 < n and nums[i - 1] >= nums[i + 1]:
                    return False

        return count < 2
