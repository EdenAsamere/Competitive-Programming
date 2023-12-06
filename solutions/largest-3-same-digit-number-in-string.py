class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxSum = 0
        for i in range(len(num)- 3 + 1):
            if len(set(num[i:i+3])) == 1:
                maxSum = max(maxSum,int(num[i:i+3]))
        if maxSum > 0:
            return str(maxSum)
        elif maxSum == 0 and "000" in num:
            return "000"
        else:
            return ""
