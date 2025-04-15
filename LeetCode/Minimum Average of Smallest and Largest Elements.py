class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        averages = []

        for i in range(n // 2):
            minNumber = min(nums)
            nums.remove(minNumber)

            maxNumber = max(nums)
            nums.remove(maxNumber)

            averages.append((minNumber + maxNumber) / 2)
    
        return min(averages)
