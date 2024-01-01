class Solution:
    def smallestNumber(self, num: int) -> int:
        numStr = str(num)
        
        if num < 0:
            sortedNum = sorted(numStr[1:], reverse=True)
            return -int("".join(sortedNum))
        else:
            sortedNum = sorted(numStr)
            for i in range(len(sortedNum)):
                if sortedNum[i] != '0':
                    tmp = sortedNum[i]
                    sortedNum[i] = sortedNum[0]
                    sortedNum[0] = tmp
                    break
            return int("".join(sortedNum))