class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        init_to_target = abs(target[0])+ abs(target[1])
        for x ,y in ghosts:
            target_to_ghost=abs(target[0]-x)+abs(target[1]-y)
            if target_to_ghost<=init_to_target:
                return False
        return True
            