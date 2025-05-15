class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dict = {}
        result = []
        for num in nums:
            if num in dict:
                result.append(num)
            else:
                dict[num] = True
        return result
