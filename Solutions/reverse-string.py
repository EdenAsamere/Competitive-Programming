class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        end = len(s)-1
        while left < end:
            s[left],s[end] = s[end],s[left]
            left+=1
            end-=1