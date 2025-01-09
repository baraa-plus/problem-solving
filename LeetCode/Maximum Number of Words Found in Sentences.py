class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        for i in range(len(sentences)):
            temp = 1
            for j in range(len(sentences[i])):
                if sentences[i][j] == ' ':
                    temp += 1
            result = max(temp, result)
        return result
        
