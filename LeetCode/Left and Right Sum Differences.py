# Method - 1 (Brute Force):
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0 for _ in range(n)]
        for i in range(n):
            left_sum = right_sum = 0
            for j in range(n):
                if i == j:
                    continue
                elif i < j:
                    left_sum += nums[j]
                else:
                    right_sum += nums[j]
            result[i] = abs(left_sum - right_sum)
        return result

# Method - 2:
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:        
        n = len(nums)
        result = [0 for _ in range(n)]
        left_sum = right_sum = 0
      
        for i in range(1, n):
            right_sum += nums[i]
          
        result[0] = right_sum
        for i in range(1, n):
            right_sum -= nums[i]
            left_sum += nums[i - 1]
            result[i] = abs(left_sum - right_sum)
          
        return result



