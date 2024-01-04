class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        first = 0
        second = len(skill)-1
        chemistry = 0
        t_sum = skill[first] + skill[second]

        while first < second:
            summ = skill[first] + skill[second]
            if t_sum != summ:
                return -1
            chemistry += (skill[first] *skill[second])
            first += 1
            second -= 1

        return chemistry
                
        