class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        f,n =0,len(nums)-1
        count = 0
        while f < n:
            if nums[f] + nums[n] == k:
                nums.pop(f)
                nums.pop(n-1) 
                count +=1
                n-=2
            elif nums[f] + nums[n] < k:
                f+=1
            else:
                n-=1                
        return count
                
    [1,3,3,3,4]
    
                
                
            