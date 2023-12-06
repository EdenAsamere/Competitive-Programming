class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_can = max(candies)
        return [True if extraCandies+i >= max_can else False for i in candies]