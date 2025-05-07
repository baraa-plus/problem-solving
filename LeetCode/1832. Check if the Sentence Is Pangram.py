class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = [False] * 26

        for char in sentence:
            letters[ord(char) - 97] = True

        for letter in letters:
            if letter == False:
                return False
        
        return True

