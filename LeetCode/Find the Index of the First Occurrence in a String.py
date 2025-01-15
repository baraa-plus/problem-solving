class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      
        def sub_str(string, i, j):
            length = len(string) - i
            if length < j:
                return ""
            sub = ""
            for i in range(i, i + j):
                sub += string[i]
            return sub

        n = len(haystack)
        needle_n = len(needle)
      
        for i in range(n):
            if sub_str(haystack, i, needle_n) == needle:
                return i
        return -1
