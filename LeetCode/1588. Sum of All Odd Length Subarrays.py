class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        n = len(arr)

        for i in range(n):
            sum = 0
            counter = 0
            for j in range(i, n):
                sum += arr[j]
                counter += 1
                if counter % 2 == 1:
                    result += sum
        
        return result
