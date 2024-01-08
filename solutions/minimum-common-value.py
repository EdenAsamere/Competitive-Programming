class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        minCommon = float('inf')
        first = 0
        second = 0
        while first < len(nums1) and second < len(nums2):
            if nums1[first] == nums2[second]:
                minCommon = min(minCommon , nums1[first])     
                first +=1
                second +=1
            elif nums1[first] > nums2[second]:
                second+=1
            else:
                first +=1      
        return minCommon if minCommon != float('inf') else -1
       
                
                
            
        
        