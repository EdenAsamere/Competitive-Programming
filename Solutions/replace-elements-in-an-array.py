class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashmap = {num: i for i, num in enumerate(nums)}
        for old, new in operations:
            temp = hashmap[old]
            nums[temp] = new
            hashmap[new] = temp
            del hashmap[old]
        return nums
                       
        
 