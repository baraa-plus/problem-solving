class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            isPalindromic = True
            l = 0
            r = len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    isPalindromic = False
                    break
                l += 1
                r -= 1
            if isPalindromic:
                return word

        return ""
