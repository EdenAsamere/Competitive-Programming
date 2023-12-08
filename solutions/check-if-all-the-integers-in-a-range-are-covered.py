class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        new_list =[]
        
        for j in range(len(ranges)):
            new_list.extend(list(range(ranges[j][0],ranges[j][1]+1)))
        print(new_list)
        for i in range(left, right+1):
            if i not in new_list:
                return False
        
        return True