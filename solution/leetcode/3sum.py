class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 or (len(nums) == 1 and nums[0] == 0):
            return []
        nums.sort()
        result = set()
        for i, n in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curSum = nums[left] + nums[i] + nums[right]
                if (curSum) == 0:
                    result.add((nums[left], nums[i], nums[right]))
                    left += 1
                    right -= 1
                elif (curSum) < 0:
                    left += 1
                else:
                    right -= 1
        return result
                