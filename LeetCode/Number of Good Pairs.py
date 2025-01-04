# Method - 1 (Brute Force):
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    result += 1
        return result

# Method - 2:
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        dict = {}
        for num in nums:
            if num in dict:
                result += dict[num]
                dict[num] += 1
            else:
                dict[num] = 1
        return result
