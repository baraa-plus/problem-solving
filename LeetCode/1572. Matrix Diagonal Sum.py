class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        result = 0

        for i in range(n):
            result  += mat[i][i]
            if i != n - 1 - i:
                result += mat[i][n - 1 - i]

        return result                
