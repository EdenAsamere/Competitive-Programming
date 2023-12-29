class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        start = 0
        end = len(piles)-2
        sum = 0
        while start <= end:
            sum += piles[end]
            start += 1
            end-=2
        return sum


        