class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        n = len(pref)

        for i in range(len(words)):
            startWithPref = True
            for j in range(n):
                if n > len(words[i]) or words[i][j] != pref[j]:
                    startWithPref = False
                    break
            if startWithPref:
                result += 1
              
        return result
            
