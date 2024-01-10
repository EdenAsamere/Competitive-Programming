class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        length = n + 1
        j = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            while curr_sum >= target:
                length = min(length,i-j+1)
                curr_sum -= nums[j]
                j+=1      
        return length if length !=n+1 else 0
            
    