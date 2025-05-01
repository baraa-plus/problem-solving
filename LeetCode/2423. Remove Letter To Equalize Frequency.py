class Solution:
    def equalFrequency(self, word: str) -> bool:
        frequency = [0 for i in range(26)]

        for char in word:
            frequency[ord(char) - 97] += 1

        for i in range(26):
            if frequency[i]:
                frequency[i] -= 1
                st = set()
                for j in range(26):
                    if frequency[j]:
                        st.add(frequency[j])
                if len(st) == 1:
                    return True
                frequency[i] += 1

        return False
