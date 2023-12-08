class Solution:
    def largestOddNumber(self, num: str) -> str:
        if int(num[-1]) % 2 :
            return num
        for r in range(len(num)-1,-1,-1):
            if int(num[r]) % 2 != 0:
                return num[:r+1]
        return ""

                    
                