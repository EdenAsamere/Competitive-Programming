class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        j = len(cardPoints) - k
        i = 0
        total = sum(cardPoints[j:])
        k = total
        while j < len(cardPoints):
            total += (cardPoints[i] - cardPoints[j])
            k = max(k,total)
            j += 1
            i += 1
        return k
