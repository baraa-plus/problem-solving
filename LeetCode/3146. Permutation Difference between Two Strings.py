class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0
        n = len(s)
        dict = {s[i]: i for i in range(n)}
        for i in range(n):
            if s[i] != t[i]:
                result += abs(i - dict[t[i]])
        return result
