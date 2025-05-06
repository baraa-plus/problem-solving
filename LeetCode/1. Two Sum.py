# Method - 1 (Brute Force):
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Method - 2:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            number_to_check = target - nums[i]
            if number_to_check in dict:
                return [dict[number_to_check], i]
            dict[nums[i]] = i
        return []
