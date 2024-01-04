class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        first = second = count =0
        while first < len(g) and second < len(s):
            if g[first] <= s[second]:
                count += 1
                first += 1
                second+= 1
            elif g[first] > s[second]:
                second += 1
        return count
            
        