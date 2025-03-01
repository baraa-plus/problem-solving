class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(len(s) - 1):
            roman_value = roman_values[s[i]]
            if roman_value < roman_values[s[i + 1]]:
                result -= roman_value
            else:
                result += roman_value
        result += roman_values[s[len(s) - 1]]
        return result
