class Solution:
    def countValidWords(self, sentence: str) -> int:
        n = len(sentence)
        if n == 1 and sentence.isalpha() or sentence in ['!', ',', '.']:
            return 1
        if n == 2 and '-' in sentence:
            return 0
          
        isWord = True
        hyphenCount = 0
        punctuationCount = 0
        result = 0

        i = 0
        while i < n:
            if sentence[i].isdigit():
                isWord = False
            elif sentence[i] == '-':
                hyphenCount += 1
                if hyphenCount > 1 or i == 0 or i == n - 1 or (not sentence[i - 1].isalpha() or not sentence[i + 1].isalpha()):
                    isWord = False
            elif sentence[i] in ['!', '.', ',']:
                punctuationCount += 1
                if i == 0 and n > 1 and sentence[i + 1] == ' ':
                    isWord = True
                elif punctuationCount > 1 or i == 0 or (i < n - 1 and sentence[i + 1] != ' '):
                    isWord = False
            elif sentence[i] == ' ':
                hyphenCount = 0
                punctuationCount = 0
                if isWord and i > 0 and sentence[i - 1] != ' ':
                    result += 1
                isWord = True
            i += 1
        
        if isWord and sentence[n - 1] != ' ':
            result += 1

        return result
