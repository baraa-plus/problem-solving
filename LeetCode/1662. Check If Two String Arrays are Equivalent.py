class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        string1 = ""
        string2 = ""
        
        for i in range(len(word1)):
            for j in range(len(word1[i])):
                string1 += word1[i][j]

        for i in range(len(word2)):
            for j in range(len(word2[i])):
                string2 += word2[i][j]

        return string1 == string2
