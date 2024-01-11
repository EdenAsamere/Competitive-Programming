class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        na = 0
        ty = 0
        while na <= len(name) and ty < len(typed):
            if na < len(name) and name[na] == typed[ty]:
                na +=1
                ty +=1
            elif typed[ty] == name[na-1] and na != 0:
                ty += 1
            else:
                return False
            
        return na == len(name) and ty == len(typed)
            
        