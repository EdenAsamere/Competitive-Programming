class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        j = 0
        uniques = defaultdict(int)
        cur_sum=0
        max_score=0
        for i in range(len(nums)):
            cur_sum+=nums[i]
            uniques[nums[i]]+=1
            while uniques[nums[i]] >1:
                cur_sum-=nums[j]
                uniques[nums[j]]-=1
                j+=1
            max_score=max(cur_sum,max_score)
        return max_score
