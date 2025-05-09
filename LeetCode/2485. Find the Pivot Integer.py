class Solution:
    def pivotInteger(self, n: int) -> int:
        sum = n * (n + 1) // 2

        temp = 0
        while sum > temp:
            if sum - n == temp:
                return n
            temp += n
            sum -= n
            n -= 1

        return -1

            


