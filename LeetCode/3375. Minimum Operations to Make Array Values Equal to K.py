class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0
        seen = set()

        for num in nums:
            if num < k:
                return -1
            elif num > k and num not in seen:
                result += 1
                seen.add(num)
        
        return result
