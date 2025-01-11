class Solution:
    def minimumSum(self, num: int) -> int:
        nums = []
        num1, num2 = 0, 0

        while num > 0:
            nums.append(num % 10)
            num //= 10

        nums.sort()
        num1 = num1 * 10 + nums[0]
        num1 = num1 * 10 + nums[2]
        
        num2 = num2 * 10 + nums[1]
        num2 = num2 * 10 + nums[3]
        return num1 + num2
