class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        allowed_chars = {char: True for char in allowed}
        for str in words:
            is_allowed = True
            for char in str:
                if char not in allowed_chars:
                    is_allowed = False
                    break
            if is_allowed:
                result += 1
        return result
