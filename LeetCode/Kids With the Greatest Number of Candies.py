class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_number = max(candies)
        for candy in candies:
            if candy + extraCandies < max_number:
                result.append(False)
            else:
                result.append(True)
        return result
