# Method - 1 (Brute Force):
class Solution:
    def arithmeticTriplets(self, nums, diff: int) -> int:
        result = 0
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        result += 1
        return result

# Method - 2:
class Solution:
    def arithmeticTriplets(self, nums, diff: int) -> int:
        result = 0
        n = len(nums)
        
        seen = set() 
        for num in nums:
            if num - diff in seen and num - diff * 2 in seen:
                result += 1
            seen.add(num)

        return result

