class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        frequency_map ={}
        output = []
        for i in nums:
            if i in frequency_map:
                frequency_map[i]+=1
            else:
                frequency_map[i] =1
        for val,freq in frequency_map.items():
            if freq>n//3:
                output.append(val)
        return output
                
        