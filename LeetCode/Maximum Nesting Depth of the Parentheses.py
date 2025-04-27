class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        result = 0

        for parentheses in s:
            if parentheses == '(':
                stack.append(parentheses)
            elif parentheses == ')':
                result = max(result, len(stack))
                stack.pop()

        return result
