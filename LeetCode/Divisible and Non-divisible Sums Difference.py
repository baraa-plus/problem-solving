class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        result = 0
        for i in range(1, n + 1):
            result = result - i if i % m == 0 else result + i
        return result
