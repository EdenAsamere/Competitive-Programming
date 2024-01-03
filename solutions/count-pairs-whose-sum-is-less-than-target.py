class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        start,end = 0,len(nums)-1
        while start < end:
            if nums[start] + nums[end] < target:
                count += end - start
                start += 1
            else:
                end-= 1
        return count