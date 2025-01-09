class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        num_of_l = 0
        num_of_r = 0
        for i in range(len(s)):
            if s[i] == 'L':
                num_of_l += 1
            else:
                num_of_r += 1
            if num_of_l == num_of_r:
                result += 1
        return result
