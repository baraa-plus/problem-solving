class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        n = len(nums)
        i = n - 1
        seen = set()
        result = 0

        while i >= 0:
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])
            i -= 1

        return result
