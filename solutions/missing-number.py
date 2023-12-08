class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashmap = {i:j for i,j in enumerate(list(range(len(nums)+1)))}
        for key in hashmap:
            if key not in nums:
                return key
            
        