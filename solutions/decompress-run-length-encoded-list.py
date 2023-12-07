class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        j = 1
        while i < j and j < len(nums):
            freq = nums[i]
            val = nums[j]
            result.extend([val]*freq)
            i+=2
            j+=2
        return result

        