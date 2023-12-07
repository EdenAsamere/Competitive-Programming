class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[:n+1]
        nums2 = nums[n:]
        result =[]
        for i,j in list(zip(nums1,nums2)):
            result.append(i)
            result.append(j)
        return result
        