class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        while n > 0:
            mod = n % 10
            product *= mod 
            sum += mod
            n //= 10
        return product - sum
