class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        result = ''
        n = len(s)
        i = 0
        while k > 0 and i < n:
            if s[i] == ' ':
                k -= 1
                if k < 1:
                    break
            result += s[i]
            i += 1
        return result
