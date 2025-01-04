class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in range(len(operations)):
            x = x + 1 if operations[i][1] == '+' else x - 1
        return x
        
