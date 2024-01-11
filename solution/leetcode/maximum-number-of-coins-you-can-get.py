class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        end = len(piles)
        start = 0
        my_sum = 0
        while start < end:
            end-=2
            my_sum += piles[end]
            start +=1
        return my_sum
            
            