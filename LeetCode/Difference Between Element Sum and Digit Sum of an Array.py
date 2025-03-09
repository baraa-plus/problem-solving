class Solution:
    def differenceOfSum(self, nums) -> int:
        nums_sum = sum(nums)
        digit_sum = 0

        for num in nums:
            if num < 10 and num > -10:
                digit_sum += abs(num)
            else:
                str_num = str(abs(num))
                for char in str_num:
                    digit_sum += int(char)
        
        return nums_sum - digit_sum
    
