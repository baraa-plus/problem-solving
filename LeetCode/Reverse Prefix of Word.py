class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result = ""
        n = len(word)
        ch_found = False

        i = 0
        while i < n:
            if word[i] == ch:
                ch_found = True
                for j in range(i, -1, -1):
                    result += word[j]
                i += 1
                break
            i += 1

        if ch_found:          
            while i < n:
                result += word[i]
                i += 1
            return result

        return word
