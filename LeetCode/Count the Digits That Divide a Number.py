class Solution:
    def countDigits(self, num: int) -> int:
        copy_num = num
        result = 0
        while copy_num > 0:
            digit = copy_num % 10
            copy_num //= 10
            if num % digit == 0:
                result += 1
        return result
