# Method - 1 (Brute Force):
class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[j] - nums[i]) == k:
                    result += 1

        return result

# Method - 2:
class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        hashMap = {}
        result = 0

        for num in nums: 
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
                
        for num in hashMap:  
            com = num - k  
            if com in hashMap:  
                result += hashMap[num] * hashMap[com]

        return result
