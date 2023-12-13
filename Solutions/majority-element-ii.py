from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_table = Counter(nums)
        return [i for i,j in freq_table.items() if j >= (len(nums)//3 ) + 1 ]
                
        
        