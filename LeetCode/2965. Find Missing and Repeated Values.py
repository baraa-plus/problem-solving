class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        gridN = n * n
        count = [0] * (gridN + 1)
        result = [0, 0]

        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1
        
        for i in range(1, gridN + 1):
            if count[i] == 2:
                result[0] = i
            elif count[i] == 0:
                result[1] = i

        return result
