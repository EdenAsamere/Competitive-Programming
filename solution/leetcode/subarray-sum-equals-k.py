class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dic={0:1}
        n =len(nums)
        count = 0
        sub_sum = 0
        for i in nums:
            sub_sum += i
            if sub_sum - k in sum_dic:
                count+= sum_dic[sub_sum-k]
            if sub_sum in sum_dic:
                sum_dic[sub_sum] +=1
            else:
                sum_dic[sub_sum] =1
        return count
            