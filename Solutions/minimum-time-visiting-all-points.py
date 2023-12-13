class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        i = 0
        while i < len(points) -1 :
            diff1 = abs(points[i][0] - points[i+1][0])
            diff2 = abs(points[i][1] - points[i+1][1])
            diff = abs(diff2 - diff1)
            result += (min(diff1,diff2) + diff)
            i+=1
        return result
                
            