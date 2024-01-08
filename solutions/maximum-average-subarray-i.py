class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        maxSum = window_sum

        i = 0
        for j in range(k,len(nums)):
            window_sum += nums[j]
            window_sum -= nums[i]
            i +=1
            maxSum = max(window_sum,maxSum)

        return maxSum/k
        