from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freqmap = Counter(arr)
        for item,freq in freqmap.items():
            if freq > (len(arr) * 0.25):
                return item
                