class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0

        current = 0
        for num in gain:
            current += num
            result = max(current, result)

        return result
