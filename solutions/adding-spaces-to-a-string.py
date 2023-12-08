class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        count = 0
        result = ""
        space =0
        for i in s:
            if space <= len(spaces)-1 and count == spaces[space]:
                result += " "
                space+=1
            result+=i
            count +=1
        return result
        
        