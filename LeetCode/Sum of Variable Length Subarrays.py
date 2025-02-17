# Method - 1 (Brute Force):
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            start = max(0, i - nums[i])
            for j in range(start, i + 1):
                result += nums[j]
        return result

# Method - 2 (Prefix Sum):
class Solution:
    def subarraySum(self, nums) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = nums[i - 1] + pref[i - 1]

        result = 0
        for i in range(n):
            start = max(0, i - nums[i])
            result += pref[i + 1] - pref[start]
        
        return result
