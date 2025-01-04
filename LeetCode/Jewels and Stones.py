class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        jewelries = {jewels[i]: True for i in range(len(jewels))}
        for char in stones:
            if char in jewelries:
                result += 1
        return result
