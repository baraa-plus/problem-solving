class Solution:
    def reverseWords(self, s: str) -> str:
        word = ''
        result = ''
        n = len(s)
        spaces = 0

        i = n - 1
        while i >= 0:
            if s[i] != ' ':
                word += s[i]
            else:
                result = ' ' + word + result
                word = ''
            i -= 1

        result = word  + result

        return result
