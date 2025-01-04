class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        for char in address:
            result = result + "[.]" if char == '.' else result + char
        return result
